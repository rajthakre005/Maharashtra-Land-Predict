"""
Maharashtra Talukas (Tehsils) Data Module
Contains talukas with geographic data and land pricing
"""

# Thane/Palghar District Talukas
THANE_TALUKAS = [
    {"name": "Thane", "lat": 19.2183, "lon": 72.9781, "base_price": 18000, "zone": "urban", "infra_score": 95},
    {"name": "Kalyan", "lat": 19.2416, "lon": 73.1203, "base_price": 15000, "zone": "urban", "infra_score": 90},
    {"name": "Dombivli", "lat": 19.2184, "lon": 73.0868, "base_price": 14000, "zone": "urban", "infra_score": 88},
    {"name": "Ulhasnagar", "lat": 19.2215, "lon": 73.1645, "base_price": 12000, "zone": "urban", "infra_score": 85},
    {"name": "Bhiwandi", "lat": 19.3002, "lon": 73.0580, "base_price": 10000, "zone": "industrial", "infra_score": 80},
    {"name": "Vasai", "lat": 19.3919, "lon": 72.8314, "base_price": 16000, "zone": "urban", "infra_score": 92},
    {"name": "Virar", "lat": 19.4700, "lon": 72.8000, "base_price": 14000, "zone": "urban", "infra_score": 88},
    {"name": "Palghar", "lat": 19.6942, "lon": 72.7659, "base_price": 8000, "zone": "semi_urban", "infra_score": 75},
    {"name": "Dahanu", "lat": 19.9833, "lon": 72.7333, "base_price": 5000, "zone": "coastal", "infra_score": 58},
    {"name": "Talasari", "lat": 20.0833, "lon": 72.8500, "base_price": 4000, "zone": "rural", "infra_score": 50},
    {"name": "Wada", "lat": 19.6500, "lon": 73.1500, "base_price": 4500, "zone": "rural", "infra_score": 55},
    {"name": "Murbad", "lat": 19.3667, "lon": 73.4000, "base_price": 5500, "zone": "rural", "infra_score": 60},
    {"name": "Shahapur", "lat": 19.4500, "lon": 73.3300, "base_price": 6000, "zone": "rural", "infra_score": 65},
    {"name": "Jawhar", "lat": 19.9167, "lon": 73.2333, "base_price": 3500, "zone": "hilly", "infra_score": 48},
    {"name": "Mokhada", "lat": 19.9333, "lon": 73.3167, "base_price": 3000, "zone": "tribal", "infra_score": 42},
    {"name": "Vikramgad", "lat": 19.7833, "lon": 73.1000, "base_price": 4000, "zone": "rural", "infra_score": 52},
]

# Mumbai Areas
MUMBAI_AREAS = [
    {"name": "South Mumbai", "lat": 18.9667, "lon": 72.8333, "base_price": 80000, "zone": "prime_urban", "infra_score": 100},
    {"name": "Bandra", "lat": 19.0544, "lon": 72.8403, "base_price": 65000, "zone": "prime_urban", "infra_score": 98},
    {"name": "Andheri", "lat": 19.1136, "lon": 72.8697, "base_price": 55000, "zone": "prime_urban", "infra_score": 95},
    {"name": "Borivali", "lat": 19.2307, "lon": 72.8567, "base_price": 45000, "zone": "urban", "infra_score": 92},
    {"name": "Mulund", "lat": 19.1725, "lon": 72.9425, "base_price": 48000, "zone": "urban", "infra_score": 93},
    {"name": "Dadar", "lat": 19.0183, "lon": 72.8439, "base_price": 60000, "zone": "prime_urban", "infra_score": 96},
    {"name": "Worli", "lat": 19.0167, "lon": 72.8333, "base_price": 70000, "zone": "prime_urban", "infra_score": 98},
    {"name": "Juhu", "lat": 19.1000, "lon": 72.8333, "base_price": 60000, "zone": "prime_urban", "infra_score": 97},
    {"name": "Goregaon", "lat": 19.1645, "lon": 72.8490, "base_price": 42000, "zone": "urban", "infra_score": 90},
    {"name": "Malad", "lat": 19.1868, "lon": 72.8485, "base_price": 38000, "zone": "urban", "infra_score": 88},
    {"name": "Kandivali", "lat": 19.2000, "lon": 72.8500, "base_price": 40000, "zone": "urban", "infra_score": 89},
    {"name": "Chembur", "lat": 19.0582, "lon": 72.9005, "base_price": 45000, "zone": "urban", "infra_score": 91},
    {"name": "Ghatkopar", "lat": 19.0850, "lon": 72.9100, "base_price": 40000, "zone": "urban", "infra_score": 88},
    {"name": "Powai", "lat": 19.1200, "lon": 72.9100, "base_price": 50000, "zone": "prime_urban", "infra_score": 94},
    {"name": "Vikhroli", "lat": 19.1100, "lon": 72.9400, "base_price": 35000, "zone": "urban", "infra_score": 85},
]

# Navi Mumbai Talukas
NAVI_MUMBAI_TALUKAS = [
    {"name": "Vashi", "lat": 19.0330, "lon": 73.0297, "base_price": 25000, "zone": "urban", "infra_score": 90},
    {"name": "Nerul", "lat": 19.0333, "lon": 73.0167, "base_price": 22000, "zone": "urban", "infra_score": 88},
    {"name": "Belapur", "lat": 19.0167, "lon": 73.0400, "base_price": 20000, "zone": "urban", "infra_score": 85},
    {"name": "Panvel", "lat": 18.9893, "lon": 73.1198, "base_price": 18000, "zone": "semi_urban", "infra_score": 82},
    {"name": "Kharghar", "lat": 19.0400, "lon": 73.0600, "base_price": 24000, "zone": "urban", "infra_score": 89},
    {"name": "Kamothe", "lat": 19.0167, "lon": 73.0833, "base_price": 19000, "zone": "semi_urban", "infra_score": 84},
    {"name": "Kalamboli", "lat": 19.0333, "lon": 73.1167, "base_price": 16000, "zone": "semi_urban", "infra_score": 80},
    {"name": "Taloja", "lat": 19.0833, "lon": 73.0833, "base_price": 15000, "zone": "industrial", "infra_score": 78},
    {"name": "New Panvel", "lat": 18.9833, "lon": 73.1000, "base_price": 17000, "zone": "semi_urban", "infra_score": 81},
    {"name": "Uran", "lat": 18.8000, "lon": 72.9500, "base_price": 12000, "zone": "coastal", "infra_score": 75},
    {"name": "Karjat", "lat": 18.9100, "lon": 73.3300, "base_price": 10000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Khalapur", "lat": 18.8333, "lon": 73.3000, "base_price": 9000, "zone": "rural", "infra_score": 68},
]

# Pune District Talukas (15 talukas)
PUNE_TALUKAS = [
    {"name": "Pune City", "lat": 18.5204, "lon": 73.8567, "base_price": 20000, "zone": "prime_urban", "infra_score": 95},
    {"name": "Koregaon Park", "lat": 18.5362, "lon": 73.8930, "base_price": 28000, "zone": "prime_urban", "infra_score": 96},
    {"name": "Kothrud", "lat": 18.5074, "lon": 73.8077, "base_price": 22000, "zone": "prime_urban", "infra_score": 93},
    {"name": "Baner", "lat": 18.5636, "lon": 73.8116, "base_price": 21000, "zone": "prime_urban", "infra_score": 94},
    {"name": "Aundh", "lat": 18.5580, "lon": 73.8070, "base_price": 20000, "zone": "prime_urban", "infra_score": 93},
    {"name": "Viman Nagar", "lat": 18.5670, "lon": 73.9150, "base_price": 23000, "zone": "prime_urban", "infra_score": 95},
    {"name": "Pimpri-Chinchwad", "lat": 18.6279, "lon": 73.8009, "base_price": 16000, "zone": "urban", "infra_score": 90},
    {"name": "Hinjewadi", "lat": 18.5971, "lon": 73.7180, "base_price": 18000, "zone": "it_corridor", "infra_score": 88},
    {"name": "Wakad", "lat": 18.6238, "lon": 73.7500, "base_price": 17000, "zone": "urban", "infra_score": 87},
    {"name": "Kharadi", "lat": 18.5500, "lon": 73.9500, "base_price": 19000, "zone": "urban", "infra_score": 89},
    {"name": "Hadapsar", "lat": 18.5089, "lon": 73.9250, "base_price": 17000, "zone": "urban", "infra_score": 88},
    {"name": "Bavdhan", "lat": 18.5200, "lon": 73.7800, "base_price": 18000, "zone": "urban", "infra_score": 89},
    {"name": "Kondhwa", "lat": 18.4800, "lon": 73.8900, "base_price": 15000, "zone": "semi_urban", "infra_score": 85},
    {"name": "Warje", "lat": 18.5000, "lon": 73.8000, "base_price": 16000, "zone": "semi_urban", "infra_score": 86},
    {"name": "Kothrud-Bavdhan", "lat": 18.5100, "lon": 73.7800, "base_price": 17000, "zone": "semi_urban", "infra_score": 87},
    {"name": "Pashan", "lat": 18.5400, "lon": 73.7900, "base_price": 17000, "zone": "urban", "infra_score": 88},
    {"name": "Maval", "lat": 18.6700, "lon": 73.5200, "base_price": 12000, "zone": "semi_urban", "infra_score": 78},
    {"name": "Mulshi", "lat": 18.5400, "lon": 73.4700, "base_price": 8000, "zone": "hilly", "infra_score": 70},
    {"name": "Khed", "lat": 19.0300, "lon": 73.8800, "base_price": 10000, "zone": "rural", "infra_score": 72},
    {"name": "Shirur", "lat": 18.8300, "lon": 74.3800, "base_price": 9000, "zone": "rural", "infra_score": 70},
    {"name": "Daund", "lat": 18.4600, "lon": 74.5800, "base_price": 8500, "zone": "semi_urban", "infra_score": 68},
    {"name": "Indapur", "lat": 18.3000, "lon": 75.0300, "base_price": 7500, "zone": "rural", "infra_score": 65},
    {"name": "Baramati", "lat": 18.1800, "lon": 74.5800, "base_price": 11000, "zone": "agricultural", "infra_score": 75},
    {"name": "Bhor", "lat": 18.1500, "lon": 73.8500, "base_price": 7000, "zone": "rural", "infra_score": 65},
    {"name": "Velhe", "lat": 18.4100, "lon": 73.6500, "base_price": 6000, "zone": "rural", "infra_score": 60},
    {"name": "Junnar", "lat": 19.2000, "lon": 73.8800, "base_price": 8000, "zone": "rural", "infra_score": 68},
    {"name": "Ambegaon", "lat": 19.1800, "lon": 73.7500, "base_price": 7500, "zone": "rural", "infra_score": 65},
    {"name": "Purandar", "lat": 18.2800, "lon": 74.1500, "base_price": 7000, "zone": "hilly", "infra_score": 62},
]

# Nashik District Talukas (15 talukas)
NASHIK_TALUKAS = [
    {"name": "Nashik City", "lat": 19.9975, "lon": 73.7898, "base_price": 12000, "zone": "urban", "infra_score": 90},
    {"name": "Nashik Road", "lat": 19.9500, "lon": 73.8500, "base_price": 10000, "zone": "semi_urban", "infra_score": 85},
    {"name": "Deolali", "lat": 19.9500, "lon": 73.8333, "base_price": 9500, "zone": "semi_urban", "infra_score": 83},
    {"name": "Malegaon", "lat": 20.5500, "lon": 74.5300, "base_price": 9000, "zone": "urban", "infra_score": 82},
    {"name": "Sinnar", "lat": 19.8500, "lon": 74.0000, "base_price": 8500, "zone": "industrial", "infra_score": 80},
    {"name": "Igatpuri", "lat": 19.7000, "lon": 73.5600, "base_price": 7000, "zone": "hilly", "infra_score": 75},
    {"name": "Trimbakeshwar", "lat": 19.9333, "lon": 73.5333, "base_price": 8000, "zone": "religious", "infra_score": 78},
    {"name": "Niphad", "lat": 20.0800, "lon": 74.1100, "base_price": 7500, "zone": "agricultural", "infra_score": 72},
    {"name": "Dindori", "lat": 20.2000, "lon": 73.8300, "base_price": 6500, "zone": "rural", "infra_score": 68},
    {"name": "Baglan", "lat": 20.6800, "lon": 74.0800, "base_price": 5500, "zone": "rural", "infra_score": 62},
    {"name": "Chandwad", "lat": 20.3300, "lon": 74.2500, "base_price": 6000, "zone": "rural", "infra_score": 65},
    {"name": "Kalwan", "lat": 20.4800, "lon": 74.0200, "base_price": 5500, "zone": "rural", "infra_score": 60},
    {"name": "Surgana", "lat": 20.5800, "lon": 73.7500, "base_price": 5000, "zone": "tribal", "infra_score": 55},
    {"name": "Peint", "lat": 20.2500, "lon": 73.6300, "base_price": 5000, "zone": "tribal", "infra_score": 52},
    {"name": "Yeola", "lat": 20.0400, "lon": 74.4900, "base_price": 7000, "zone": "semi_urban", "infra_score": 70},
]

# Nagpur District Talukas (14 talukas)
NAGPUR_TALUKAS = [
    {"name": "Nagpur City", "lat": 21.1458, "lon": 79.0882, "base_price": 10000, "zone": "urban", "infra_score": 90},
    {"name": "Nagpur Rural", "lat": 21.2000, "lon": 79.1500, "base_price": 7000, "zone": "semi_urban", "infra_score": 78},
    {"name": "Kamptee", "lat": 21.2200, "lon": 79.2000, "base_price": 7500, "zone": "semi_urban", "infra_score": 80},
    {"name": "Hingna", "lat": 21.0833, "lon": 78.9833, "base_price": 8000, "zone": "industrial", "infra_score": 82},
    {"name": "Umred", "lat": 20.8700, "lon": 79.3300, "base_price": 6500, "zone": "semi_urban", "infra_score": 72},
    {"name": "Ramtek", "lat": 21.4000, "lon": 79.3300, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Savner", "lat": 21.3800, "lon": 78.9200, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Kuhi", "lat": 21.0200, "lon": 79.2000, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Mouda", "lat": 21.0700, "lon": 79.2700, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Kalmeshwar", "lat": 21.2333, "lon": 78.9000, "base_price": 5800, "zone": "rural", "infra_score": 66},
    {"name": "Parseoni", "lat": 21.3700, "lon": 79.0500, "base_price": 5200, "zone": "rural", "infra_score": 63},
    {"name": "Bhiwapur", "lat": 20.7800, "lon": 79.5200, "base_price": 4800, "zone": "rural", "infra_score": 60},
    {"name": "Katol", "lat": 21.2800, "lon": 78.5800, "base_price": 6500, "zone": "semi_urban", "infra_score": 72},
    {"name": "Narkhed", "lat": 21.4700, "lon": 78.5200, "base_price": 6000, "zone": "rural", "infra_score": 68},
]

# Aurangabad District Talukas (9 talukas)
AURANGABAD_TALUKAS = [
    {"name": "Aurangabad City", "lat": 19.8762, "lon": 75.3433, "base_price": 11000, "zone": "urban", "infra_score": 88},
    {"name": "Paithan", "lat": 19.4800, "lon": 75.3800, "base_price": 7500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Kannad", "lat": 20.2700, "lon": 75.1300, "base_price": 6500, "zone": "rural", "infra_score": 70},
    {"name": "Gangapur", "lat": 19.7000, "lon": 75.0000, "base_price": 7000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Khultabad", "lat": 20.0000, "lon": 75.4000, "base_price": 6000, "zone": "rural", "infra_score": 68},
    {"name": "Sillod", "lat": 20.3000, "lon": 75.6500, "base_price": 6800, "zone": "semi_urban", "infra_score": 70},
    {"name": "Vaijapur", "lat": 19.9300, "lon": 74.7300, "base_price": 6200, "zone": "semi_urban", "infra_score": 68},
    {"name": "Phulambri", "lat": 19.5700, "lon": 75.2800, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Soyegaon", "lat": 20.5700, "lon": 74.7000, "base_price": 5000, "zone": "rural", "infra_score": 62},
]

# Solapur District Talukas (11 talukas)
SOLAPUR_TALUKAS = [
    {"name": "Solapur City", "lat": 17.6599, "lon": 75.9064, "base_price": 8000, "zone": "urban", "infra_score": 85},
    {"name": "North Solapur", "lat": 17.6800, "lon": 75.9200, "base_price": 7500, "zone": "semi_urban", "infra_score": 80},
    {"name": "South Solapur", "lat": 17.6400, "lon": 75.8900, "base_price": 7200, "zone": "semi_urban", "infra_score": 78},
    {"name": "Barshi", "lat": 18.2300, "lon": 75.7000, "base_price": 6500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Pandharpur", "lat": 17.6800, "lon": 75.3300, "base_price": 7000, "zone": "religious", "infra_score": 75},
    {"name": "Sangola", "lat": 17.4400, "lon": 75.2000, "base_price": 5800, "zone": "rural", "infra_score": 68},
    {"name": "Malshiras", "lat": 17.3200, "lon": 75.1700, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Madha", "lat": 18.0700, "lon": 75.5500, "base_price": 6000, "zone": "rural", "infra_score": 68},
    {"name": "Karmala", "lat": 18.4000, "lon": 75.2000, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Akkalkot", "lat": 17.5200, "lon": 76.2000, "base_price": 6500, "zone": "religious", "infra_score": 72},
    {"name": "Mohol", "lat": 17.8000, "lon": 75.6500, "base_price": 5800, "zone": "rural", "infra_score": 68},
    {"name": "Mangalwedha", "lat": 17.5000, "lon": 75.5000, "base_price": 6000, "zone": "rural", "infra_score": 70},
]

# Amravati District Talukas (14 talukas)
AMRAVATI_TALUKAS = [
    {"name": "Amravati City", "lat": 20.9374, "lon": 77.7796, "base_price": 8500, "zone": "urban", "infra_score": 85},
    {"name": "Badnera", "lat": 20.8533, "lon": 77.7333, "base_price": 7500, "zone": "semi_urban", "infra_score": 80},
    {"name": "Achalpur", "lat": 21.2572, "lon": 77.5086, "base_price": 6500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Morshi", "lat": 21.3300, "lon": 78.0200, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Warud", "lat": 21.4700, "lon": 78.2700, "base_price": 5800, "zone": "rural", "infra_score": 68},
    {"name": "Daryapur", "lat": 20.9300, "lon": 77.3300, "base_price": 6200, "zone": "rural", "infra_score": 72},
    {"name": "Anjangaon", "lat": 21.1600, "lon": 77.3100, "base_price": 6000, "zone": "semi_urban", "infra_score": 70},
    {"name": "Chandur", "lat": 20.8200, "lon": 77.9800, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Dhamangaon", "lat": 20.7800, "lon": 77.5500, "base_price": 5800, "zone": "rural", "infra_score": 68},
    {"name": "Tiosa", "lat": 20.9100, "lon": 77.5200, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Nandgaon", "lat": 21.2700, "lon": 77.2000, "base_price": 5200, "zone": "rural", "infra_score": 62},
    {"name": "Chikhaldara", "lat": 21.2100, "lon": 77.3300, "base_price": 7000, "zone": "hill_station", "infra_score": 75},
    {"name": "Bhatkuli", "lat": 20.9500, "lon": 77.7000, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Dharani", "lat": 21.1800, "lon": 77.6200, "base_price": 4800, "zone": "rural", "infra_score": 60},
]

# Kolhapur District Talukas
KOLHAPUR_TALUKAS = [
    {"name": "Karvir", "lat": 16.7000, "lon": 74.2200, "base_price": 12000, "zone": "urban", "infra_score": 88},
    {"name": "Shirol", "lat": 16.7300, "lon": 74.4300, "base_price": 9000, "zone": "industrial", "infra_score": 82},
    {"name": "Hatkanangle", "lat": 16.6000, "lon": 74.4500, "base_price": 8500, "zone": "semi_urban", "infra_score": 80},
    {"name": "Kagal", "lat": 16.5800, "lon": 74.3000, "base_price": 9000, "zone": "industrial", "infra_score": 82},
    {"name": "Panhala", "lat": 16.8200, "lon": 74.1100, "base_price": 10000, "zone": "hill_fort", "infra_score": 85},
    {"name": "Gadhinglaj", "lat": 16.2300, "lon": 74.3500, "base_price": 8000, "zone": "urban", "infra_score": 80},
    {"name": "Chandgad", "lat": 15.9700, "lon": 74.1800, "base_price": 6500, "zone": "rural", "infra_score": 72},
    {"name": "Ajra", "lat": 16.1000, "lon": 74.0700, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Bavda", "lat": 16.5700, "lon": 74.1000, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Radhanagari", "lat": 16.4200, "lon": 73.9900, "base_price": 6000, "zone": "rural", "infra_score": 68},
    {"name": "Gaganbawada", "lat": 16.5400, "lon": 73.8400, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Shahuwadi", "lat": 17.0200, "lon": 73.9100, "base_price": 5200, "zone": "rural", "infra_score": 62},
]

# Jalgaon District Talukas
JALGAON_TALUKAS = [
    {"name": "Jalgaon", "lat": 21.0077, "lon": 75.5626, "base_price": 8000, "zone": "urban", "infra_score": 85},
    {"name": "Bhusawal", "lat": 21.0500, "lon": 75.7800, "base_price": 7500, "zone": "industrial", "infra_score": 82},
    {"name": "Chopda", "lat": 21.2500, "lon": 75.3000, "base_price": 6200, "zone": "semi_urban", "infra_score": 75},
    {"name": "Yawal", "lat": 21.1700, "lon": 75.7000, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Raver", "lat": 21.2400, "lon": 76.0400, "base_price": 6500, "zone": "agricultural", "infra_score": 72},
    {"name": "Amalner", "lat": 21.0500, "lon": 75.0600, "base_price": 7000, "zone": "semi_urban", "infra_score": 78},
    {"name": "Erandol", "lat": 20.9200, "lon": 75.3300, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Dharangaon", "lat": 21.0000, "lon": 75.2800, "base_price": 5800, "zone": "rural", "infra_score": 68},
    {"name": "Chalisgaon", "lat": 20.4700, "lon": 75.0200, "base_price": 6500, "zone": "semi_urban", "infra_score": 72},
    {"name": "Pachora", "lat": 20.6700, "lon": 75.3500, "base_price": 6000, "zone": "semi_urban", "infra_score": 70},
    {"name": "Jamner", "lat": 20.8500, "lon": 75.7800, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Bhadgaon", "lat": 20.6700, "lon": 74.9200, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Muktainagar", "lat": 21.0700, "lon": 76.0300, "base_price": 5800, "zone": "rural", "infra_score": 68},
]

# Akola District Talukas
AKOLA_TALUKAS = [
    {"name": "Akola", "lat": 20.7002, "lon": 77.0082, "base_price": 7000, "zone": "urban", "infra_score": 82},
    {"name": "Akot", "lat": 21.1000, "lon": 77.1000, "base_price": 6500, "zone": "semi_urban", "infra_score": 78},
    {"name": "Balapur", "lat": 20.6700, "lon": 76.7700, "base_price": 5800, "zone": "rural", "infra_score": 70},
    {"name": "Barshitakli", "lat": 20.9333, "lon": 77.0333, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Murtijapur", "lat": 20.7300, "lon": 77.3700, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Telhara", "lat": 21.0333, "lon": 76.8333, "base_price": 5500, "zone": "rural", "infra_score": 65},
    {"name": "Patur", "lat": 20.4500, "lon": 76.9500, "base_price": 5200, "zone": "rural", "infra_score": 65},
]

# Latur District Talukas
LATUR_TALUKAS = [
    {"name": "Latur", "lat": 18.4088, "lon": 76.5604, "base_price": 7000, "zone": "urban", "infra_score": 80},
    {"name": "Ahmadpur", "lat": 18.7000, "lon": 76.9300, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Udgir", "lat": 18.3900, "lon": 77.1200, "base_price": 6200, "zone": "semi_urban", "infra_score": 75},
    {"name": "Nilanga", "lat": 18.1200, "lon": 76.7500, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Ausa", "lat": 18.2500, "lon": 76.5000, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Renapur", "lat": 18.5500, "lon": 76.6000, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Chakur", "lat": 18.3500, "lon": 76.6200, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Shirur-Anantpal", "lat": 18.2300, "lon": 76.8500, "base_price": 4800, "zone": "rural", "infra_score": 60},
    {"name": "Devani", "lat": 18.3800, "lon": 76.4200, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Jalkot", "lat": 18.5200, "lon": 77.0800, "base_price": 4800, "zone": "rural", "infra_score": 60},
]

# Nanded District Talukas
NANDED_TALUKAS = [
    {"name": "Nanded", "lat": 19.1383, "lon": 77.3210, "base_price": 8000, "zone": "urban", "infra_score": 85},
    {"name": "Mudkhed", "lat": 19.1600, "lon": 77.9300, "base_price": 6200, "zone": "semi_urban", "infra_score": 75},
    {"name": "Bhokar", "lat": 19.2200, "lon": 77.7000, "base_price": 5800, "zone": "rural", "infra_score": 70},
    {"name": "Degloor", "lat": 18.5500, "lon": 77.5800, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Mukhed", "lat": 18.7000, "lon": 77.3500, "base_price": 5800, "zone": "rural", "infra_score": 70},
    {"name": "Kandhar", "lat": 18.9000, "lon": 77.2000, "base_price": 6000, "zone": "rural", "infra_score": 72},
    {"name": "Loha", "lat": 18.9300, "lon": 76.9000, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Dharmabad", "lat": 18.9000, "lon": 77.8500, "base_price": 6500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Hadgaon", "lat": 19.5000, "lon": 77.6800, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Kinwat", "lat": 19.6500, "lon": 78.2000, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Mahur", "lat": 18.8300, "lon": 77.9300, "base_price": 5000, "zone": "religious", "infra_score": 70},
    {"name": "Biloli", "lat": 18.7800, "lon": 77.7300, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Ardhapur", "lat": 19.2200, "lon": 77.9000, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Himayatnagar", "lat": 19.4300, "lon": 77.3500, "base_price": 5200, "zone": "rural", "infra_score": 65},
]

# Parbhani District Talukas
PARBHANI_TALUKAS = [
    {"name": "Parbhani", "lat": 19.2608, "lon": 76.7767, "base_price": 6500, "zone": "urban", "infra_score": 80},
    {"name": "Gangakhed", "lat": 18.9500, "lon": 76.7500, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Pathri", "lat": 19.2600, "lon": 76.4500, "base_price": 5800, "zone": "semi_urban", "infra_score": 70},
    {"name": "Sonpeth", "lat": 19.1300, "lon": 76.4800, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Palam", "lat": 19.0500, "lon": 76.9300, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Jintur", "lat": 19.6200, "lon": 76.7000, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Manwath", "lat": 19.3000, "lon": 76.5000, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Purna", "lat": 19.1800, "lon": 77.0500, "base_price": 5800, "zone": "rural", "infra_score": 70},
    {"name": "Sailu", "lat": 19.4700, "lon": 76.4300, "base_price": 5200, "zone": "rural", "infra_score": 65},
]

# Ahmednagar District Talukas
AHMEDNAGAR_TALUKAS = [
    {"name": "Ahmednagar", "lat": 19.0948, "lon": 74.7480, "base_price": 7500, "zone": "urban", "infra_score": 82},
    {"name": "Shrirampur", "lat": 19.6200, "lon": 74.6600, "base_price": 6500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Shirdi", "lat": 19.7600, "lon": 74.4800, "base_price": 8000, "zone": "religious", "infra_score": 80},
    {"name": "Rahuri", "lat": 19.3900, "lon": 74.6500, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Kopargaon", "lat": 19.8800, "lon": 74.4800, "base_price": 6200, "zone": "semi_urban", "infra_score": 73},
    {"name": "Sangamner", "lat": 19.5700, "lon": 74.2000, "base_price": 6000, "zone": "semi_urban", "infra_score": 72},
    {"name": "Karjat", "lat": 18.5500, "lon": 74.9600, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Jamkhed", "lat": 18.8800, "lon": 75.3100, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Pathardi", "lat": 19.1700, "lon": 75.1800, "base_price": 5000, "zone": "rural", "infra_score": 62},
    {"name": "Shevgaon", "lat": 19.1500, "lon": 75.2000, "base_price": 4800, "zone": "rural", "infra_score": 60},
    {"name": "Parner", "lat": 19.0000, "lon": 74.4300, "base_price": 5200, "zone": "rural", "infra_score": 65},
    {"name": "Akole", "lat": 19.5300, "lon": 73.9900, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Nevasa", "lat": 19.8900, "lon": 74.9200, "base_price": 5500, "zone": "rural", "infra_score": 68},
]

# Satara District Talukas
SATARA_TALUKAS = [
    {"name": "Satara", "lat": 17.6800, "lon": 74.0203, "base_price": 9000, "zone": "urban", "infra_score": 85},
    {"name": "Karad", "lat": 17.2800, "lon": 74.2000, "base_price": 8000, "zone": "urban", "infra_score": 82},
    {"name": "Mahabaleshwar", "lat": 17.9200, "lon": 73.6500, "base_price": 12000, "zone": "hill_station", "infra_score": 88},
    {"name": "Wai", "lat": 17.9500, "lon": 73.8900, "base_price": 7000, "zone": "semi_urban", "infra_score": 78},
    {"name": "Phaltan", "lat": 17.9900, "lon": 74.4300, "base_price": 6500, "zone": "semi_urban", "infra_score": 75},
    {"name": "Patan", "lat": 17.3800, "lon": 73.9000, "base_price": 6000, "zone": "rural", "infra_score": 70},
    {"name": "Koregaon", "lat": 18.1400, "lon": 74.0000, "base_price": 6200, "zone": "rural", "infra_score": 72},
    {"name": "Jaoli", "lat": 17.7800, "lon": 73.7500, "base_price": 5500, "zone": "hilly", "infra_score": 68},
    {"name": "Khandala", "lat": 18.1100, "lon": 74.2600, "base_price": 6500, "zone": "semi_urban", "infra_score": 74},
    {"name": "Khatav", "lat": 17.7000, "lon": 74.5500, "base_price": 5500, "zone": "rural", "infra_score": 68},
    {"name": "Man", "lat": 17.4100, "lon": 74.5500, "base_price": 5800, "zone": "rural", "infra_score": 70},
]

# All talukas combined
ALL_TALUKAS = {
    "Thane": THANE_TALUKAS,
    "Mumbai": MUMBAI_AREAS,
    "Navi Mumbai": NAVI_MUMBAI_TALUKAS,
    "Pune": PUNE_TALUKAS,
    "Nashik": NASHIK_TALUKAS,
    "Nagpur": NAGPUR_TALUKAS,
    "Aurangabad": AURANGABAD_TALUKAS,
    "Solapur": SOLAPUR_TALUKAS,
    "Amravati": AMRAVATI_TALUKAS,
    "Kolhapur": KOLHAPUR_TALUKAS,
    "Jalgaon": JALGAON_TALUKAS,
    "Akola": AKOLA_TALUKAS,
    "Latur": LATUR_TALUKAS,
    "Nanded": NANDED_TALUKAS,
    "Parbhani": PARBHANI_TALUKAS,
    "Ahmednagar": AHMEDNAGAR_TALUKAS,
    "Satara": SATARA_TALUKAS,
}

def get_all_talukas_flat():
    """Get all talukas as a flat list"""
    flat_list = []
    for district, talukas in ALL_TALUKAS.items():
        for taluka in talukas:
            taluka_copy = taluka.copy()
            taluka_copy['district'] = district
            flat_list.append(taluka_copy)
    return flat_list

def get_taluka_price(taluka_name, year=2024):
    """Calculate taluka land price with appreciation"""
    all_talukas = get_all_talukas_flat()
    for taluka in all_talukas:
        if taluka['name'].lower() == taluka_name.lower():
            base = taluka['base_price']
            # Appreciation based on zone
            rates = {'prime_urban': 0.15, 'urban': 0.12, 'it_corridor': 0.13, 
                    'industrial': 0.10, 'semi_urban': 0.09, 'rural': 0.07,
                    'agricultural': 0.06, 'hilly': 0.05, 'tribal': 0.04,
                    'coastal': 0.08, 'religious': 0.08, 'hill_station': 0.11,
                    'hill_fort': 0.07}
            rate = rates.get(taluka['zone'], 0.08)
            return round(base * ((1 + rate) ** (year - 2023)), 2)
    return None

