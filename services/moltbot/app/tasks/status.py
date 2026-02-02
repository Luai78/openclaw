import time

START_TS = time.time()

def run(text: str, payload: dict) -> dict:
    return {
        "service": "moltbot",
        "state": "running",
        "uptime_s": round(time.time() - START_TS, 2),
    }

