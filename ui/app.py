"""Minimal UI entrypoint (Flask)."""

from flask import Flask, render_template_string
import sys
import importlib.metadata as importlib_metadata

app = Flask(__name__)

def get_pkg_version(name: str) -> str:
    try:
        return importlib_metadata.version(name)
    except importlib_metadata.PackageNotFoundError:
        return "not installed"

@app.route("/")
def index():
    print("Flask sys.executable:", sys.executable)
    print("Flask google-genai:", get_pkg_version("google-genai"))
    print("Flask langgraph:", get_pkg_version("langgraph"))

    return render_template_string(
        "<h1>AI Research Agent UI</h1>"
        "<p>Python executable: {}<br>google-genai: {}<br>langgraph: {}</p>".format(
            sys.executable,
            get_pkg_version("google-genai"),
            get_pkg_version("langgraph"),
        )
    )


# Run with: flask --app ui.app run
