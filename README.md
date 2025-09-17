# Repository Pattern Demo

This repository contains a simple Python project to demonstrate the **Repository Pattern**, a fundamental pattern from Martin Fowler's "Patterns of Enterprise Application Architecture".

## What is the Repository Pattern?

The Repository pattern mediates between the application's domain (business logic) and data mapping layers. It provides a clean, collection-like interface for accessing domain objects, completely hiding the details of the underlying data source.

## Benefits Shown in this Demo

*   **Decoupling:** The `UserService` has no knowledge of the `InMemoryUserRepository`. It only knows about the `AbstractUserRepository` interface.
*   **Testability:** The service can be easily tested by passing a mock repository.
*   **Separation of Concerns:** The project is structured to separate models, data access (repositories), and business logic (services).

## Project Structure