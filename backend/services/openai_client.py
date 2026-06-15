import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
api_key=os.getenv(
"GITHUB_TOKEN"
),
base_url=
"https://models.inference.ai.azure.com"
)

MODEL_NAME = "gpt-4o-mini"
