import pandas as pd
import sqlite3

# load and print rows of the csv dataframe
df = pd.read_csv('test_3.csv')
print(df.head()) # check rows of data frame

# connect to sqlite3 and add users as a new table
conn = sqlite3.connect('test_3.db') # connect to the sql database
df.to_sql('users', conn, if_exists='replace', index=False)
conn.close()

# now in sqlite3 test_3.db, we can run QUERIES
# Ex: SELECT * FROM users; will return all of the rows and columns
# SELECT * FROM users LIMIT 1; will only return 1st row
# SELECT * FROM users WHERE age = 20; will only return rows where age = 20