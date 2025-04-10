import pandas as pd
import sqlite3
import os
import logging
from step1 import *
from step2 import *
from step3 import *
from step4 import *


# Generated with help from ChatGPT



### STEP 1 ###
# CSV_FILENAME = 'test_3.csv'
# DB_FILENAME = 'test_3.db'
# TABLE_NAME = 'users'

# Create a small sample CSV for testing
# try:
#     sample_data = pd.DataFrame({
#         'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [22, 30, 21],
#         'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
#     })
#     sample_data.to_csv(CSV_FILENAME, index=False)
# except Exception as e:
#     logging.error(f"Failed to create test CSV: {e}")
#
# # Run Step 1: load CSV and copy into SQLITE with pandas
# try:
#     print('Test data:')
#     copy_table_from_csv(CSV_FILENAME, DB_FILENAME, TABLE_NAME)
#     print('-------------------------------------------------')
#     print(f"Step 1 - Created table {TABLE_NAME} in {DB_FILENAME}\n")
# except Exception as e:
#     logging.error(f"Error loading/storing CSV data: {e}")



### STEP 2 ###

# Run Step 2/3: load CSV and execute in SQLITE with a SQL table query
# try:
#     sql_command = create_table_from_csv(CSV_FILENAME, DB_FILENAME, TABLE_NAME)
#     print(f'Step 2 - Generated and executed SQL Query: \n{sql_command}\n')
# except Exception as e:
#     logging.error(f"Error running create_table: {e}")



### STEP 3 ###

# Run Step 3: Validate the inputs
# try:
#     with sqlite3.connect(DB_FILENAME) as conn:
#         cursor = conn.cursor()
#         print(f"Fetched table {TABLE_NAME} schema: ", get_table_schema(cursor, TABLE_NAME))
#         print(f"Check if table {TABLE_NAME} exists: ", table_exists(cursor, TABLE_NAME))
# except Exception as e:
#     logging.error(f"Error verifying table structure: {e}")


# Run Step 3: Validate the inputs
# try:
#     db_filename = input("Enter database name [name].db: ")
#     table_name = input("Enter table name to create: ")
#
#     if not os.path.exists(db_filename):
#         print("Database does not exist. It will be created.")
#
#     conn = sqlite3.connect(db_filename)
#     cursor = conn.cursor()
#     if table_exists(cursor, table_name):
#         print(f"Table '{table_name}' already exists.")
#         existing_schema = get_table_schema(cursor, table_name)
#         print("Existing schema:")
#         for column in existing_schema:
#             print(f" - {column[1]} ({column[2]})")
#
#         choice = input("Schema conflict: [O]verwrite, [R]ename, or [S]kip? ").strip().lower()
#         if choice == 'o':
#             drop_table(cursor, table_name)
#             create_table_from_query(cursor, db_filename, table_name)
#         elif choice == 'r':
#             new_name = input("Enter new table name: ")
#             create_table_from_query(cursor, db_filename, new_name)
#         elif choice == 's':
#             print("Operation skipped.")
#         else:
#             print("Invalid choice. Skipping operation.")
#     else:
#         create_table_from_query(cursor, db_filename, table_name)
#     conn.commit()
#     conn.close()
# except Exception as e:
#     logging.error(f"Error during user prompt section: {e}")

### STEP 4 ###
# try:
#     df = pd.read_csv(CSV_FILENAME)
#     with sqlite3.connect(DB_FILENAME) as conn:
#         cursor = conn.cursor()
#         interactive_cli(cursor, DB_FILENAME)
# except Exception as e:
#     print(f'Error: {e}')


### STEP 5 ###
# Run Step 5: Incorporate the LLM in the CLI and can specicially ask user for what database they want to work on
CSV_FILENAME = 'default.csv'
TABLE_NAME = 'default'
DB_FILENAME = input('Enter a database file name <name>.db: ')
try:
    with sqlite3.connect(DB_FILENAME) as conn:
        cursor = conn.cursor()
        interactive_cli(cursor, DB_FILENAME)
except Exception as e:
    print(f'Error: {e}')

# Optional Cleanup
# try:
#     os.remove(CSV_FILENAME)
#     os.remove(DB_FILENAME)
# except Exception as e:
#     logging.error(f"Cleanup failed: {e}")
