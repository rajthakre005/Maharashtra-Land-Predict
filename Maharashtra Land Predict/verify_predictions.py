import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_land_use(district):
    print(f"\n--- Testing Land Use Predictions for {district} ---")
    response = requests.get(f"{BASE_URL}/api/predict/land-use/{district}?years=5")
    if response.status_code == 200:
        data = response.json()
        print(f"District: {data['district']}")
        for pred in data['predictions']:
            print(f"Year {pred['year']}: Plots={pred['plots_for_sale']}, Houses={pred['houses_for_sale']}, Rentals={pred['rentals_available']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def test_land_price(district):
    print(f"\n--- Testing Land Price Predictions for {district} ---")
    response = requests.get(f"{BASE_URL}/api/predict/land-price/{district}?years=5")
    if response.status_code == 200:
        data = response.json()
        print(f"District: {data['district']}")
        for pred in data['predictions']:
            print(f"Year {pred['year']}: Land Price={pred['predicted_price_rs_per_sqft']}, Plot Price={pred['predicted_plot_price']}, House Price={pred['predicted_house_price']}, Rental={pred['predicted_rental_price']}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

if __name__ == "__main__":
    test_land_use("Pune")
    test_land_price("Pune")
    test_land_use("Mumbai")
    test_land_price("Mumbai")
    test_land_use("Nagpur")
    test_land_price("Nagpur")
