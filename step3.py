## EC530 SQL LLM Hackathon
import logging
from step2 import *

### STEP 3 ###
# Objective: Learn to build robust systems that validates inputs

logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')

def table_exists(cursor, table_name):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cursor.fetchone() is not None
    except Exception as e:
        logging.error(f"Error checking if table exists: {e}")
        return False

# create table
def create_table_from_csv(cursor, csv_filename, table_name):  # using sqlite
    try:
        if table_exists(cursor, table_name):
            print(f"Table '{table_name}' already exists.")
            choice = input("Schema conflict: [D]rop old table, or [S]kip? ").strip().lower()
            if choice == 'o':
                drop_table(cursor, table_name)
            elif choice == 's':
                print("Operation skipped.")
            else:
                print("Invalid choice. Skipping operation.")
        else:
            df = pd.read_csv(csv_filename)
            table_query = generate_table_query(df, table_name)
            cursor.execute(table_query)
            print(f'Created table {table_name}\n')
            return table_query
    except Exception as e:
        logging.error(f"Error creating table '{table_name}': {e}")
        print(f"Failed to create table '{table_name}'. Check error_log.txt.")

#read table
def get_schema(cursor, table_name):
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Error fetching schema for table '{table_name}': {e}")
        return None

# delete table
def drop_table(cursor, table_name):
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
        print(f"Table '{table_name}' dropped.")
    except Exception as e:
        logging.error(f"Error dropping table '{table_name}': {e}")

def execute_query(cursor, query):  # using sqlite
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        return results
    except Exception as e:
        logging.error(f"SQL query failed: {e}")
        return None

def list_tables(cursor):
    try:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Failed to list tables: {e}")
        return None