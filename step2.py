## EC530 SQL LLM Hackathon
import pandas as pd
import sqlite3

### STEP 2 ###
# Objective: Automate table creation by inferring schema from CSV

# go over csv column names and data types and convert to sql data type
def datatype_csv_to_sql(data_type):
    if pd.api.types.is_integer_dtype(data_type):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(data_type):
        return "FLOAT"
    else:
        return "TEXT"
    # can add more later

# generate sql query
def generate_table_query(df, table_name):
    col_types = []
    for col in df.columns:
        sql_type = datatype_csv_to_sql(df[col].dtype)
        col_types.append(f'"{col}" {sql_type}') # puts in format: "{columns}" TEXT for example
    col_sql = ', \n '.join(col_types)
    table_query = f'CREATE TABLE IF NOT EXISTS "{table_name}" (\n {col_sql}\n);'
    return table_query