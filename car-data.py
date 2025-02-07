import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
# print("please work")

# Connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres",         
        password="l9l9L(L(",     
        host="localhost",           
        port="5432"                   
    )

# Fetch year data from database
def crash_per_year(conn):
    query = """
    SELECT crash_year, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_year
    ORDER BY crash_year
    """
  
    cpr = pd.read_sql_query(query, conn)
    return cpr

# Plot line graph
def line_crash_per_year(cpr):
    plt.figure(figsize=(10, 6))
    plt.plot(cpr['crash_year'], cpr['crash_count'], marker='o', linestyle='-', color='b')
    plt.title('Car Crashes per Year', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.grid(True)
    plt.show()

# Fetch country data from database
def crash_per_country(conn):
    query = """
    SELECT crash_country, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_country
    ORDER BY crash_count DESC
    """
    
    # Use pd.read_sql_query for direct DataFrame creation
    df = pd.read_sql_query(query, conn) 
    return df

# Plot pie chart
def pie_crash_per_country(df):
    plt.figure(figsize=(8, 8))  
    plt.pie(df['crash_count'], labels=df['crash_country'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Car Crashes by Country', fontsize=14)
    plt.axis('equal')  
    plt.show() 

# plot bar graph
def bargraph_crash_per_country(df):
    plt.figure(figsize=(10, 6))
    plt.bar(df['crash_country'], df['crash_count'], color='skyblue')
    plt.title('Car Crashes by Country', fontsize=14)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
    plt.tight_layout()  # Adjust layout to prevent clipping
    plt.show()

def weather_condition(conn):
    query = """
    SELECT weather_condition, count(*) as crash_count
    FROM crash_table
    GROUP BY weather_condition
    ORDER BY crash_count DESC"""
    wc = pd.read_sql_query(query, conn)
    return wc

def pie_weather_condition(wc):
    plt.figure(figsize=(8, 8))  
    plt.pie(wc['crash_count'], labels=wc['weather_condition'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)
    plt.title('Weather Condition', fontsize=14)
    plt.axis('equal')  
    plt.show()

def crash_per_country_per_year(conn):
    query = """
    SELECT crash_year, crash_country, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_year, crash_country
    ORDER BY crash_year, crash_country DESC
    """
    
    cpc = pd.read_sql_query(query, conn)
    return cpc

def scatter_crash_per_country_per_year(cpc):
    countries = cpc["crash_country"].unique()

    plt.figure(figsize=(12, 6))

    for country in countries:
        country_data = cpc[cpc["crash_country"] == country]
        plt.scatter(country_data["crash_year"], country_data["crash_count"], label=country)

    plt.xlabel("Year")
    plt.ylabel("Number of Crashes")
    plt.title("Crashes Per Country Per Year")
    plt.legend(title="Country", loc="upper left", bbox_to_anchor=(1, 1))  
    plt.show()

def crash_per_weather_per_year(conn):
    query = """
    SELECT crash_year, weather_conditions, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_year, weather_conditions
    ORDER BY crash_year, weather_conditions DESC
    """
    
    wpy = pd.read_sql_query(query, conn)
    return wpy

def scatter_crash_per_weather_per_year(wpy):
    weathers = wpy["weather_conditions"].unique()

    plt.figure(figsize=(12, 6))

    for weather in weathers:
        weather_data = wpy[wpy["weather_conditions"] == weather]
        plt.scatter(weather_data["crash_year"], weather_data["crash_count"], label=weather)

    plt.xlabel("Year")
    plt.ylabel("Number of Crashes")
    plt.title("Crashes Per Weather Per Year")
    plt.legend(title="Weather", loc="upper left", bbox_to_anchor=(1, 1))  
    plt.show()

def crash_per_weather_per_country(conn):
    query = """
    SELECT crash_country, weather_conditions, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_country, weather_conditions
    ORDER BY crash_country, weather_conditions DESC
    """
    
    wpc = pd.read_sql_query(query, conn)
    return wpc

def scatter_crash_per_weather_per_country(wpc):
    weathers = wpc["weather_conditions"].unique()

    plt.figure(figsize=(12, 6))

    for weather in weathers:
        weather_data = wpc[wpc["weather_conditions"] == weather]
        plt.scatter(weather_data["crash_country"], weather_data["crash_count"], label=weather)

    plt.xlabel("Year")
    plt.ylabel("Number of Crashes")
    plt.title("Crashes Per Weather Per Country")
    plt.legend(title="Weather", loc="upper left", bbox_to_anchor=(1, 1))  
    plt.show()

def main():
    conn = connect_to_db()
    df = crash_per_country(conn)
    cpr = crash_per_year(conn)
    wc = weather_condition(conn)
    cpc = crash_per_country_per_year(conn)
    wpy = crash_per_weather_per_year(conn)
    wpc = crash_per_weather_per_country(conn)
    conn.close()

    chart = int(input('Which chart would you like to see? \n\t1 = crashes per country\n\t2 = crashes per year\n3 = crashes per country\n4 = weather conditions\n5 = crashes per country per year\n6 = crashes per weather per year\n7 = crashes per weather per country'))
    if chart == 1:
        pie_crash_per_country(df)
    elif chart == 2:
        line_crash_per_year(cpr)
    elif chart == 3:
        bargraph_crash_per_country(df)
    elif chart == 4:
        pie_weather_condition(wc)
    elif chart == 5:
        scatter_crash_per_country_per_year(cpc)
    elif chart == 6:
        scatter_crash_per_weather_per_year(wpy)
    elif chart == 7:
        scatter_crash_per_weather_per_country(wpc)
    else:
        return

if __name__ == '__main__':

    main()
