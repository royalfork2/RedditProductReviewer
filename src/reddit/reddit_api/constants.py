from dotenv import load_dotenv
import os

load_dotenv()

# Constants needed for the Reddit API
CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USERNAME = os.getenv("REDDIT_USERNAME")
PASSWORD = os.getenv("REDDIT_PASSWORD")
USER_AGENT = "ReviewAnalyzer by u/Imaginary-Weekend55"
