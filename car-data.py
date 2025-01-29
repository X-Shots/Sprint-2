import psycopg2
import pandas as pd
import matplotlib.pyplot as plt


# Connect to your PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres",         
        password="l9l9L(L(",     
        host="localhost",           
        port="5432"                   
    )
    # Check if the connection works
    print("Connected to the database!") 
    return conn



# # Fetch data from database
# def fetch_car_crash_data(conn):
#     query = """
#     SELECT crash_year, COUNT(*) as crash_count
#     FROM crash_table
#     GROUP BY crash_year
#     ORDER BY crash_year
#     """
    
#     df = pd.read_sql_query(query, conn)
#     return df

# # Plot data
# def plot_data(df):
#     plt.figure(figsize=(10, 6))
#     plt.plot(df['crash_year'], df['crash_count'], marker='o', linestyle='-', color='b')

#     plt.title('Car Crashes per Year', fontsize=14)
#     plt.xlabel('Year', fontsize=12)
#     plt.ylabel('Number of Crashes', fontsize=12)

#     plt.grid(True)

#     plt.show()




def fetch_car_crash_data2(conn):
    query = """
    SELECT crash_country, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_country
    ORDER BY crash_count DESC
    """
    
    df = pd.read_sql_query(query, conn)  # Use pd.read_sql_query for direct DataFrame creation
    return df

# Plot pie chart
def plot_pie_chart(df):
    plt.figure(figsize=(8, 8))  # Create a square figure for better pie chart display
    plt.pie(df['crash_count'], labels=df['crash_country'], autopct='%1.1f%%', startangle=90, colors=plt.cm.Paired.colors)

    plt.title('Car Crashes by Country', fontsize=14)

    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    plt.show()  # Display the pie chart

def main():
    conn = connect_to_db()
    df = fetch_car_crash_data2(conn)
    conn.close

    plot_pie_chart(df)

if __name__ == '__main__':
    main()
