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

counrties = """
    SELECT crash_country, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_country
    ORDER BY crash_count DESC
    """
crashes = """
    SELECT crash_year, COUNT(*) as crash_count
    FROM crash_table
    GROUP BY crash_year
    ORDER BY crash_year
    """

plt.bar(counrties, crashes)
plt.title('Fruit Sales')
plt.xlabel('Countries')
plt.ylabel('Crashes')
plt.show()


# Connect to the PostgreSQL database    
