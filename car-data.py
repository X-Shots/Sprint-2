import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
print("please work")

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

def main():
    conn = connect_to_db()
    df = crash_per_country(conn)
    cpr = crash_per_year(conn)
    conn.close()

    chart = int(input('Which chart would you like to see? \n\t1 = crashes per country\n\t2 = crashes per year\n: '))
    if chart == 1:
        pie_crash_per_country(df)
    elif chart == 2:
        line_crash_per_year(cpr)
    else:
        return

if __name__ == '__main__':

    main()
