import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the PostgreSQL database
def connect_to_db():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres",         
        password="l9l9L(L(",     
        host="localhost",           
        port="5432"                   
    )

# Function to fetch crash data by a given category (crash_year or crash_country)
def fetch_crash_data(conn, category):
    if category not in ['crash_year', 'crash_country', 'weather_condition', 'crash_setting']:
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

# Plot bar graph
def bar_graph(df, category):
    plt.figure(figsize=(10, 6))
    plt.bar(df[category], df['crash_count'], color='skyblue')
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.xlabel(category.replace('_', ' ').title(), fontsize=12)
    plt.ylabel('Number of Crashes', fontsize=12)
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()  
    plt.show()

# Plot pie chart
def pie_chart(df, category):        
    plt.figure(figsize=(8, 8))
    plt.pie(df['crash_count'], labels=df[category], autopct='%1.1f%%', startangle=140)
    plt.title(f'Car Crashes per {category.replace("_", " ").title()}', fontsize=14)
    plt.axis('equal')  
    plt.show()  

# Plot scatter plot
def scatter_plot(df, category):
    return None


def main():
    conn = connect_to_db()

    #menu
    while True:
        category = input("Enter a category to analyze (crash_year, crash_country, weather_condition, crash_setting): ").strip().lower()
        type_of_graph = input("What type of graph do you want to plot? (line, bar, pie, scatter): ").strip().lower()
    

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
            continue

        choice = input("Do you want to analyze another category? (yes/no): ").strip().lower()
        if choice != "yes":
            break

    conn.close()


if __name__ == '__main__':

    main()
