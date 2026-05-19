# Maharashtra Future Land Predictions

An AI-powered land use analytics and prediction system for Maharashtra, India. This project combines machine learning models with an interactive web interface to predict future land use patterns, urban sprawl, agricultural degradation, and land prices across all 36 districts of Maharashtra.

## Features

### Core Features
- **Land Use Prediction** - Predicts future urban, agricultural, and forest land percentages.
- **Land Price Prediction** - Random Forest Regressor predicting land prices per sqft based on socio-economic and climate factors.
- **Land Type Classification** - Random Forest Classifier classifying satellite imagery features (NDVI, NDBI, etc.).
- **Time Series Forecasting** - LSTM neural network for multi-year land use trend prediction.
- **Urban Sprawl Predictor** - Specialized model for analyzing urban expansion patterns.
- **Agricultural Degradation** - Monitors soil quality and predicts agricultural land loss.

### Web Dashboard
- **Interactive Map** - Leaflet-based map with district markers and heatmap layers
- **Real-time Predictions** - Multi-year forecast visualization
- **Data Visualization** - Plotly charts for land use, prices, and trends
- **AI Insights** - Automated recommendations based on predictions

### Supported Districts (36)
Mumbai, Pune, Nagpur, Thane, Nashik, Aurangabad, Solapur, Amravati, Kolhapur, Navi Mumbai, Akola, Jalgaon, Latur, Ahmednagar, Chandrapur, Parbhani, Jalna, Nanded, Satara, Beed, Yavatmal, Osmanabad, Wardha, Sangli, Gondia, Hingoli, Gadchiroli, Washim, Buldhana, Bhandara, Palghar, Raigad, Ratnagiri, Sindhudurg, Dhule, Nandurbar

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup
```bash
# Clone or extract the project
cd "Maharashtra Future Land Predictions"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Train Models (First Time)
```bash
python train_models.py
```

This generates synthetic training data and trains all ML models.

### Run Web Application
```bash
python app.py
```

Access the dashboard at: http://localhost:5000

## Deployment

To deploy this project from your GitHub repository:

### 1. GitHub Actions (Optional)
The project is set up for automatic deployment to platforms like **Render** or **Railway**.

### 2. Manual Deployment (e.g., Render)
1. Connect your GitHub repository to Render.com.
2. Select "Web Service".
3. Use the following settings:
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### 3. Environment Variables
No specific environment variables are required, but you can set `PORT` if your hosting provider requires a specific one.

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard |
| `/api/districts` | GET | List all districts |
| `/api/district/<name>` | GET | District details |
| `/api/predict/land-use/<district>` | GET | Land use predictions |
| `/api/predict/land-price/<district>` | GET | Price forecasts |
| `/api/predict/urban-sprawl/<district>` | GET | Urban expansion |
| `/api/predict/agricultural-degradation/<district>` | GET | Degradation analysis |
| `/api/classify/land-type` | POST | Classify from satellite features |
| `/api/analyze/statewide` | GET | Statewide statistics |
| `/api/data/heatmap/<metric>` | GET | Heatmap data |

## Project Structure
```
├── app.py                    # Flask web application
├── train_models.py           # Model training script
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── data/
│   ├── maharashtra_districts.py    # District data
│   └── data_generator.py             # Synthetic data generator
│
├── models/
│   └── land_use_predictor.py       # ML model classes
│
├── web/
│   ├── templates/
│   │   └── index.html                # Dashboard UI
│   └── static/                       # Static assets
│
├── datasets/                 # Generated data (created on run)
│   ├── historical_land_use.csv
│   ├── satellite_features.csv
│   └── climate_projections.csv
│
└── saved_models/             # Trained models (created on run)
    ├── land_price_model.pkl
    ├── land_classifier.pkl
    ├── time_series_model.h5
    └── ...
```

## Technologies Used
- **Backend**: Flask, Flask-CORS
- **Machine Learning**: scikit-learn, TensorFlow/Keras (LSTM), XGBoost
- **Data Science**: NumPy, Pandas
- **Visualization**: Plotly, Leaflet.js
- **Frontend**: HTML5, CSS3, JavaScript

## Model Details

### Land Price Prediction
- Algorithm: Random Forest Regressor (200 estimators)
- Features: Population, area, rainfall, temperature, industrial zones, water bodies, soil quality, GDP contribution
- Metrics: R² Score > 0.85

### Land Type Classification
- Algorithm: Random Forest Classifier (150 estimators)
- Features: NDVI, NDBI, NDWI, surface temperature, elevation, slope, texture
- Classes: urban, agricultural, forest, water, barren
- Accuracy: > 90%

### Time Series Forecasting
- Algorithm: LSTM Neural Network (2 layers)
- Sequence Length: 5 years
- Purpose: Predict future urban/agricultural/forest percentages

## Unique Features

1. **Multi-Model Ensemble** - Combines Random Forest, LSTM, and specialized predictors
2. **Satellite Simulation** - Generates synthetic NDVI, NDBI, NDWI indices
3. **Climate Integration** - Incorporates rainfall and temperature projections
4. **Soil Quality Tracking** - Monitors agricultural degradation over time
5. **Interactive Visualizations** - Real-time map updates with metric switching

## License
MIT License

## Author
AI-Generated Project for Maharashtra Future Land Predictions
