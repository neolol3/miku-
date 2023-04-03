from os import environ, path

from dotenv import load_dotenv

if path.exists("config.env"):
    load_dotenv("config.env")

TOKEN = environ.get("TOKEN", None)
API_ID = int(environ.get("API_ID", 6))
API_HASH = environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
Dev = [int(x) for x in environ.get("Dev", "").split()]
LOG_GROUP_ID = int(environ.get("LOG_GROUP_ID", None))
GBAN_LOG_GROUP_ID = int(environ.get("GBAN_LOG_GROUP_ID", None))
MESSAGE_DUMP_CHAT = int(environ.get("MESSAGE_DUMP_CHAT", None))
WELCOME_DELAY_KICK_SEC = int(environ.get("WELCOME_DELAY_KICK_SEC", None))
MONGO_URL = environ.get("MONGO_URL", None)
ARQ_API_URL = environ.get("ARQ_API_URL", None)
ARQ_API_KEY = environ.get("ARQ_API_KEY", None)
RSS_DELAY = int(environ.get("RSS_DELAY", None))
UPSTREAM_REPO = environ.get(
    "UPSTREAM_REPO", "https://github.com/DesiNobita/SuzuneBot.git"
)