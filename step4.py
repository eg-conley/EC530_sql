## EC530 SQL LLM Hackathon
import logging
from step3 import *
from step5 import *

### STEP 4 ###
# Objective: Create a simple, interactive assistant using Python CLI

# CLI Interface

# display available commands
def print_help():
    print("\nAvailable commands:")
    print("  load <csv_path> [table_name] - Load CSV into database")
    print("  query <sql_query>           - Execute SQL query")
    print("  ask <table> <question>      - Generate SQL from natural language model")
    print("  tables                      - List all tables")
    print("  schema <table_name>         - Show table schema")
    print("  help                        - Show this help message")
    print("  exit                        - Exit the program")

def interactive_cli(cursor, db_filename):
    print("\nWelcome to the SQL Assistant CLI")
    print("Type 'help' for available commands.")

    while True:
        try:
            user_input = input("\n> ").strip()
            if not user_input:
                continue

            # parse input
            parts = user_input.split(maxsplit=1)
            command = parts[0].lower()

            if command == "exit":
                print("Exiting...")
                break

            elif command == "help":
                print_help()

            elif command == "load":
                if len(parts) < 2:
                    print("Please specify a CSV file. Usage: load <csv_path> [table_name]")
                    continue
                load_parts = parts[1].split(maxsplit=1)
                csv_filename = load_parts[0]
                table_name = 'default' if len(load_parts) < 2 else load_parts[1]
                create_table_from_csv(cursor, csv_filename, table_name)

            elif command == "query":
                if len(parts) < 2:
                    print("Please specify a query. Usage: query <sql_query>")
                    continue
                query = parts[1]
                results = execute_query(cursor, query)
                if results is not None:
                    if not results:
                        print("Query executed successfully but returned no results.")
                    else:
                        print("\nQuery results:")
                        print(results)
                else:
                    print("Query failed. Check error log for details.")

            ## have yet to implement the LLM
            elif command == "ask":
                if len(parts) < 2:
                    print("Please specify a table and question. Usage: ask <table_name> <question>")
                    continue
                ask_parts = parts[1].split(maxsplit=1)
                if len(ask_parts) < 2:
                    print("Please specify both table name and question.")
                    continue

                table_name = ask_parts[0]
                question = ask_parts[1]
                schema = get_schema(cursor, table_name)
                if not schema:
                    print(f"Schema for table '{table_name}' not found.")
                    continue
                print("\nGenerating SQL for your question")
                generated_query = generate_sql_from_llm(table_name, question, schema)

                if generated_query:
                    print(f"\nGenerated query:\n{generated_query}")

                    confirm = input("Execute this query? [Y/N] ").strip().lower()
                    if confirm == 'y':
                        results = execute_query(cursor, generated_query)
                        if results is not None:
                            if not results:
                                print("Query executed successfully but returned no results.")
                            else:
                                print("\nQuery results:")
                                print(results)
                    else:
                        print("Query not executed.")
                else:
                    print("Failed to generate SQL for your question.")

            elif command == "tables":
                tables = list_tables(cursor)
                print(tables)

            elif command == "schema":
                if len(parts) < 2:
                    print("Please specify a table name. Usage: schema <table_name>")
                    continue
                table_name = parts[1].strip()
                schema = get_schema(cursor, table_name)
                print(schema)

            else:
                print(f"Unknown command: {command}. Type 'help' for available commands.")



            # elif command == "ask":
            #     if len(parts) < 2:
            #         print("Please specify a table and question. Usage: ask <table_name> <question>")
            #         continue
            #
            #     ask_parts = parts[1].split(maxsplit=1)
            #     if len(ask_parts) < 2:
            #         print("Please specify both table name and question.")
            #         continue
            #
            #     table_name = ask_parts[0]
            #     question = ask_parts[1]
            #
            #     print(f"\nGenerating SQL for: '{question}'")
            #     generated_sql = generate_sql_from_natural_language(db_path, table_name, question)
            #
            #     if generated_sql:
            #         print(f"Generated SQL:\n{generated_sql}")
            #
            #         # Ask for confirmation before executing
            #         confirm = input("Execute this query? [y/N] ").strip().lower()
            #         if confirm == 'y':
            #             results = execute_sql_query(db_path, generated_sql)
            #
            #             if results is not None:
            #                 if not results:
            #                     print("Query executed successfully but returned no results.")
            #                 else:
            #                     print("\nQuery results:")
            #
            #         else:
            #             print("Query not executed.")
            #     else:
            #         print("Failed to generate SQL for your question.")
        except KeyboardInterrupt:
            print("\nType 'exit' to quit the program.")
        except Exception as e:
            logging.error(f"CLI error: {e}")
            print("An error occurred. Check error log for details.")