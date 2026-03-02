from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    description: Optional[str] = None