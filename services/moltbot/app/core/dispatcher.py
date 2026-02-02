from typing import Any, Dict, Callable

from app.tasks.echo import run as echo_run
from app.tasks.uppercase import run as uppercase_run
from app.tasks.status import run as status_run


TaskFn = Callable[[str, Dict[str, Any]], Any]

TASKS: Dict[str, TaskFn] = {
    "echo": echo_run,
    "uppercase": uppercase_run,
    "status": status_run,
}


def dispatch(task: str, text: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    fn = TASKS.get(task)
    if fn is None:
        return {
            "task": task,
            "status": "error",
            "error": f"unknown task: {task}",
            "available": sorted(TASKS.keys()),
        }

    result = fn(text, payload)
    return {"task": task, "status": "ok", "result": result}

