# app/repositories.py
from abc import ABC, abstractmethod
from typing import Dict, Optional
from .models import User

class AbstractUserRepository(ABC):
    """Defines the contract for a user repository."""
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        """Gets a user by their ID."""
        raise NotImplementedError

    @abstractmethod
    def add(self, user: User):
        """Adds a new user."""
        raise NotImplementedError

class InMemoryUserRepository(AbstractUserRepository):
    """A concrete implementation of the repository using an in-memory dictionary."""

    def __init__(self):
        self._users: Dict[int, User] = {}
        print("Initialized InMemoryUserRepository")

    def get_by_id(self, user_id: int) -> Optional[User]:
        print(f"Repository: Fetching user {user_id} from memory.")
        return self._users.get(user_id)

    def add(self, user: User):
        print(f"Repository: Adding user {user.username} to memory.")
        self._users[user.id] = user