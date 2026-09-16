# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to create a simple REST API using the FastAPI framework. In this assignment, you will build endpoints for creating, reading, and updating data while practicing request handling, JSON responses, and route design.

## 📝 Tasks

### 🛠️ Create a FastAPI App

#### Description
Set up a basic FastAPI application and make sure it starts correctly in a local Python environment. You will create the app structure and define your first route.

#### Requirements
Completed program should:

- Import and initialize a FastAPI app
- Define a root route that returns a welcome message
- Run the app locally using Uvicorn or FastAPI's development server
- Confirm the app returns JSON data in the browser or terminal

### 🛠️ Build a Resource API

#### Description
Create a small API for a simple resource such as books, students, or tasks. The API should support retrieving and creating items using HTTP methods.

#### Requirements
Completed program should:

- Define a route to list all items
- Define a route to create a new item
- Return JSON data for each item
- Store items in a simple in-memory list or dictionary
- Use meaningful endpoint names and response formats

### 🛠️ Add CRUD Functionality

#### Description
Expand the API so it can handle the main CRUD operations for your resource. This will help you practice working with HTTP methods and URL parameters.

#### Requirements
Completed program should:

- Add a route to retrieve one item by ID
- Add a route to update an existing item
- Add a route to delete an item
- Use path parameters or request bodies appropriately
- Return clear status codes such as 200, 201, and 404 when needed

### 🛠️ Validate Input and Improve the API

#### Description
Improve your application by validating incoming data and using better API design patterns. This step helps make the API more reliable and professional.

#### Requirements
Completed program should:

- Use Pydantic models to validate request data
- Ensure required fields are enforced
- Return helpful error responses for invalid input
- Keep the code organized with clear function names and a readable structure
