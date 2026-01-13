"""Minimal UI entrypoint (Flask)."""
from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string("<h1>AI Research Agent UI</h1>")


# Run with: flask --app ui.app run
