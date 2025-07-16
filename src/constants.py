from dotenv import load_dotenv
import os

load_dotenv()

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MAX_COMMENTS = 200
