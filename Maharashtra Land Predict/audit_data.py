import pandas as pd
import numpy as np
from data.maharashtra_districts import DISTRICTS, DISTRICT_FEATURES
from data.data_generator import MaharashtraDataGenerator

def audit_districts_list():
    print("--- Auditing Districts List ---")
    districts_in_list = set(DISTRICTS)
    districts_in_features = set(DISTRICT_FEATURES.keys())

    missing_in_features = districts_in_list - districts_in_features
    missing_in_list = districts_in_features - districts_in_list

    print(f"Total districts in list: {len(districts_in_list)}")
    print(f"Total districts in features: {len(districts_in_features)}")

    if missing_in_features:
        print(f"Missing in DISTRICT_FEATURES: {missing_in_features}")
    if missing_in_list:
        print(f"Missing in DISTRICTS list: {missing_in_list}")

    if not missing_in_features and not missing_in_list:
        print("Districts list and features are consistent.")

def audit_generated_data():
    print("\n--- Auditing Generated Historical Data ---")
    generator = MaharashtraDataGenerator()
    df = generator.generate_historical_data()

    # 1. Check for missing values
    if df.isnull().values.any():
        print("WARNING: Null values found in generated data!")
        print(df.isnull().sum())
    else:
        print("No null values found.")

    # 2. Check land use percentages
    df['total_pct'] = df['urban_pct'] + df['agricultural_pct'] + df['forest_pct'] + df['other_land_pct']
    outliers_pct = df[(df['total_pct'] < 99) | (df['total_pct'] > 101)]
    if not outliers_pct.empty:
        print(f"WARNING: Found {len(outliers_pct)} rows where land percentages don't sum to ~100%")
        # print(outliers_pct[['district', 'year', 'total_pct']])
    else:
        print("Land use percentages sum correctly (~100%).")

    # 3. Check for negative values where they shouldn't be
    cols_to_check = ['urban_pct', 'agricultural_pct', 'forest_pct', 'other_land_pct',
                     'land_price_rs_per_sqft']

    for col in cols_to_check:
        if col not in df.columns:
            continue
        negatives = df[df[col] < 0]
        if not negatives.empty:
            print(f"WARNING: Found negative values in column {col} for districts: {negatives['district'].unique()}")
        else:
            print(f"Column {col} has no negative values.")

    # 4. Check for price outliers (e.g. price < 100 or price > 100,000)
    price_outliers = df[(df['land_price_rs_per_sqft'] < 100) | (df['land_price_rs_per_sqft'] > 100000)]
    if not price_outliers.empty:
        print(f"WARNING: Found price outliers in {len(price_outliers)} rows.")
        print(price_outliers[['district', 'year', 'land_price_rs_per_sqft']])
    else:
        print("Land prices are within expected ranges.")

    # 5. Statistical summary for consistency
    print("\n--- Statistical Summary (Last Year 2023) ---")
    last_year = df[df['year'] == 2023]
    summary = last_year[['land_price_rs_per_sqft']].describe()
    print(summary)

if __name__ == "__main__":
    audit_districts_list()
    audit_generated_data()
