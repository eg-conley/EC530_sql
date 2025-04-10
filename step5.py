## EC530 SQL LLM Hackathon
from openai import OpenAI
import os
import logging
from dotenv import load_dotenv

load_dotenv()
### STEP 5 ###
# Objective: Enable interaction through plain language using ChatGPT or another LLM

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY"),
)

def generate_sql_from_llm(table_name, schema, question):
    prompt = f""" You are a helpful assistant that writes SQLite queries. Here is the schema for the table '{table_name}': {schema}
    Write an SQL query (no explanation) to answer this question: "{question}" """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI API call failed: {e}")
        return None