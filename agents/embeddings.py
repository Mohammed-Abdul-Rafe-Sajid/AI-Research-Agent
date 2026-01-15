from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def embed_texts(texts: list[str]) -> list[list[float]]:
    vectors = []
    for t in texts:
        resp = client.models.embed_content(
            model="models/text-embedding-004",
            contents=t
        )
        # NEW SDK: embeddings is a list
        vectors.append(resp.embeddings[0].values)
    return vectors
