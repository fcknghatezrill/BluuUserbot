import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.environ.get("MAX_BOT"))

DEVS = list(map(int, os.environ.get("DEVS", "7779651486").split()))

API_ID = int(os.environ.get("API_ID", "21801044"))

API_HASH = os.environ.get("API_HASH", "f8b8c21ad946683f79a4814c743cffd1")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7771682570:AAEm3PGqrjXgg_bEnKQaD8B2jUdj98uL>")

OWNER_ID = int(os.environ.get("OWNER_ID", "7779651486"))

BLACKLIST_CHAT = list(map(int, os.environ.get("BLACKLIST_CHAT", "-1002125842026").split()))

RMBG_API = os.environ.get("RMBG_API", "uiuHHXvfXK8ADSUycDCHzFU3")

MONGO_URL = os.environ.get("mongodb+srv://crystaline028:C2OChFlMoB2NI9fo@cluster0.1yhtvoo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.environ.get("LOGS_MAKER_UBOT", "-2745239674"))
