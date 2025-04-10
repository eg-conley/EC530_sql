## EC530 SQL LLM Hackathon
import pandas as pd
import sqlite3

### STEP 1 ###
# Objective: Understand the structure of CSV and how it maps to SQL tables

# in sqlite3 we can run QUERIES
# Ex: SELECT * FROM users; will return all of the rows and columns
# SELECT * FROM users LIMIT 1; will only return 1st row
# SELECT * FROM users WHERE age = 20; will only return rows where age = 20

# def create_table_from_csv(csv_filename, db_filename, table_name):
#     # load and print rows of the csv dataframe
#     df = pd.read_csv(csv_filename)
#     print(df.head())
#
#     # connect to sqlite3 and add as a new table
#     conn = sqlite3.connect(db_filename) # connect to the sql database
#     df.to_sql(f'{table_name}', conn, if_exists='replace', index=False)
#     conn.close()