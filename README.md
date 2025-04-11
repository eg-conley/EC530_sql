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
|-- main.py # \
|-- step1.py # \
|-- step2.py # \
|-- step3.py # \
|-- step4.py # \
|-- step5.py # \
|-- test_data.csv # \
|-- testing.db #

## How to Use
### Requirements
* Python 3.9 or newer
* MacOS, Windows
* Python packages: 

### Steps
 1. Clone the repository
 2. Navigate to the directory containing the files
 3. Open a terminal/shell
 4. Run python3 main.py [port] (in virtual environment)

### Example Use
*
  
## Future Improvements
* 

## Acknowledgements
* Code derived from ChatGPT and edited for use
