import openai
import os
from dotenv import load_dotenv

load_dotenv()

def extract_table_contents(text):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt = f"""
    The following text is extracted from an image of a table. Please analyze it and return the table contents in a structured format:

    {text}

    Format the table as a list of lists, where each inner list represents a row in the table.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts and structures table contents from text."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0]['message']['content']
