# app/services.py
from typing import Optional
from .models import User
from .repositories import AbstractUserRepository

class UserService:
    """
    Contains the business logic for users.
    It depends on the repository interface, not a concrete implementation.
    """
    def __init__(self, repository: AbstractUserRepository):
        self._repository = repository
        print("UserService initialized with a repository.")

    def create_user(self, user_id: int, username: str, email: str) -> User:
        """Creates and saves a new user."""
        print(f"Service: Business logic for creating user '{username}'.")
        new_user = User(id=user_id, username=username, email=email)
        self._repository.add(new_user)
        return new_user

    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieves a user."""
        print(f"Service: Business logic for fetching user {user_id}.")
        return self._repository.get_by_id(user_id)