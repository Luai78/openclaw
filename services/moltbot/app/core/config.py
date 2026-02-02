import os

class Settings:
    ENV = os.getenv("MOLTBOT_ENV", "dev")
    LOG_LEVEL = os.getenv("MOLTBOT_LOG_LEVEL", "info")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
