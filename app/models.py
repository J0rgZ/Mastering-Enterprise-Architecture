# app/models.py
from dataclasses import dataclass

@dataclass
class User:
    """A simple data class representing our domain model."""
    id: int
    username: str
    email: str