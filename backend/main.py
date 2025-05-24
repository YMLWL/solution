import os
import uvicorn

from fastapi import FastAPI
from google.adk.cli.fast_api import get_fast_api_app

ALLOWED_ORIGINS = ["*"]
AGENT_DIR = os.path.dirname(os.path.abspath(__file__))


app: FastAPI = get_fast_api_app(
    agent_dir=AGENT_DIR,
    allow_origins=ALLOWED_ORIGINS,
    web=True,
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
