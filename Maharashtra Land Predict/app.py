"""
Maharashtra Future Land Predictions - Flask Web Application
"""
import os
import json
import numpy as np
import pandas as pd
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import sys

# Add modules to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data.maharashtra_districts import DISTRICTS, DISTRICT_FEATURES
from data.maharashtra_talukas import ALL_TALUKAS, get_all_talukas_flat, get_taluka_price
from data.data_generator import MaharashtraDataGenerator
from models.land_use_predictor import LandUsePredictor, UrbanSprawlPredictor, AgriculturalLandDegradationPredictor

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
CORS(app)

# Global model instances
predictor = LandUsePredictor()
urban_predictor = UrbanSprawlPredictor()
agri_predictor = AgriculturalLandDegradationPredictor()
historical_data = None
satellite_data = None
models_initialized = False

def initialize_models():
    """Initialize and train models on startup"""
    global historical_data, satellite_data, models_initialized
    
    if models_initialized:
        return

    print("Initializing Maharashtra Future Land Predictions System...")
    
    # Generate data
    generator = MaharashtraDataGenerator(start_year=2010, end_year=2023)
    os.makedirs('./datasets', exist_ok=True)
    os.makedirs('./saved_models', exist_ok=True)
    
    historical_data, satellite_data, _ = generator.save_data('./datasets')
    
    # Check if pre-trained models exist
    if os.path.exists('./saved_models/land_price_model.pkl'):
        print("Loading pre-trained models...")
        predictor.load_models('./saved_models')
    else:
        print("Training new models...")
        predictor.train_all(historical_data, satellite_data)
        predictor.save_models('./saved_models')
    
    # Train specialized models
    urban_predictor.train(historical_data)
    agri_predictor.train(historical_data)
    
    models_initialized = True
    print("System ready!")

# Initialize models at module level for production servers
try:
    initialize_models()
except Exception as e:
    print(f"Error during initialization: {e}")


@app.route('/')
def index():
    """Main dashboard page"""
    return render_template('index.html')


@app.route('/api/districts')
def get_districts():
    """Get all districts with coordinates and latest metrics"""
    districts_list = []

    # Get latest data from historical_data
    latest_stats = {}
    if historical_data is not None:
        latest_data = historical_data.groupby('district').last()
        latest_stats = latest_data.to_dict('index')

    for dist in DISTRICTS:
        feat = DISTRICT_FEATURES.get(dist, {})
        stats = latest_stats.get(dist, {})

        districts_list.append({
            'name': dist,
            'lat': feat.get('lat', 19.0),
            'lon': feat.get('lon', 75.0),
            'population': int(stats.get('population', feat.get('population_2023', 0))),
            'land_type': feat.get('land_type', 'Unknown'),
            'urban_pct': float(stats.get('urban_pct', feat.get('urban_pct', 40))),
            'forest_pct': float(stats.get('forest_pct', feat.get('forest_cover_pct', 20))),
            'area_sqkm': feat.get('area_sqkm', 100)
        })
    return jsonify(districts_list)


@app.route('/api/district/<district_name>')
def get_district_details(district_name):
    """Get detailed information for a specific district"""
    if district_name not in DISTRICTS:
        return jsonify({'error': 'District not found'}), 404
        
    feat = DISTRICT_FEATURES.get(district_name, {})
    
    # Get historical data for this district
    district_history = historical_data[historical_data['district'] == district_name].to_dict('records')
    
    return jsonify({
        'name': district_name,
        'features': feat,
        'historical_data': district_history
    })


@app.route('/api/predict/land-use/<district_name>')
def predict_land_use(district_name):
    """Predict future land use percentages"""
    if district_name not in DISTRICTS:
        return jsonify({'error': 'District not found'}), 404
        
    years = request.args.get('years', 5, type=int)
    
    district_hist = historical_data[historical_data['district'] == district_name]
    
    if len(district_hist) == 0:
        return jsonify({'error': 'No historical data available'}), 404
    
    # Get LSTM predictions
    urban_preds = predictor.predict_future_land_use(district_hist, years)
    
    # Get current values
    current = district_hist.iloc[-1]
    
    # Calculate other land types based on urban growth
    predictions = []
    for i, urban_pct in enumerate(urban_preds):
        year_offset = i + 1
        # As urban grows, agricultural decreases
        agri_decline = (urban_pct - current['urban_pct']) * 0.7
        agri_pct = max(0, current['agricultural_pct'] - agri_decline)
        
        # Forest may slightly decline
        forest_decline = (urban_pct - current['urban_pct']) * 0.2
        forest_pct = max(0, current['forest_pct'] - forest_decline)
        
        # Other land adjusts
        other_pct = max(0, 100 - urban_pct - agri_pct - forest_pct)
        
        predictions.append({
            'year': 2024 + i,
            'urban_pct': round(urban_pct, 2),
            'agricultural_pct': round(agri_pct, 2),
            'forest_pct': round(forest_pct, 2),
            'other_pct': round(other_pct, 2)
        })
    
    return jsonify({
        'district': district_name,
        'current': {
            'year': int(current['year']),
            'urban_pct': current['urban_pct'],
            'agricultural_pct': current['agricultural_pct'],
            'forest_pct': current['forest_pct']
        },
        'predictions': predictions
    })


@app.route('/api/predict/land-price/<district_name>')
def predict_land_price(district_name):
    """Predict land prices for future years"""
    if district_name not in DISTRICTS:
        return jsonify({'error': 'District not found'}), 404
        
    years = request.args.get('years', 5, type=int)
    
    district_hist = historical_data[historical_data['district'] == district_name]
    
    if len(district_hist) == 0:
        return jsonify({'error': 'No historical data available'}), 404
    
    predictions = []
    current = district_hist.iloc[-1]
    
    for year_offset in range(1, years + 1):
        year = 2023 + year_offset
        
        # Prepare features for prediction
        features = {
            'population': current['population'] * (1.015 ** year_offset),
            'area_sqkm': current['area_sqkm'],
            'avg_rainfall_mm': current['avg_rainfall_mm'] - 5 * year_offset,  # Climate change
            'temperature_anomaly_c': current['temperature_anomaly_c'] + 0.15 * year_offset,
            'industrial_zones': int(current['industrial_zones'] + year_offset * 0.3),
            'water_bodies': current['water_bodies'],
            'water_table_depth_m': current['water_table_depth_m'] + 0.3 * year_offset,
            'soil_quality_index': max(30, current['soil_quality_index'] - year_offset * 0.8),
            'gdp_contribution_cr': current['gdp_contribution_cr'] * (1.05 ** year_offset)
        }
        
        # Add one-hot encoded features
        for col in predictor.price_feature_cols:
            if col.startswith('soil_type_'):
                features[col] = 1 if current['soil_type'] in col else 0
            elif col.startswith('land_type_'):
                features[col] = 1 if current['land_type'] in col else 0
        
        price = predictor.predict_land_price(features)
        
        predictions.append({
            'year': year,
            'predicted_price_rs_per_sqft': round(price, 2),
            'confidence': 'High' if year_offset <= 3 else 'Medium'
        })
    
    return jsonify({
        'district': district_name,
        'current_price': current['land_price_rs_per_sqft'],
        'predictions': predictions
    })


@app.route('/api/predict/urban-sprawl/<district_name>')
def predict_urban_sprawl(district_name):
    """Predict urban sprawl patterns"""
    if district_name not in DISTRICTS:
        return jsonify({'error': 'District not found'}), 404
        
    years = request.args.get('years', 10, type=int)
    
    district_hist = historical_data[historical_data['district'] == district_name]
    current = district_hist.iloc[-1].to_dict()
    
    predictions = urban_predictor.predict_urban_expansion(current, years)
    
    return jsonify({
        'district': district_name,
        'current_urban_pct': current['urban_pct'],
        'predictions': predictions
    })


@app.route('/api/predict/agricultural-degradation/<district_name>')
def predict_agricultural_degradation(district_name):
    """Predict agricultural land degradation"""
    if district_name not in DISTRICTS:
        return jsonify({'error': 'District not found'}), 404
        
    years = request.args.get('years', 10, type=int)
    
    district_hist = historical_data[historical_data['district'] == district_name]
    current = district_hist.iloc[-1].to_dict()
    
    predictions = agri_predictor.predict_degradation(current, years)
    
    return jsonify({
        'district': district_name,
        'current_soil_quality': current['soil_quality_index'],
        'predictions': predictions
    })


@app.route('/api/classify/land-type', methods=['POST'])
def classify_land_type():
    """Classify land type from satellite features"""
    data = request.json
    
    satellite_features = {
        'ndvi': data.get('ndvi', 0),
        'ndbi': data.get('ndbi', 0),
        'ndwi': data.get('ndwi', 0),
        'surface_temp_c': data.get('surface_temp_c', 30),
        'elevation_m': data.get('elevation_m', 100),
        'slope_degrees': data.get('slope_degrees', 5),
        'texture_contrast': data.get('texture_contrast', 0.5),
        'texture_homogeneity': data.get('texture_homogeneity', 0.5)
    }
    
    result = predictor.predict_land_type(satellite_features)
    
    if result is None:
        return jsonify({'error': 'Model not trained'}), 500
    
    return jsonify({
        'predicted_land_type': result['land_type'],
        'confidence': round(result['confidence'] * 100, 2)
    })


@app.route('/api/analyze/statewide')
def analyze_statewide():
    """Get statewide analysis and predictions"""
    # Calculate aggregates
    total_population = historical_data.groupby('district')['population'].last().sum()
    avg_urban = historical_data.groupby('district')['urban_pct'].last().mean()
    avg_forest = historical_data.groupby('district')['forest_pct'].last().mean()
    avg_agri = historical_data.groupby('district')['agricultural_pct'].last().mean()
    
    # Top growing districts
    growth_data = []
    for district in DISTRICTS:
        dist_data = historical_data[historical_data['district'] == district]
        if len(dist_data) >= 2:
            urban_growth = dist_data['urban_pct'].iloc[-1] - dist_data['urban_pct'].iloc[0]
            growth_data.append({'district': district, 'urban_growth': urban_growth})
    
    top_growing = sorted(growth_data, key=lambda x: x['urban_growth'], reverse=True)[:5]
    
    return jsonify({
        'total_population': int(total_population),
        'average_urban_pct': round(avg_urban, 2),
        'average_forest_pct': round(avg_forest, 2),
        'average_agricultural_pct': round(avg_agri, 2),
        'top_urbanizing_districts': top_growing,
        'total_districts': len(DISTRICTS)
    })


@app.route('/api/data/heatmap/<metric>')
def get_heatmap_data(metric):
    """Get data for heatmap visualization"""
    valid_metrics = ['urban_pct', 'forest_pct', 'agricultural_pct', 'land_price_rs_per_sqft',
                     'population', 'industrial_zones', 'soil_quality_index']
    
    if metric not in valid_metrics:
        return jsonify({'error': 'Invalid metric'}), 400
    
    latest_data = historical_data.groupby('district').last().reset_index()
    
    heatmap_data = []
    for _, row in latest_data.iterrows():
        heatmap_data.append({
            'district': row['district'],
            'lat': row['lat'],
            'lon': row['lon'],
            'value': row.get(metric, 0)
        })
    
    return jsonify({
        'metric': metric,
        'data': heatmap_data
    })


@app.route('/api/talukas')
def get_talukas():
    """Get all talukas with prices"""
    return jsonify(get_all_talukas_flat())


@app.route('/api/talukas/<district>')
def get_district_talukas(district):
    """Get talukas for a specific district"""
    if district in ALL_TALUKAS:
        talukas = ALL_TALUKAS[district]
        return jsonify({
            'district': district,
            'talukas': talukas,
            'count': len(talukas)
        })
    return jsonify({'error': 'District not found'}), 404


@app.route('/api/taluka/<taluka_name>')
def get_taluka_details(taluka_name):
    """Get details and price for a specific taluka"""
    all_talukas = get_all_talukas_flat()
    for taluka in all_talukas:
        if taluka['name'].lower() == taluka_name.lower():
            current_price = get_taluka_price(taluka_name, 2024)
            future_price = get_taluka_price(taluka_name, 2030)
            return jsonify({
                'taluka': taluka['name'],
                'district': taluka['district'],
                'coordinates': {'lat': taluka['lat'], 'lon': taluka['lon']},
                'base_price_2023': taluka['base_price'],
                'current_price_2024': current_price,
                'predicted_price_2030': future_price,
                'zone_type': taluka['zone'],
                'infrastructure_score': taluka['infra_score'],
                'appreciation_rate': round(((future_price/current_price)**(1/6) - 1)*100, 2) if current_price else None
            })
    return jsonify({'error': 'Taluka not found'}), 404


@app.route('/api/talukas/prices/<zone_type>')
def get_talukas_by_zone(zone_type):
    """Get talukas filtered by zone type"""
    all_talukas = get_all_talukas_flat()
    filtered = [t for t in all_talukas if t['zone'] == zone_type]
    
    # Calculate price statistics
    prices = [get_taluka_price(t['name'], 2024) for t in filtered]
    
    return jsonify({
        'zone_type': zone_type,
        'talukas': filtered,
        'count': len(filtered),
        'price_stats': {
            'min': min(prices) if prices else 0,
            'max': max(prices) if prices else 0,
            'avg': round(sum(prices)/len(prices), 2) if prices else 0
        }
    })


@app.route('/api/talukas/top-priced')
def get_top_priced_talukas():
    """Get top priced talukas"""
    limit = request.args.get('limit', 20, type=int)
    all_talukas = get_all_talukas_flat()
    
    # Calculate current prices
    priced_talukas = []
    for t in all_talukas:
        price = get_taluka_price(t['name'], 2024)
        t_copy = t.copy()
        t_copy['current_price'] = price
        priced_talukas.append(t_copy)
    
    # Sort by price
    top_talukas = sorted(priced_talukas, key=lambda x: x['current_price'], reverse=True)[:limit]
    
    return jsonify({
        'top_talukas': top_talukas,
        'count': len(top_talukas)
    })


if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
