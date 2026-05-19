"""
Model Training Script for Maharashtra Future Land Predictions
Train and save all ML models for deployment
"""
import os
import sys
import numpy as np
import pandas as pd
from data.maharashtra_districts import DISTRICTS, DISTRICT_FEATURES
from data.data_generator import MaharashtraDataGenerator
from models.land_use_predictor import LandUsePredictor, UrbanSprawlPredictor, AgriculturalLandDegradationPredictor


def main():
    print("="*60)
    print("Maharashtra Future Land Predictions - Model Training Pipeline")
    print("="*60)
    
    # Create directories
    os.makedirs('./datasets', exist_ok=True)
    os.makedirs('./saved_models', exist_ok=True)
    
    # Generate data
    print("\n[1/5] Generating synthetic training data...")
    generator = MaharashtraDataGenerator(start_year=2010, end_year=2023)
    
    historical_data = generator.generate_historical_data()
    satellite_data = generator.generate_satellite_features(n_samples=10000)
    climate_data = generator.generate_climate_projections(years_ahead=15)
    
    # Save datasets
    historical_data.to_csv('./datasets/historical_land_use.csv', index=False)
    satellite_data.to_csv('./datasets/satellite_features.csv', index=False)
    climate_data.to_csv('./datasets/climate_projections.csv', index=False)
    
    print(f"  [OK] Generated {len(historical_data)} historical records")
    print(f"  [OK] Generated {len(satellite_data)} satellite feature records")
    print(f"  [OK] Generated {len(climate_data)} climate projection records")
    
    # Train main predictor
    print("\n[2/5] Training main land use prediction models...")
    predictor = LandUsePredictor()
    metrics = predictor.train_all(historical_data, satellite_data)
    
    print(f"  [OK] Land Price Model - R2 Score: {metrics['land_price']['r2']:.4f}")
    print(f"  [OK] Classification Model - Accuracy: {metrics['classification']['accuracy']:.4f}")
    if metrics['time_series']:
        print(f"  [OK] Time Series Model - RMSE: {metrics['time_series']['rmse']:.4f}")
    
    # Save models
    predictor.save_models('./saved_models')
    print("  [OK] Models saved to ./saved_models/")
    
    # Train urban sprawl predictor
    print("\n[3/5] Training urban sprawl prediction model...")
    urban_predictor = UrbanSprawlPredictor()
    urban_predictor.train(historical_data)
    print("  [OK] Urban sprawl model trained")
    
    # Train agricultural degradation predictor
    print("\n[4/5] Training agricultural degradation prediction model...")
    agri_predictor = AgriculturalLandDegradationPredictor()
    agri_predictor.train(historical_data)
    print("  [OK] Agricultural degradation model trained")
    
    # Generate sample predictions
    print("\n[5/5] Running sample predictions...")
    test_districts = ["Mumbai", "Pune", "Nagpur", "Thane"]
    
    for district in test_districts:
        dist_data = historical_data[historical_data['district'] == district]
        
        if len(dist_data) > 0:
            # Test land price prediction
            sample_features = {
                'population': dist_data['population'].iloc[-1],
                'area_sqkm': dist_data['area_sqkm'].iloc[-1],
                'avg_rainfall_mm': dist_data['avg_rainfall_mm'].iloc[-1],
                'temperature_anomaly_c': dist_data['temperature_anomaly_c'].iloc[-1],
                'industrial_zones': dist_data['industrial_zones'].iloc[-1],
                'water_bodies': dist_data['water_bodies'].iloc[-1],
                'water_table_depth_m': dist_data['water_table_depth_m'].iloc[-1],
                'soil_quality_index': dist_data['soil_quality_index'].iloc[-1],
                'gdp_contribution_cr': dist_data['gdp_contribution_cr'].iloc[-1]
            }
            
            price_pred = predictor.predict_land_price(sample_features)
            
            # Test future predictions
            future = predictor.predict_future_land_use(dist_data, years_ahead=5)
            
            print(f"  [OK] {district}: Current Price Rs{dist_data['land_price_rs_per_sqft'].iloc[-1]:.0f}/sqft, "
                  f"Predicted Rs{price_pred:.0f}/sqft, Urban growth to {future[-1]:.1f}%")
    
    print("\n" + "="*60)
    print("Training Complete! Run 'python app.py' to start the web server.")
    print("="*60)


if __name__ == "__main__":
    main()
