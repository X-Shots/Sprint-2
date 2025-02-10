population_data = {
    "China": 1425893465,
    "India": 1417173173,
    "United States": 338289857,
    "Indonesia": 277534122,
    "Pakistan": 240485658,
    "Nigeria": 236747130,
    "Brazil": 220051512,
    "Bangladesh": 168697184,
    "Russia": 140820810,
    "Mexico": 127504125,
    "Japan": 123294513,
    "Ethiopia": 126527060,
    "Philippines": 116894484,
    "Egypt": 111684559,
    "Vietnam": 98168833,
    "DR Congo": 102262808,
    "Turkey": 87476197,
    "Iran": 89172767,
    "Germany": 81770900,
    "Thailand": 71697030,
    "United Kingdom": 67026292,
    "France": 64805274,
    "Italy": 58870762,
    "South Africa": 60414495,
    "Tanzania": 67438000,
    "Myanmar": 51300000,
    "South Korea": 51439038,
    "Colombia": 52796842,
    "Kenya": 55100000,
    "Spain": 47163418,
    "Argentina": 46044703,
    "Algeria": 46164222,
    "Sudan": 45600000,
    "Ukraine": 36744634,
    "Uganda": 48582334,
    "Iraq": 44000000,
    "Poland": 37627000,
    "Canada": 39293000,
    "Morocco": 37123000,
    "Saudi Arabia": 36023000,
    "Uzbekistan": 36024000,
    "Peru": 34049588,
    "Angola": 35588987,
    "Malaysia": 33573874,
    "Ghana": 34121000,
    "Mozambique": 33089461,
    "Yemen": 33000000,
    "Nepal": 30034989,
    "Venezuela": 28199867,
    "Madagascar": 30000000,
    "Cameroon": 29000000,
    "Côte d'Ivoire": 28713000,
    "North Korea": 25971909,
    "Australia": 26000000,
    "Niger": 27202843,
    "Sri Lanka": 21411000,
    "Burkina Faso": 23000000,
    "Mali": 22000000,
    "Romania": 18500000,
    "Malawi": 20000000,
    "Chile": 19250195,
    "Kazakhstan": 19000000,
    "Zambia": 19000000,
    "Guatemala": 19000000,
    "Ecuador": 18000000,
    "Syria": 17500657,
    "Netherlands": 17800000,
    "Senegal": 17000000,
    "Cambodia": 16000000,
    "Chad": 17000000,
    "Somalia": 17000000,
    "Zimbabwe": 16000000,
    "Guinea": 14000000,
    "Rwanda": 13000000,
    "Benin": 13000000,
    "Burundi": 13000000,
    "Tunisia": 12000000,
    "Bolivia": 12000000,
    "Belgium": 11700000,
    "Haiti": 11000000,
    "Cuba": 11000000,
    "South Sudan": 11000000,
    "Dominican Republic": 11000000,
    "Czech Republic": 10700000,
    "Greece": 10500000,
    "Jordan": 10500000,
    "Portugal": 10300000,
    "Azerbaijan": 10000000,
    "Sweden": 10500000,
    "Honduras": 10000000,
    "United Arab Emirates": 9500000,
    "Hungary": 9600000,
    "Tajikistan": 10000000,
    "Belarus": 9200000,
    "Austria": 9000000,
    "Papua New Guinea": 9000000,
    "Serbia": 6600000,
    "Israel": 9000000,
    "Switzerland": 8800000,
    "Togo": 8000000,
    "Sierra Leone": 8000000,
    "Hong Kong": 7500000,
    "Laos": 7500000,
    "Paraguay": 7000000,
    "Bulgaria": 6500000,
    "Libya": 7000000,
    "Lebanon": 5500000,
    "Nicaragua": 6800000,
    "Kyrgyzstan": 6500000,
    "El Salvador": 6500000,
    "Turkmenistan": 6000000,
    "Singapore": 5500000,
    "Denmark": 5800000,
    "Finland": 5500000,
    "Congo": 5500000,
    "Slovakia": 5400000,
    "Norway": 5500000,
    "Oman": 5000000,
    "State of Palestine": 5000000,
    "Costa Rica": 5000000,
    "Liberia": 5000000,
    "Ireland": 5000000,
    "Central African Republic": 5000000,
    "New Zealand": 5000000,
    "Mauritania": 4500000
}

def fetch_crash_data(conn, category):
    query = f"""
    SELECT {category}, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY {category}
    ORDER BY {category}
    """
    df = pd.read_sql_query(query, conn)

    # Add crashes per capita using the population data
    if category == 'crash_region':  # Example for region-based data
        df['crashes_per_capita'] = df[category].map(population_data).apply(
            lambda pop: df['crash_count'] / pop if pop else None
        )
    else:
        print("Per capita calculation only applies to regions with population data.")
    return df

def fetch_crash_data_with_population(conn, category, population_file='population_data.csv'):
    query = f"""
    SELECT {category}, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY {category}
    ORDER BY {category}
    """
    df = pd.read_sql_query(query, conn)

    # Load population data
    population_df = pd.read_csv(population_file)

    # Merge crash data with population data
    if category == 'crash_region':  # Adjust based on your category
        df = pd.merge(df, population_df, left_on=category, right_on='region', how='left')
        df['crashes_per_capita'] = df['crash_count'] / df['population']
    else:
        print("Per capita calculation only applies to regions with population data.")
    return df

import requests

def get_population_data(region):
    # Replace with an actual API endpoint
    api_url = f"https://population.api.example.com/get?region={region}"
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json().get('population', None)
    else:
        print(f"Failed to fetch data for {region}")
        return None
    
average_population = 1000000  # Example: replace with your estimate

# Update DataFrame
df['crashes_per_capita'] = df['crash_count'] / average_population


def bar_graph(df, category):
    plt.figure(figsize=(10, 6))
    plt.bar(df[category], df['crashes_per_capita'], color='skyblue')
    plt.title(f'Car Crashes per Capita by {category.replace("_", " ").title()}', fontsize=14)
    plt.xlabel(category.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Crashes per Capita', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()



