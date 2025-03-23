#  🏎️ Nexu Backend Test 💥
This project aims to create a backend API for managing vehicle brands and models. The API exposes various routes to interact with vehicle data, including adding, updating, and fetching brands and models. It integrates with a PostgreSQL database to persist the data.

## Technologies Used
- FastAPI: A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- Uvicorn: An ASGI server used to serve the FastAPI application.
- SQLAlchemy: ORM to interact with the PostgreSQL database.
- Pydantic: Data validation and settings management using Python type annotations.
- Psycopg2-binary: PostgreSQL database adapter for Python.
- Python-dotenv: To load environment variables from a .env file.
- Commitizen: A tool to standardize commit messages.
- PostgreSQL: Relational database used for storing vehicle brands and models.

## Routes
### GET /brands
List all brands along with their average price.

Example response:
```bash
   [
      {"id": 1, "name": "Acura", "average_price": 702109},
      {"id": 2, "name": "Audi", "average_price": 630759},
      {"id": 3, "name": "Bentley", "average_price": 3342575},
      {"id": 4, "name": "BMW", "average_price": 858702}
    ]
 ```
### GET /brands/:id/models
List all models of a specific brand.

Example response:
```bash
   [
      {"id": 1, "name": "ILX", "average_price": 303176},
      {"id": 2, "name": "MDX", "average_price": 448193}
    ]
 ```
### POST /brands/:id/models
Add a new model to an existing brand. Model names must be unique within a brand.

Example request:
```bash
  {"name": "Toyota"}
 ```

### POST /brands/:id/models
Add a new model to an existing brand. Model names must be unique within a brand.

Example request:
```bash
   {"name": "Prius", "average_price": 406400}
 ```

### PUT /models/:id
Update the average price of a model.

Example request:
```bash
   {"average_price": 406400}
 ```

### GET /models?greater=&lower=
List models within a specified price range.

Example request:
```bash
   GET /models?greater=380000&lower=400000
 ```
## Overview
You just got hired to join the *cool* engineering team at *Nexu*! The first story in your sprint backlog is to build a backend application for an already existing frontend. The frontend needs the next routes:


```
                              GET    /brands
                              GET    /brands/:id/models
                              POST   /brands
                              POST   /brands/:id/models
                              PUT    /models/:id
                              GET    /models
```

#### GET /brands

List all brands 
```json
[
  {"id": 1, "nombre": "Acura", "average_price": 702109},
  {"id": 2, "nombre": "Audi", "average_price": 630759},
  {"id": 3, "nombre": "Bentley", "average_price": 3342575},
  {"id": 4, "nombre": "BMW", "average_price": 858702},
  {"id": 5, "nombre": "Buick", "average_price": 290371},
  "..."
]
```
The average price of each brand is the average of its models average prices

#### GET /brands/:id/models

List all models of the brand
```json
[
  {"id": 1, "name": "ILX", "average_price": 303176},
  {"id": 2, "name": "MDX", "average_price": 448193},
  {"id": 1264, "name": "NSX", "average_price": 3818225},
  {"id": 3, "name": "RDX", "average_price": 395753},
  {"id": 354, "name": "RL", "average_price": 239050}
]
```

#### POST /brands

You may add new brands. A brand name must be unique.

```json
{"name": "Toyota"}
```

If a brand name is already in use return a response code and error message reflecting it.


#### POST /brands/:id/models

You may add new models to a brand. A model name must be unique inside a brand.

```json
{"name": "Prius", "average_price": 406400}
```
If the brand id doesn't exist return a response code and error message reflecting it.

If the model name already exists for that brand return a response code and error message reflecting it.

Average price is optional, if supply it must be greater than 100,000.


#### PUT /models/:id

You may edit the average price of a model.

```json
{"average_price": 406400}
```
The average_price must be greater then 100,000.

#### GET /models?greater=&lower=

List all models. 
If greater param is included show all models with average_price greater than the param
If lower param is included show all models with average_price lower than the param
```
# /models?greater=380000&lower=400000
```
```json
[
  {"id": 1264, "name": "NSX", "average_price": 3818225},
  {"id": 3, "name": "RDX", "average_price": 395753}
]
```

## Usage with Makefile
The project includes a Makefile to simplify development tasks. Here are the available commands:

### Available Commands
- make help: Display this list of commands.
- make create-venv: Create a virtual environment with Python 3.11.
- make install: Install all necessary dependencies.
- make test: Run the tests.
- make run: Start the service and all related services (such as a DB) in Docker.
- make down: Stops all running services.
- make clean: Stops and removes all associated containers and resources.
- make clear: Clean temporary files.

### Detailed Command Breakdown
- make create-venv: Creates a virtual environment using Python 3.11.
- make pip: Installs pip in the virtual environment.
- make install: Installs all dependencies listed in requirements.txt after creating the virtual environment.
- make test-requirements: Ensures all dependencies are installed correctly and starts the server.
- make build: Builds the Docker image.
- make up: Starts the Docker containers for the application and services (e.g., PostgreSQL).
- make down: Stops the Docker containers.
- make rebuild: Stops, removes, and rebuilds the Docker containers from scratch.

To use these commands, you can run make <command>. For example:
```json
  make install
  make run
```

## Issues Encountered
- Database Connection: Initially, I encountered issues connecting to the PostgreSQL container in Docker due to incorrect hostnames and database configurations. I had to debug and adjust the environment variables to ensure proper connection.

- Data Import: There was difficulty importing the models.json file, especially given its large size (677 objects). The process of loading the data into the database wasn't as smooth as expected, and I couldn't complete the CRUD operations within the given time frame.

## What I Would Have Done With More Time
- Error Handling: I would improve the error handling for duplicate brands/models, and ensure more specific error messages are returned for better debugging.

- Data Validation: I would add more thorough validation for model data (e.g., checking that the average_price is a positive integer).

- Performance Improvements: For handling large datasets, I would optimize database queries and consider pagination for the GET /models route to prevent loading too many records at once.

- Frontend Integration: If given more time, I would integrate this backend with a frontend to visualize the brands and models, making it easier to interact with the data.

- Unit Test Development: I would develop more comprehensive unit tests for the API endpoints and services to ensure all business logic is thoroughly tested. This includes writing tests for:

  - Successful creation and update of brands and models.
  - Validation checks, such as ensuring the uniqueness of brands and models.
  - Edge cases like invalid or missing data, and ensuring proper error handling.
  - Testing the performance of endpoints for handling large datasets.
  - Using mock data for simulating database interactions and testing the API in isolation.



## New Ideas for Future Work
- Filtering and Searching: Add more filtering options for models, such as filtering by brand, price range, or other attributes like engine type or year of manufacture.

- User Authentication: Implement user authentication for adding or modifying brands/models, allowing for role-based access control (e.g., admin users).

- Advanced Pricing Insights: Implement analytics endpoints that provide insights like the average price by brand or trends over time.


