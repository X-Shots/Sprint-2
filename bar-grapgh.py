import matplotlib.pyplot as plt
import psycopg2
import pandas as pd

import numpy as np

# crashes = '''SELECT crash_country, COUNT(*) as crash_count
#     FROM crash_table
#     GROUP BY crash_country
#     ORDER BY crash_count DESC'''
# slaes = pd.read_sql_query(crashes, conn)

# plt.bar(crashes['crash_country'], crashes['crash_count'])
# plt.title('Car Crashes')
# plt.xlabel('lol')
# plt.ylabel('number of crashes')
# plt.show(crashes)

import matplotlib.pyplot as plt
import numpy as np

def connect_to_db():
    return psycopg2.connect(
        dbname="postgres",  
        user="postgres",         
        password="l9l9L(L(",     
        host="localhost",           
        port="5432"                   
    )

def crashes_per_year(conn):
    query = """
        SELECT crash_country, COUNT(*) as crash_count
        FROM crash_table
        GROUP BY crash_country
        ORDER BY crash_count DESC
        """
    bar = pd.read_sql_query(query,conn)
    return bar


def bargraph_crash_per_country():
    plt.bar()
    plt.title('Crashes')
    plt.xlabel('Countries')
    plt.ylabel('Crashes')
    plt.show()

def main()
    conn = connect_to_db()
    crashes = crashes_per_year(conn)
    conn.close()

    bragraph(bar)



# Connect to the PostgreSQL database    
