import os
import sys
import logging
from typing import List
from google import genai
from google.genai.errors import ClientError
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

EMBEDDING_MODELS = [
    "models/gemini-embedding-001",
    "models/gemini-embedding-2-preview"
]


def embed_texts(texts: List[str], batch_size: int = 128) -> List[List[float]]:
    if not isinstance(texts, list):
        raise TypeError("texts must be a list of strings")

    if not texts:
        logger.info("embed_texts called with empty texts list")
        return []

    last_error = None

    for model_name in EMBEDDING_MODELS:
        try:
            logger.info("Embedding with model=%s count=%s", model_name, len(texts))

            all_embeddings: List[List[float]] = []
            for i in range(0, len(texts), batch_size):
                chunk = texts[i : i + batch_size]
                logger.info("Processing chunk %s-%s", i, i + len(chunk))
                response = client.models.embed_content(
                    model=model_name,
                    contents=chunk,
                )

                if not hasattr(response, "embeddings") or response.embeddings is None:
                    raise RuntimeError(f"No embeddings in response for model {model_name}")

                for e in response.embeddings:
                    values = getattr(e, "values", None)
                    if values is None:
                        raise RuntimeError("Embedding object missing values")
                    all_embeddings.append(values)

            if len(all_embeddings) != len(texts):
                raise RuntimeError(
                    f"Embedding count mismatch for model {model_name}:"
                    f" expected {len(texts)}, got {len(all_embeddings)}"
                )

            logger.info("Embedding successful with model %s", model_name)
            return all_embeddings

        except ClientError as e:
            logger.warning(
                "ClientError with model %s: %s", model_name, e, exc_info=True
            )
            last_error = e
        except Exception as e:
            logger.error(
                "Unexpected error with model %s: %s", model_name, e, exc_info=True
            )
            last_error = e

    raise RuntimeError(
        "Embedding failed for all candidate models: " + ", ".join(EMBEDDING_MODELS)
    ) from last_error
