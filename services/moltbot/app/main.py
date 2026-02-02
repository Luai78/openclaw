from fastapi import FastAPI

from app.core.logging import setup_logging
from app.api.health import router as health_router
from app.api.run import router as run_router

setup_logging()

app = FastAPI(title="Moltbot")

app.include_router(health_router)
app.include_router(run_router)


