import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

def get_llm():
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client
