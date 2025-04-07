import pandas as pd
import sqlite3

### STEP 2 ###
# go over csv column names and data types and convert to sql data type
def datatype_csv_to_sql(data_type):
    if pd.api.types.is_integer_dtype(data_type):
        return "INTEGER" # sql equivalent
    elif pd.api.types.is_float_dtype(data_type):
        return "FLOAT"
    else: # can add more later
        return "TEXT"

# generate CREATE TABLE query
def table_query(df, user_table_name):
    col_types = []
    for col in df.columns:
        sql_type = datatype_csv_to_sql(df[col].dtype)
        col_types.append(f'"{col}" {sql_type}') # puts in format: "{columns}" TEXT for example
    col_sql = ', \n '.join(col_types)
    create_sql = f'CREATE TABLE IF NOT EXISTS "{user_table_name}" (\n   {col_sql}\n);'
    return create_sql


# reads CSV, iterates columns, infers schema, and creates table
def create_table(user_csv, user_db, user_table_name):
df = pd.read_csv(user_csv)
create_sql = table_query(df, user_table_name)

# connect to sqlite3
with sqlite3.connect(user_db) as conn:
    cursor = conn.cursor()
    cursor.execute(create_sql)
    conn.commit()
return create_sql

