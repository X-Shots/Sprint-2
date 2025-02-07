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
        print("Do you want to analyze another category?")
        choice = input("Enter 'yes' or 'no': ")
        if choice.lower() != 'yes':
            break
        category = input("Which data do you want to analyze:\ncrash_year\ncrash_country\nweather_condition\ncrash_setting\nType Category here: ")
        crash_data = fetch_crash_data(conn, category)
        if crash_data is "line":
            line_graph(crash_data, category)
        elif crash_data is "bar":
            bar_graph(crash_data, category)
        elif crash_data is "pie":
            pie_chart(crash_data, category)
        else:
            print("Invalid choice. Please choose 'line', 'bar', or 'pie'.")
        else:   
            category = input("Which data do you want to analyze:\ncrash_year\ncrash_country\nweather_condition\ncrash_setting\nType Category here: ")
        
            type_of_graph = input("What type of graph do you want to plot? (line, bar, pie, scatter): ")
            crash_data = fetch_crash_data(conn, category)
            if category is "crash_year":
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
                    

            elif category is "crash_country":
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
                    

            elif category is "weather_condition":
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
                    

            elif category is "crash_setting":
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

            else:
                print("Invalid category. Please choose one of the options. Make sure to spell correctly.")
        

    conn.close()
  

if __name__ == '__main__':

    main()
