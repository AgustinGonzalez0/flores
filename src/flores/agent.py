from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Agent:
    name: str = "flores"
    memory: list[dict[str, Any]] = field(default_factory=list)

    def run(self, task: str) -> str:
        self.memory.append({"task": task, "status": "completed"})
        return self.respond(task)

    def respond(self, task: str) -> str:
        response = f"{self.name} will handle: {task}."
        self.memory.append({"task": task, "response": response})
        return response
