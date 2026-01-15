import io
import requests
from typing import Optional
from pathlib import Path
from pdfminer.high_level import extract_text  # pip install pdfminer.six

def download_pdf(url: str, save_dir: str = "data/pdfs") -> Optional[str]:
    Path(save_dir).mkdir(parents=True, exist_ok=True)
    try:
        resp = requests.get(url, timeout=20)
        if resp.status_code == 200 and "application/pdf" in resp.headers.get("content-type", ""):
            fname = url.split("/")[-1].split("?")[0] or "download.pdf"
            path = Path(save_dir) / fname
            path.write_bytes(resp.content)
            return str(path)
    except Exception:
        return None
    return None

def extract_pdf_text(path: str) -> str:
    try:
        text = extract_text(path)
        return text or ""
    except Exception:
        return ""
