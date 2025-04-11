# SQL Assistant Application 🤖

## Table of Contents
 1. [Overview](#overview)
 2. [File Structure](#file-structure)
 3. [How to Use](#how-to-use)
 4. [Future Improvements](#future-improvements)

## Overview
This application allows users to create and manage SQLite Databases through a CLI. Users can choose from a variety of features including asking a chat bot (through OpenAI's API) a question related to databases.

## API
https://github.com/openai/openai-python

## Features
* Automated SQL table creation from CSV file
* Variety of inout validation: Testing for existing tables, schema validation
* Simple, interactive, user-friendly CLI
* LLM integration allowing for simple plain language prompts

## Command Options
1. load <csv_path> [table_name]: Load CSV into the database initally specified
2. query <sql_query>: Execute SQL query
3. ask <table> <question>: Generate SQL from natural language model
4. tables: List all tables
5. schema <table_name>: Show table schema
6. help: Show this help message
7. exit: Exit the program

## File Structure
EC530_sql/ \
|-- error_log.txt # check the error logs \
|-- main.py # runs all 5 steps\
|-- step1.py # structure of CSV and how it maps to SQL tables (commented out) \
|-- step2.py # automate table creation by inferring schema from CSV \
|-- step3.py # table creation, query exectution, and validation functions \
|-- step4.py # CLI functions \
|-- step5.py # OpenAI integration\
|-- test_data.csv # test csv file for uploading \
|-- testing.db # test database to work on

## How to Use
### Requirements
* Python 3.9 or newer
* MacOS, Windows
* Python packages: pandas, logging, sqlite3, os, dotenv, openai
  
### Steps
 1. Clone the repository
 2. Navigate to the directory containing the files
 3. Open a terminal/shell
 5. Run python3 main.py [port] (in virtual environment)
 6. Follow CLI options

### Example Use
* The first CL prompt will be for a database. Enter the name of the desired database you would like to edit in the format `<database_filename>.db`
> <img width="585" alt="Enter database name" src="https://github.com/user-attachments/assets/17fe8dee-1f5d-482a-9bf0-ca819c864bff"/>
* Type `help` to list options
> <img width="583" alt="Screenshot 2025-04-11 at 5 55 45 PM" src="https://github.com/user-attachments/assets/cf8a6eef-a11c-4056-a108-409f7e8743ff" />
* Execute any SQL query with `query [your_query]`
> <img width="564" alt="Screenshot 2025-04-11 at 6 01 32 PM" src="https://github.com/user-attachments/assets/71b84ca0-7fdb-4b76-8d1f-7055684b74a9" /> \
> <img width="227" alt="Screenshot 2025-04-11 at 6 02 51 PM" src="https://github.com/user-attachments/assets/95b87427-31b6-4c5a-98eb-17104a090341" />
* Enter any plain language request and get a SQL command with `ask [your_prompt]`
* List all of the current tables in the database with `tables`
> <img width="201" alt="Screenshot 2025-04-11 at 5 57 47 PM" src="https://github.com/user-attachments/assets/27c962e3-213e-413d-9113-2d2a4b49a2e2" />
* Get the schema of a specific table in the database with `schema <table_name>`
> <img width="820" alt="Screenshot 2025-04-11 at 5 59 01 PM" src="https://github.com/user-attachments/assets/a97da7cb-4410-44ff-a10a-9fba36ad0ed4" />
* Find any errors in the error log command!
> <img width="570" alt="Screenshot 2025-04-11 at 6 05 35 PM" src="https://github.com/user-attachments/assets/c3aa9e34-5cd5-4784-b51d-62921e1dbb1e" /> \
> <img width="534" alt="Screenshot 2025-04-11 at 6 05 52 PM" src="https://github.com/user-attachments/assets/3cfb6b83-b64b-4715-8cfc-12be6ee7f7a3" />

## Future Improvements
* Improve the CLI and add more options
* Create more of a GUI
* Improve the organization and efficiency of code

## Acknowledgements
* Code derived from ChatGPT and edited for use
