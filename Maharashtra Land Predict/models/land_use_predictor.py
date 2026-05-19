"""
Maharashtra Land Use Prediction Models
Includes Random Forest for land classification and ARIMA for time series forecasting
"""
import numpy as np
import pandas as pd
import joblib
import json
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, r2_score, classification_report, accuracy_score
import warnings
warnings.filterwarnings('ignore')


class LandUsePredictor:
    """Multi-model system for land use predictions"""
    
    def __init__(self):
        self.land_price_model = None
        self.land_classification_model = None
        self.time_series_model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        self.is_trained = False
        
    def prepare_features(self, df):
        """Prepare features for modeling"""
        feature_cols = [
            'population', 'area_sqkm', 'avg_rainfall_mm', 'temperature_anomaly_c',
            'industrial_zones', 'water_bodies', 'water_table_depth_m',
            'soil_quality_index', 'gdp_contribution_cr'
        ]
        
        # One-hot encode categorical features
        df_encoded = pd.get_dummies(df, columns=['soil_type', 'land_type'], drop_first=True)
        
        # Get numeric features that exist
        available_cols = [c for c in df_encoded.columns if c in feature_cols or 
                          c.startswith('soil_type_') or c.startswith('land_type_')]
        
        return df_encoded[available_cols]
    
    def train_land_price_model(self, df):
        """Train Random Forest model for land price prediction"""
        print("Training Land Price Prediction Model...")
        
        X = self.prepare_features(df)
        y = df['land_price_rs_per_sqft']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        model = RandomForestRegressor(
            n_estimators=200,
            max_depth=15,
            min_samples_split=5,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=-1
        )
        
        model.fit(X_train_scaled, y_train)
        
        y_pred = model.predict(X_test_scaled)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Land Price Model - RMSE: {np.sqrt(mse):.2f}, R2: {r2:.4f}")
        
        self.land_price_model = model
        self.price_feature_cols = X.columns.tolist()
        
        return {'rmse': np.sqrt(mse), 'r2': r2}
    
    def train_land_classification_model(self, df):
        """Train Random Forest classifier for land type classification"""
        print("Training Land Classification Model...")
        
        feature_cols = [
            'ndvi', 'ndbi', 'ndwi', 'surface_temp_c', 'elevation_m',
            'slope_degrees', 'texture_contrast', 'texture_homogeneity'
        ]
        
        X = df[feature_cols]
        y = self.label_encoder.fit_transform(df['land_type'])
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = RandomForestClassifier(
            n_estimators=150,
            max_depth=12,
            min_samples_split=10,
            random_state=42,
            n_jobs=-1
        )
        
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        
        print(f"Land Classification Model - Accuracy: {accuracy:.4f}")
        
        self.land_classification_model = model
        self.class_feature_cols = feature_cols
        
        return {'accuracy': accuracy}
    
    def train_time_series_model(self, df, target='urban_pct', epochs=100):
        """Train time series forecasting using trend analysis"""
        print(f"Training Time Series Model for {target} prediction...")
        
        # Store target column for predictions
        self.ts_target = target
        
        # Calculate overall trend statistics
        districts = df['district'].unique()
        trends = []
        
        for district in districts:
            district_data = df[df['district'] == district].sort_values('year')
            values = district_data[target].values
            
            if len(values) >= 3:
                # Calculate year-over-year growth rates
                growth_rates = []
                for i in range(1, len(values)):
                    if values[i-1] != 0:
                        growth_rates.append((values[i] - values[i-1]) / values[i-1])
                
                if growth_rates:
                    trends.append(np.mean(growth_rates))
        
        self.ts_trend_stats = {
            'mean_growth': np.mean(trends) if trends else 0.02,
            'std_growth': np.std(trends) if trends else 0.01,
            'target': target
        }
        
        print(f"Time Series Model - Mean Growth Rate: {self.ts_trend_stats['mean_growth']:.4f}")
        
        return {'rmse': self.ts_trend_stats['std_growth'], 'trend_stats': self.ts_trend_stats}
    
    def predict_future_land_use(self, district_data, years_ahead=5):
        """Predict future land use percentages using trend extrapolation"""
        if not hasattr(self, 'ts_trend_stats'):
            return None
            
        recent_values = district_data[self.ts_target].tail(3).values
        current_value = recent_values[-1]
        
        predictions = []
        
        for i in range(years_ahead):
            # Apply trend with some noise
            growth = self.ts_trend_stats['mean_growth'] + np.random.normal(0, self.ts_trend_stats['std_growth'])
            
            # For urban_pct, cap at 95%
            if self.ts_target == 'urban_pct':
                growth = max(0, growth)  # Urban only grows
                current_value = min(95, current_value * (1 + growth) + np.random.normal(0, 0.5))
            else:
                current_value = current_value * (1 + growth)
            
            predictions.append(max(0, min(100, current_value)))
            
        return predictions
    
    def predict_land_price(self, features_dict):
        """Predict land price for a given set of features"""
        if self.land_price_model is None:
            return None
            
        # Create feature vector
        feature_vector = []
        for col in self.price_feature_cols:
            if col in features_dict:
                feature_vector.append(features_dict[col])
            elif col.startswith('soil_type_') or col.startswith('land_type_'):
                feature_vector.append(1 if features_dict.get(col, 0) else 0)
            else:
                feature_vector.append(0)
                
        feature_vector = np.array(feature_vector).reshape(1, -1)
        feature_vector_scaled = self.scaler.transform(feature_vector)
        
        return self.land_price_model.predict(feature_vector_scaled)[0]
    
    def predict_land_type(self, satellite_features):
        """Predict land type from satellite features"""
        if self.land_classification_model is None:
            return None
            
        features = np.array([satellite_features.get(col, 0) for col in self.class_feature_cols])
        features = features.reshape(1, -1)
        
        pred_encoded = self.land_classification_model.predict(features)[0]
        pred_proba = self.land_classification_model.predict_proba(features)[0]
        
        confidence = np.max(pred_proba)
        pred_label = self.label_encoder.inverse_transform([pred_encoded])[0]
        
        return {'land_type': pred_label, 'confidence': confidence}
    
    def save_models(self, output_dir='./saved_models'):
        """Save all trained models"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        if self.land_price_model:
            joblib.dump(self.land_price_model, f'{output_dir}/land_price_model.pkl')
            joblib.dump(self.scaler, f'{output_dir}/price_scaler.pkl')
            joblib.dump(self.price_feature_cols, f'{output_dir}/price_features.pkl')
            
        if self.land_classification_model:
            joblib.dump(self.land_classification_model, f'{output_dir}/land_classifier.pkl')
            joblib.dump(self.label_encoder, f'{output_dir}/label_encoder.pkl')
            joblib.dump(self.class_feature_cols, f'{output_dir}/class_features.pkl')
            
        if hasattr(self, 'ts_trend_stats'):
            with open(f'{output_dir}/time_series_stats.json', 'w') as f:
                json.dump(self.ts_trend_stats, f)
            
        print(f"Models saved to {output_dir}/")
        
    def load_models(self, model_dir='./saved_models'):
        """Load all saved models"""
        try:
            self.land_price_model = joblib.load(f'{model_dir}/land_price_model.pkl')
            self.scaler = joblib.load(f'{model_dir}/price_scaler.pkl')
            self.price_feature_cols = joblib.load(f'{model_dir}/price_features.pkl')
            
            self.land_classification_model = joblib.load(f'{model_dir}/land_classifier.pkl')
            self.label_encoder = joblib.load(f'{model_dir}/label_encoder.pkl')
            self.class_feature_cols = joblib.load(f'{model_dir}/class_features.pkl')
            
            # Load time series stats
            with open(f'{model_dir}/time_series_stats.json', 'r') as f:
                self.ts_trend_stats = json.load(f)
                self.ts_target = self.ts_trend_stats.get('target', 'urban_pct')
            
            self.is_trained = True
            print("Models loaded successfully")
        except Exception as e:
            print(f"Error loading models: {e}")
            self.is_trained = False
            
    def train_all(self, historical_df, satellite_df):
        """Train all models"""
        print("="*50)
        print("Training All Prediction Models")
        print("="*50)
        
        price_metrics = self.train_land_price_model(historical_df)
        class_metrics = self.train_land_classification_model(satellite_df)
        ts_metrics = self.train_time_series_model(historical_df)
        
        self.is_trained = True
        
        return {
            'land_price': price_metrics,
            'classification': class_metrics,
            'time_series': ts_metrics
        }


class UrbanSprawlPredictor:
    """Specialized model for predicting urban expansion patterns"""
    
    def __init__(self):
        self.model = RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def train(self, df):
        """Train urban sprawl prediction model"""
        features = [
            'population', 'gdp_contribution_cr', 'industrial_zones',
            'water_table_depth_m', 'land_price_rs_per_sqft',
            'year'
        ]
        
        X = df[features]
        y = df['urban_pct']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        X_train_scaled = self.scaler.fit_transform(X_train)
        
        self.model.fit(X_train_scaled, y_train)
        self.feature_names = features
        
        # Feature importance
        importance = dict(zip(features, self.model.feature_importances_))
        print("Urban Sprawl Feature Importance:", importance)
        
    def predict_urban_expansion(self, district_features, years=5):
        """Predict urban expansion over time"""
        predictions = []
        
        for year_offset in range(1, years + 1):
            features = district_features.copy()
            features['year'] = 2023 + year_offset
            
            # Simulate population growth
            features['population'] = features.get('population', 500000) * (1.015 ** year_offset)
            
            X = np.array([[features.get(f, 0) for f in self.feature_names]])
            X_scaled = self.scaler.transform(X)
            
            pred = self.model.predict(X_scaled)[0]
            predictions.append({
                'year': 2023 + year_offset,
                'urban_pct': min(98, max(0, pred))
            })
            
        return predictions


class AgriculturalLandDegradationPredictor:
    """Predict agricultural land degradation patterns"""
    
    def __init__(self):
        self.model = None
        
    def train(self, df):
        """Train degradation prediction model"""
        features = [
            'agricultural_pct', 'avg_rainfall_mm', 'temperature_anomaly_c',
            'soil_quality_index', 'water_table_depth_m', 'industrial_zones'
        ]
        
        X = df[features]
        y = df['soil_quality_index']  # Target: soil quality
        
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(X, y)
        self.feature_names = features
        
    def predict_degradation(self, district_features, years=5):
        """Predict soil quality and agricultural land degradation"""
        predictions = []
        base_soil = district_features.get('soil_quality_index', 70)
        
        for year_offset in range(1, years + 1):
            features = district_features.copy()
            # Simulate degradation factors
            features['temperature_anomaly_c'] = features.get('temperature_anomaly_c', 0) + 0.15 * year_offset
            features['water_table_depth_m'] = features.get('water_table_depth_m', 10) + 0.3 * year_offset
            
            X = np.array([[features.get(f, 0) for f in self.feature_names]])
            pred_soil = self.model.predict(X)[0]
            
            # Calculate degradation metrics
            degradation_rate = (base_soil - pred_soil) / base_soil * 100
            
            predictions.append({
                'year': 2023 + year_offset,
                'soil_quality': round(pred_soil, 2),
                'degradation_rate': round(degradation_rate, 2),
                'agri_sustainability': 'High' if pred_soil > 70 else 'Medium' if pred_soil > 50 else 'Low'
            })
            
        return predictions
