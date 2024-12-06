# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

Welcome to the Event Manager Company! As a newly hired Software QA Analyst/Developer and a student in software engineering, you are embarking on an exciting journey to contribute to our project aimed at developing a secure, robust REST API that supports JWT token-based OAuth2 authentication. This API serves as the backbone of our user management system and will eventually expand to include features for event management and registration.

## Issue resolved:

1. #### Min password length as 8 char:
 Improved password validation by introducing a `password_min_length` function to ensure user passwords meet security best practices. This function enforces a minimum length of 8 characters, preventing the use of weak, overly short passwords. This enhancement reinforces account security by adhering to current password policy standards.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/5-minimum-password-length-of-8-character

2. #### remove duplicate login endpoint : 
Streamlined the user route by eliminating the duplicate login endpoint, consolidating it into a single login route. This adjustment minimizes redundancy, enhances maintainability, and ensures consistency in the login logic.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/3-remove-duplicate-login-endpoint

3. #### exceptions logs are missing:
 Integrated logging functionality into user routes to address the lack of exception logs. This ensures all exceptions are properly captured and recorded, enhancing traceability, debugging efficiency, and monitoring of user-related operations.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/11-exceptions-logs-are-missing-in-user_routes


4. #### Refactored jwt Service: 
The code was improved to enhance **readability**, **functionality**, and **maintainability**. Detailed **docstrings** were introduced to provide clear and thorough documentation. The `decode_token` function now incorporates error handling to safely address invalid tokens. Logical structures were streamlined for better clarity, and explicit algorithm definitions were added to bolster security. These updates ensure the code is more robust, user-friendly, and easier to maintain or expand.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/1-error-handling-issue-in-decode_token-so-refactoring-jwt_service

5. #### Added logging Functionality in email service:
The refactored code improves upon the original by introducing detailed logging and enhanced error handling to support better monitoring and debugging. Logs are implemented at critical points, such as during service initialization, email template rendering, and email dispatch, offering clear visibility into operations. Specific details, like email type and recipient, are logged to facilitate action tracking and issue diagnosis. Error handling has been reinforced with try-except blocks to capture and log failures during template rendering or email sending, providing clear and context-rich error messages. These enhancements make the service more dependable, maintainable, and transparent for developers.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/7-limited-error-handling-in-email_service-and-logging-functionality


6. #### Password Validation Constraints: 
The refactored code adds **password validation* to enforce strong security requirements, ensuring passwords contain uppercase, lowercase, special characters, and numbers. It also includes detailed logging for monitoring key operations and robust error handling to log and manage failures during email rendering or sending. These updates enhance security, reliability, and maintainability.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/9-complexity-requirements-such-as-uppercase-lowercase-special-char-for-password


7. #### Nickname Mismatch in User Creation:
Fixed Nickname Mismatch in User Creation: Addressed an issue where provided nicknames were being overwritten during user creation. Ensured valid and unique nicknames are utilized as-is, with new unique nicknames generated only when necessary. Enhanced logging to improve visibility into nickname conflicts.

link to the issue: https://github.com/Ahmed-2k1/event_manager/tree/13-nickname-mismatch-in-user-creation

Docker Image and Container Screenshot:
![alt text](<Screenshot 2024-12-06 at 3.20.35 AM.png>)
![alt text](<Screenshot 2024-12-06 at 3.20.57 AM.png>)

## Setup and Preliminary Steps

1. *Fork the Project Repository*: Fork the [project repository](https://github.com/kaw393939/event_manager) to your own GitHub account. This creates a copy of the repository under your account, allowing you to work on the project independently.

2. *Clone the Forked Repository*: Clone the forked repository to your local machine using the git clone command. This creates a local copy of the repository on your computer, enabling you to make changes and run the project locally.

3. *Verify the Project Setup*: Follow the steps in the instructor video to set up the project using [Docker](https://www.docker.com/). Docker allows you to package the application with all its dependencies into a standardized unit called a container. Verify that you can access the API documentation at http://localhost/docs and the database using [PGAdmin](https://www.pgadmin.org/) at http://localhost:5050.

## Testing and Database Management

1. *Explore the API*: Use the Swagger UI at http://localhost/docs to familiarize yourself with the API endpoints, request/response formats, and authentication mechanisms. Swagger UI provides an interactive interface to explore and test the API endpoints.

2. *Run Tests*: Execute the provided test suite using pytest, a popular testing framework for Python. Running tests ensures that the existing functionality of the API is working as expected. Note that running tests will drop the database tables, so you may need to manually drop the Alembic version table using PGAdmin and re-run migrations to ensure a clean state.

3. *Increase Test Coverage*: To enhance the reliability of the API, aim to increase the project's test coverage to 90%. Write additional tests for various scenarios and edge cases to ensure that the API handles different situations correctly.

## Collaborative Development Using Git

1. *Enable Issue Tracking*: Enable GitHub issues in your repository settings. [GitHub Issues](https://guides.github.com/features/issues/) is a powerful tool for tracking bugs, enhancements, and other tasks related to the project. It allows you to create, assign, and prioritize issues, facilitating effective collaboration among team members.

2. *Create Branches*: For each issue or task you work on, create a new branch with a descriptive name using the git checkout -b command. Branching allows you to work on different features or fixes independently without affecting the main codebase. It enables parallel development and helps maintain a stable main branch.

3. *Pull Requests and Code Reviews*: When you have completed work on an issue, create a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to merge your changes into the main branch. Pull requests provide an opportunity for code review, where your team members can examine your changes, provide feedback, and suggest improvements. Code reviews help maintain code quality, catch potential issues, and promote knowledge sharing among the team.

## Resources and Documentation

- *Instructor Videos and Important Links*:
 - [Introduction to REST API with Postgres](https://youtu.be/dgMCSND2FQw) - This video provides an overview of the REST API you'll be working with, including its structure, endpoints, and interaction with the PostgreSQL database.
 - [Assignment Instructions](https://youtu.be/TFblm7QrF6o) - Detailed instructions on your tasks, guiding you through the assignment step by step.
 - [Git Command Reference I created and some explanation for collaboration with git](git.md)
 - [Docker Commands and Running The Tests in the Application](docker.md)
 - Look at the code comments:
    - [Test Configuration and Fixtures](tests/conftest.py)
    - [API User Routes](app/routers/user_routes.py)
    - [API Oauth Routes - Connection to HTTP](app/routers/oauth.py)
    - [User Service - Business Logic - This implements whats called the service repository pattern](app/services/user_service.py)
    - [User Schema - Pydantic models](app/schemas/user_schemas.py)
    - [User Model - SQl Alchemy Model ](app/models/user_model.py)
    - [Alembic Migration - this is what runs to create the tables when you do alembic upgrade head](alembic/versions/628adcb2d60e_initial_migration.py)
    - See the tests folder for all the tests

 - API Documentation: http://localhost/docs - The Swagger UI documentation for the API, providing information on endpoints, request/response formats, and authentication.
 - Database Management: http://localhost:5050 - The PGAdmin interface for managing the PostgreSQL database, allowing you to view and manipulate the database tables.

- *Code Documentation*:
 The project codebase includes docstrings and comments explaining various concepts and functionalities. Take the time to read through the code and understand how different components work together. Pay attention to the structure of the code, the naming conventions used, and the purpose of each function or class. Understanding the existing codebase will help you write code that is consistent and integrates well with the project.

- *Additional Resources*:
 - [SQLAlchemy Library](https://www.sqlalchemy.org/) - SQLAlchemy is a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. It provides a set of tools for interacting with databases, including query building, database schema management, and data serialization. Familiarize yourself with SQLAlchemy's documentation to understand how it is used in the project for database operations.
 - [Pydantic Documentation](https://docs.pydantic.dev/latest/) - Pydantic is a data validation and settings management library for Python. It allows you to define data models with type annotations and provides automatic validation, serialization, and deserialization. Consult the Pydantic documentation to understand how it is used in the project for request/response validation and serialization.
 - [FastAPI Framework](https://fastapi.tiangolo.com/) - FastAPI is a modern, fast (high-performance) Python web framework for building APIs. It leverages Python's type hints and provides automatic API documentation, request/response validation, and easy integration with other libraries. Explore the FastAPI documentation to gain a deeper understanding of its features and how it is used in the project.
 - [Alembic Documentation](https://alembic.sqlalchemy.org/en/latest/index.html) - Alembic is a lightweight database migration tool for usage with SQLAlchemy. It allows you to define and manage database schema changes over time, ensuring that the database structure remains consistent across different environments. Refer to the Alembic documentation to learn how to create and apply database migrations in the project.

These resources will provide you with a solid foundation to understand the tools, technologies, and concepts used in the project. Don't hesitate to explore them further and consult the documentation whenever you encounter challenges or need clarification.

### Evaluation

This assignment offered a valuable opportunity to deepen technical skills in secure software development and system reliability. Implementing features such as password complexity enforcement—ensuring requirements like minimum length, special characters, and case sensitivity—highlighted the critical role of adhering to security best practices in user authentication. Enhancing the JWT service with structured error handling and explicit algorithm specifications significantly improved both robustness and security. Resolving issues such as duplicate login routes and nickname mismatches during user creation emphasized the importance of maintaining database integrity and designing efficient queries for consistency and scalability in multi-user environments.

The addition of detailed logging across key services, including user routes and email services, showcased the critical role of observability in modern applications. By implementing logging at crucial execution points and during exception handling, the system now provides enhanced traceability and simplifies debugging. Refactoring and modularizing components underscored the necessity of maintainable and extensible code, particularly in large, collaborative projects. Moreover, addressing database constraints for unique nicknames reinforced the importance of dynamic input validation to prevent runtime conflicts.

This assignment also bolstered understanding of collaborative development workflows, such as issue tracking, branching strategies, and version control best practices. Isolating changes for individual tasks and maintaining comprehensive documentation ensured the project remained consistent and scalable while adhering to established software development standards. Overall, this assignment provided practical experience in designing secure, maintainable, and reliable systems while tackling real-world development challenges effectively.