import os 
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

DB_CONFIG = {
    "driver": "{SQL Server}",
    "server": os.getenv("DB_SERVER"),
    "database": os.getenv("DB_DATABASE"),
    "uid": os.getenv("DB_USERNAME"),
    "pwd": os.getenv("DB_PASSWORD")
}