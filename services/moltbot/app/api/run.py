from typing import Any, Dict

from fastapi import APIRouter
from pydantic import BaseModel

from app.core.dispatcher import dispatch

router = APIRouter()


class RunRequest(BaseModel):
    task: str
    input: str
    payload: Dict[str, Any] = {}


@router.post("/run")
def run_task(req: RunRequest):
    return dispatch(req.task, req.input, req.payload)

