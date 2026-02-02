from fastapi import FastAPI

app = FastAPI(title="Moltbot", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/whoami")
def whoami():
    return {"service": "moltbot", "mode": "local"}
