# Para Searcher Project

This is a Django project for searching paragraphs by word.

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- Docker (optional, if you want to run the project in a containerized environment)

### Installation Steps

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd para_searcher
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    Create a `.env` file in the project root and add the following variables:

    ```plaintext
    DATABASE_NAME=<your-database-name>
    DATABASE_USERNAME=<your-database-username>
    DATABASE_PASSWORD=<your-database-password>
    DATABASE_HOST=<your-database-host>
    DATABASE_PORT=<your-database-port>
    ```

    Replace `<your-database-name>`, `<your-database-username>`, `<your-database-password>`, `<your-database-host>`, and `<your-database-port>` with your actual database credentials.

### Running the Project

#### With Docker

1. Build the Docker image:

    ```bash
    docker-compose build
    ```

2. Run the Docker container:

    ```bash
    docker-compose up
    ```

3. Access the application at `http://localhost:8000`.

#### Without Docker

1. Migrate the database:

    ```bash
    python manage.py migrate
    ```

2. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

3. Access the application at `http://localhost:8000`.

### API Endpoints

- **Signup:** `/signup/` - POST request with email, name, and password in the request body.
- **Login:** `/login/` - POST request with email and password in the request body to get JWT tokens.
- **Refresh Token:** `/token/refresh/` - POST request with refresh token to get a new access token.
- **Create Paragraphs:** `/paragraphs/` - POST request with paragraphs data in the request body to create paragraphs and associated words.
- **Search Paragraphs:** `/search/?word=<search-word>` - GET request to search paragraphs by word.

# Para Searcher Project API Documentation

## Overview

This API documentation provides details on the endpoints available in the Para Searcher project.

### Base URL

The base URL for all API endpoints is: `http://localhost:8000`

## Authentication

- Authentication is required for some endpoints using JSON Web Tokens (JWT).
- To authenticate, obtain JWT tokens by sending a POST request to the `/login/` endpoint with valid credentials.
- Include the access token in the Authorization header for authenticated requests.

## Endpoints

### 1. User Signup

- **URL:** `/signup/`
- **Method:** POST
- **Authentication:** Not required
- **Request Body:**

    ```json
    {
        "email": "user@example.com",
        "name": "User Name",
        "password": "password"
    }
    ```

### 2. User Login

- **URL:** `/login/`
- **Method:** POST
- **Authentication:** Not required
- **Request Body:**

    ```json
    {
        "email": "user@example.com",
        "password": "password"
    }
    ```

- **Response:**

    ```json
    {
        "refresh": "refresh-token",
        "access": "access-token"
    }
    ```

### 3. Refresh Token

- **URL:** `/token/refresh/`
- **Method:** POST
- **Authentication:** Not required
- **Request Body:**

    ```json
    {
        "refresh_token": "refresh-token"
    }
    ```

- **Response:**

    ```json
    {
        "access_token": "new-access-token"
    }
    ```

### 4. Create Paragraphs

- **URL:** `/paragraphs/`
- **Method:** POST
- **Authentication:** Required
- **Request Body:**

    ```json
    {
        "paragraphs": "This is a sample paragraph.\n\nAnother paragraph."
    }
    ```

### 5. Search Paragraphs

- **URL:** `/search/?word=<search-word>`
- **Method:** GET
- **Authentication:** Required

Replace `<search-word>` with the word you want to search in the paragraphs.

## Error Handling

- Errors are returned with appropriate status codes and error messages in the response body.


