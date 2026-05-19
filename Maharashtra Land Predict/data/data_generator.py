"""
Maharashtra Land Use Data Generator
Generates synthetic historical and future projection data for ML models
"""
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random
from .maharashtra_districts import DISTRICTS, DISTRICT_FEATURES

np.random.seed(42)
random.seed(42)


class MaharashtraDataGenerator:
    """Generates realistic land use data for Maharashtra districts"""
    
    def __init__(self, start_year=2010, end_year=2023):
        self.start_year = start_year
        self.end_year = end_year
        self.districts = DISTRICTS
        self.features = DISTRICT_FEATURES
        
    def generate_historical_data(self, n_years=None):
        """Generate historical land use data for all districts"""
        if n_years is None:
            n_years = self.end_year - self.start_year + 1
            
        data = []
        years = list(range(self.start_year, self.end_year + 1))
        
        for district in self.districts:
            feat = self.features.get(district, {})
            base_urban = feat.get("urban_pct", 40)
            base_agri = feat.get("agri_pct", 50)
            base_forest = feat.get("forest_cover_pct", 20)
            base_industrial = feat.get("industrial_zones", 5)
            
            # Growth factors based on district characteristics
            urban_growth_rate = 0.02 if "Urban" in feat.get("land_type", "") else 0.01
            agri_decline_rate = -0.015 if base_urban > 50 else -0.008
            forest_decline_rate = -0.005
            industrial_growth = 0.03 if feat.get("industrial_zones", 0) > 5 else 0.015
            
            for i, year in enumerate(years):
                # Simulate year-over-year changes with some noise
                urban_pct = base_urban + (urban_growth_rate * i * 100) + np.random.normal(0, 0.5)
                agri_pct = base_agri + (agri_decline_rate * i * 100) + np.random.normal(0, 0.5)
                forest_pct = base_forest + (forest_decline_rate * i * 100) + np.random.normal(0, 0.2)
                industrial = max(0, int(base_industrial + (industrial_growth * i) + np.random.normal(0, 0.5)))
                
                # Strict normalization to 100%
                urban_pct = max(1, min(95, urban_pct))
                agri_pct = max(1, min(95, agri_pct))
                forest_pct = max(1, min(95, forest_pct))

                total = urban_pct + agri_pct + forest_pct
                if total > 99:
                    scale = 99 / total
                    urban_pct *= scale
                    agri_pct *= scale
                    forest_pct *= scale

                other_pct = 100 - (urban_pct + agri_pct + forest_pct)
                
                # Climate variables
                rainfall = feat.get("avg_rainfall", 800) + np.random.normal(0, 100)
                temp_anomaly = 0.1 * i + np.random.normal(0, 0.3)  # Warming trend
                
                # Economic indicators
                land_price_per_sqft = self._calculate_land_price(district, year, urban_pct, feat)
                gdp_contribution = (urban_pct * 0.6 + industrial * 2) * (1 + 0.05 * i)

                # Land degradation metrics
                soil_quality = max(30, 100 - agri_decline_rate * 100 * i - temp_anomaly * 5)
                water_table_depth = 10 + 0.3 * i + np.random.normal(0, 1)  # Deepening water table
                
                data.append({
                    'district': district,
                    'year': year,
                    'urban_pct': round(urban_pct, 2),
                    'agricultural_pct': round(agri_pct, 2),
                    'forest_pct': round(forest_pct, 2),
                    'other_land_pct': round(other_pct, 2),
                    'industrial_zones': industrial,
                    'avg_rainfall_mm': round(rainfall, 2),
                    'temperature_anomaly_c': round(temp_anomaly, 2),
                    'land_price_rs_per_sqft': round(land_price_per_sqft, 2),
                    'gdp_contribution_cr': round(gdp_contribution, 2),
                    'soil_quality_index': round(soil_quality, 2),
                    'water_table_depth_m': round(water_table_depth, 2),
                    'population': int(feat.get("population_2023", 500000) * (0.85 + 0.015 * i)),
                    'lat': feat.get("lat", 19.0),
                    'lon': feat.get("lon", 75.0),
                    'area_sqkm': feat.get("area_sqkm", 100),
                    'water_bodies': feat.get("water_bodies", 3),
                    'soil_type': feat.get("soil_type", "Black Cotton"),
                    'land_type': feat.get("land_type", "Rural Inland")
                })
                
        return pd.DataFrame(data)
    
    def _calculate_land_price(self, district, year, urban_pct, features):
        """Calculate land price based on realistic Maharashtra market rates"""
        # Realistic base prices per sqft for Maharashtra (2023 rates)
        district_base_prices = {
            # Tier 1 - Prime Metropolitan (₹15,000 - ₹50,000 per sqft)
            "Mumbai": 35000,          # South Mumbai prime: 50,000+, Suburban: 20,000-35,000
            "Navi Mumbai": 18000,     # Vashi, Nerul: 15,000-25,000
            "Pune": 15000,          # Koregaon Park, Kalyani Nagar: 15,000-25,000
            "Thane": 12000,         # Ghodbunder Road, Thane West: 10,000-18,000
            
            # Tier 2 - Major Cities (₹5,000 - ₹12,000 per sqft)
            "Nashik": 6000,         # City center: 5,000-10,000
            "Aurangabad": 5500,     # CIDCO, City center: 4,000-8,000
            "Nagpur": 5000,         # Dharampeth, Civil Lines: 4,000-9,000
            "Kolhapur": 4500,       # City center: 3,500-7,000
            "Solapur": 3500,        # City areas: 2,500-6,000
            
            # Tier 3 - District Centers (₹2,000 - ₹5,000 per sqft)
            "Amravati": 3000,
            "Akola": 2800,
            "Jalgaon": 2800,
            "Latur": 2500,
            "Ahmednagar": 2500,
            "Nanded": 2500,
            "Sangli": 3000,
            "Dhule": 2200,
            
            # Tier 4 - Smaller Cities (₹1,000 - ₹3,000 per sqft)
            "Chandrapur": 1800,
            "Parbhani": 1500,
            "Jalna": 1500,
            "Beed": 1400,
            "Yavatmal": 1500,
            "Osmanabad": 1200,
            "Wardha": 1600,
            "Gondia": 1400,
            "Hingoli": 1000,
            "Gadchiroli": 1000,
            "Washim": 1200,
            "Buldhana": 1300,
            "Bhandara": 1400,
            "Nandurbar": 1200,
            
            # Coastal/Industrial Regions
            "Palghar": 4000,        # Developing area, near Mumbai
            "Raigad": 3500,         # Industrial corridor
            "Ratnagiri": 2500,      # Coastal city
            "Sindhudurg": 2000      # Tourist area
        }
        
        # Get base price for district, default to rural rate
        base_price = district_base_prices.get(district, 800)
        
        # Urban percentage multiplier (urban land costs more)
        urban_multiplier = 1 + (urban_pct / 100) * 2  # Up to 3x for 100% urban
        base_price *= urban_multiplier
        
        # Industrial zones premium (more industry = higher land value)
        industrial_multiplier = 1 + features.get("industrial_zones", 0) * 0.03
        base_price *= industrial_multiplier
        
        # Population density factor
        population = features.get("population_2023", 500000)
        if population > 1000000:
            base_price *= 1.3  # 30% premium for major cities
        elif population > 500000:
            base_price *= 1.15  # 15% premium for cities
            
        # Year appreciation (10-15% annual for prime locations, 8-10% for others)
        if district in ["Mumbai", "Pune", "Thane", "Navi Mumbai"]:
            appreciation_rate = 0.08  # Capped at 8% for averages
        elif district in ["Nashik", "Aurangabad", "Nagpur"]:
            appreciation_rate = 0.06
        else:
            appreciation_rate = 0.05
            
        year_factor = (1 + appreciation_rate) ** (year - 2020)
        base_price *= year_factor
        
        # Infrastructure development factor (random variation based on projects)
        infra_factor = 1 + np.random.normal(0.05, 0.15)  # Mean 5% boost
        base_price *= max(0.7, infra_factor)
        
        # Land type adjustment
        land_type = features.get("land_type", "")
        if "Coastal" in land_type:
            base_price *= 1.2  # 20% premium for coastal
        elif "Industrial" in land_type or "Zone" in land_type:
            base_price *= 1.15  # 15% premium for industrial zones
            
        return round(base_price, 2)
    
    def generate_satellite_features(self, n_samples=5000):
        """Generate synthetic satellite-derived features for land classification"""
        data = []
        
        for district in self.districts:
            feat = self.features.get(district, {})
            n_district_samples = n_samples // len(self.districts)
            
            for _ in range(n_district_samples):
                # Land type distribution
                land_type_weights = {
                    'urban': feat.get("urban_pct", 40) / 100,
                    'agricultural': feat.get("agri_pct", 50) / 100,
                    'forest': feat.get("forest_cover_pct", 20) / 100,
                    'water': feat.get("water_bodies", 3) / 50,
                    'barren': 0.05
                }
                
                land_type = random.choices(
                    list(land_type_weights.keys()),
                    weights=list(land_type_weights.values())
                )[0]
                
                # NDVI (Normalized Difference Vegetation Index)
                if land_type == 'forest':
                    ndvi = np.random.uniform(0.5, 0.9)
                elif land_type == 'agricultural':
                    ndvi = np.random.uniform(0.3, 0.7)
                elif land_type == 'urban':
                    ndvi = np.random.uniform(-0.1, 0.3)
                elif land_type == 'water':
                    ndvi = np.random.uniform(-0.5, 0.1)
                else:
                    ndvi = np.random.uniform(-0.2, 0.2)
                    
                # NDBI (Normalized Difference Built-up Index)
                if land_type == 'urban':
                    ndbi = np.random.uniform(-0.1, 0.5)
                else:
                    ndbi = np.random.uniform(-0.5, -0.1)
                    
                # NDWI (Normalized Difference Water Index)
                if land_type == 'water':
                    ndwi = np.random.uniform(0.3, 0.8)
                else:
                    ndwi = np.random.uniform(-0.5, 0.2)
                    
                # Surface temperature (Celsius)
                if land_type == 'urban':
                    surface_temp = np.random.uniform(32, 45)  # Urban heat island
                elif land_type == 'forest':
                    surface_temp = np.random.uniform(22, 30)
                elif land_type == 'water':
                    surface_temp = np.random.uniform(24, 32)
                else:
                    surface_temp = np.random.uniform(28, 38)
                    
                # Elevation (meters)
                if "Hilly" in feat.get("land_type", "") or "Mountain" in feat.get("land_type", ""):
                    elevation = np.random.uniform(200, 1200)
                elif "Coastal" in feat.get("land_type", ""):
                    elevation = np.random.uniform(0, 100)
                else:
                    elevation = np.random.uniform(100, 600)
                    
                # Slope (degrees)
                if "Hilly" in feat.get("land_type", "") or "Mountain" in feat.get("land_type", ""):
                    slope = np.random.uniform(5, 35)
                else:
                    slope = np.random.uniform(0, 10)
                    
                # Texture features from satellite imagery
                texture_contrast = np.random.uniform(0.1, 0.9)
                texture_homogeneity = np.random.uniform(0.2, 0.8)
                
                data.append({
                    'district': district,
                    'lat': feat.get("lat", 19.0) + np.random.uniform(-0.5, 0.5),
                    'lon': feat.get("lon", 75.0) + np.random.uniform(-0.5, 0.5),
                    'ndvi': round(ndvi, 3),
                    'ndbi': round(ndbi, 3),
                    'ndwi': round(ndwi, 3),
                    'surface_temp_c': round(surface_temp, 2),
                    'elevation_m': round(elevation, 2),
                    'slope_degrees': round(slope, 2),
                    'texture_contrast': round(texture_contrast, 3),
                    'texture_homogeneity': round(texture_homogeneity, 3),
                    'land_type': land_type,
                    'year': random.randint(self.start_year, self.end_year)
                })
                
        return pd.DataFrame(data)
    
    def generate_climate_projections(self, years_ahead=10):
        """Generate climate projections for future predictions"""
        data = []
        future_years = list(range(2024, 2024 + years_ahead))
        
        for district in self.districts:
            feat = self.features.get(district, {})
            base_rainfall = feat.get("avg_rainfall", 800)
            
            for i, year in enumerate(future_years):
                # Climate change projections
                rainfall_change = np.random.normal(-5 * i, 50)  # Declining trend with variability
                temp_increase = 0.15 * i + np.random.normal(0, 0.2)
                extreme_events = max(0, int(i * 0.5 + np.random.poisson(1)))
                
                data.append({
                    'district': district,
                    'year': year,
                    'projected_rainfall_mm': round(base_rainfall + rainfall_change, 2),
                    'projected_temp_anomaly_c': round(temp_increase, 2),
                    'extreme_weather_events': extreme_events,
                    'drought_risk_score': min(100, max(0, 30 + i * 3 + np.random.normal(0, 5))),
                    'flood_risk_score': min(100, max(0, 40 + i * 2 + np.random.normal(0, 5)))
                })
                
        return pd.DataFrame(data)
    
    def save_data(self, output_dir='./datasets'):
        """Save all generated datasets"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        hist_df = self.generate_historical_data()
        sat_df = self.generate_satellite_features()
        climate_df = self.generate_climate_projections()
        
        hist_df.to_csv(f'{output_dir}/historical_land_use.csv', index=False)
        sat_df.to_csv(f'{output_dir}/satellite_features.csv', index=False)
        climate_df.to_csv(f'{output_dir}/climate_projections.csv', index=False)
        
        print(f"Data saved to {output_dir}/")
        return hist_df, sat_df, climate_df


if __name__ == "__main__":
    generator = MaharashtraDataGenerator()
    generator.save_data()
