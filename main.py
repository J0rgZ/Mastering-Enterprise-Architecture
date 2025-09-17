# main.py
from app.repositories import InMemoryUserRepository
from app.services import UserService

def main():
    """Main function to run the demonstration."""
    print("--- Setting up the application ---")
    
    # 1. Create a repository instance (the data layer)
    # We could easily swap this for a PostgresUserRepository without changing the service.
    user_repo = InMemoryUserRepository()
    
    # 2. Create a service instance and inject the repository (the business logic layer)
    user_service = UserService(repository=user_repo)
    
    print("\n--- Running the application logic ---")
    
    # Use the service to perform operations
    user1 = user_service.create_user(1, "john_doe", "john.doe@example.com")
    user2 = user_service.create_user(2, "jane_smith", "jane.smith@example.com")
    
    print("-" * 20)
    
    # Retrieve a user
    retrieved_user = user_service.get_user(1)
    if retrieved_user:
        print(f"Successfully retrieved user: {retrieved_user.username}")
        assert retrieved_user.username == "john_doe"
        
    print("-" * 20)
        
    # Try to retrieve a non-existent user
    non_existent_user = user_service.get_user(99)
    if not non_existent_user:
        print("Correctly handled non-existent user.")

if __name__ == "__main__":
    main()