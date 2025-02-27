import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres.jlgwwoyuovqvwprprwkj",      
        password="M5KNIDhJ6EP4bs3",     
        host="aws-0-us-west-1.pooler.supabase.com",           
        port="6543"                   
    )

# Function to fetch crash data by a given category (crash_year or crash_country)
def fetch_crash_data(conn, category):
    if category not in ['crash_country','crash_year','crash_month','week_day','crash_time','crash_setting','road_type','weather_condition','vision_level','cars_involved','speed_limit','driver_age','driver_gender','alcohol_level','driver_fatigue','car_condition','pedestrians_involved','cyclists_involved','crash_severity','injury_amount','fatality_amount','emergency_responce_time','traffic_volume','road_condition','crash_cause','insurance_claim','medical_cost','economic_loss','crash_region','population_density']:
        print("Invalid category. Please choose one of the options. Make sure to spell correctly.")
        return None


 # Fetch year data from database
    query = f"""
    SELECT {category}, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY {category}
    ORDER BY {category}
    """

     # Using pandas to fetch data
    df = pd.read_sql_query(query, conn)
    return df
  


# Plot line graph
def line_graph(df, category):
    plt.figure(figsize=(10, 6))
    plt.plot(df[category], df['crash_count'], marker='o', linestyle='-', color='b')
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.xlabel(category.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.grid(True)
    plt.show()
    
def bar_graph(df, category):
    plt.figure(figsize=(10, 6))
    plt.bar(df[category], df['crash_count'], color='skyblue')
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.xlabel(category.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    
    # Manually adjust the Y-axis to avoid starting from 0
    plt.ylim(bottom=min(df['crash_count']), top=max(df['crash_count']) * 1.1)  # Adjust top to make it visually appealing
    
    plt.tight_layout()  
    plt.show()

# Plot pie chart
def pie_chart(df, category):        
    plt.figure(figsize=(8, 8))
    plt.pie(df['crash_count'], labels=df[category], autopct='%1.1f%%', startangle=140)
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.axis('equal')  
    plt.show()  


def scatter_plot(df, category):
    plt.figure(figsize=(12, 6))
    plt.scatter(df[category], df['crash_count'])
    plt.xlabel(category.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.show()

   

def main():
    conn = connect_to_db()

    #menu
    while True:
       
        
        type_of_graph = input("\nWhat type of graph do you want to plot? (line, bar, pie, scatter): ").strip().lower()
        category = input("\nWhich data do you want to analyze:\n"
                 "crash_country\ncrash_year\ncrash_month\nweek_day\n"
                 "crash_time\ncrash_setting\nroad_type\nweather_condition\n"
                 "vision_level\ncars_involved\nspeed_limit\ndriver_age\n"
                 "driver_gender\nalcohol_level\ndriver_fatigue\ncar_condition\n"
                 "pedestrians_involved\ncyclists_involved\ncrash_severity\n"
                 "injury_amount\nfatality_amount\nemergency_response_time\n"
                 "traffic_volume\nroad_condition\ncrash_cause\ninsurance_claim\n"
                 "medical_cost\neconomic_loss\ncrash_region\npopulation_density\n"
                 "Type Category here: ").strip().lower()
        crash_data = fetch_crash_data(conn, category)
        if type_of_graph == "line":
            line_graph(crash_data, category)
        elif type_of_graph == "bar":
            bar_graph(crash_data, category)
        elif type_of_graph == "pie":
            pie_chart(crash_data, category)
        elif type_of_graph == "scatter":
            scatter_plot(crash_data, category)
        else:
            print("Invalid choice. Please choose 'line', 'bar', or 'pie'.")

        # Determines if user wants to view 
        print("\nDo you want to analyze another category?")
        choice = input("Enter 'yes' or 'no': ")
        if choice.lower() =='yes':
            True
        else:
            break
    
        
        
    

if __name__ == '__main__':

    main()
