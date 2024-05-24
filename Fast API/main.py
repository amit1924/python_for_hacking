# Importing necessary modules
from fastapi import (
    FastAPI,
    HTTPException,
)  # Importing FastAPI class for creating the application and HTTPException for handling HTTP errors
from pydantic import BaseModel  # Importing BaseModel for defining Pydantic models
from typing import List, Optional  # Importing List and Optional for defining type hints
from uuid import (
    UUID,
    uuid4,
)  # Importing UUID for handling UUIDs and uuid4 for generating UUIDs

# Creating an instance of FastAPI
app = FastAPI()


# Defining a Pydantic model for Task
class Task(BaseModel):
    id: Optional[UUID] = (
        None  # Optional UUID field for the task ID, initialized to None
    )
    title: str  # Required string field for the task title
    description: Optional[str] = (
        None  # Optional string field for the task description, initialized to None
    )
    completed: bool = (
        False  # Boolean field indicating whether the task is completed, initialized to False
    )


# Initializing an empty list to store tasks
tasks = []


# Endpoint to create a new task
@app.post(
    "/tasks", response_model=Task
)  # Defines a POST endpoint at "/tasks" with Task as the response model
def create_task(
    task: Task,
):  # Defines a function to handle POST requests to create tasks
    task.id = uuid4()  # Generates a unique UUID for the task
    tasks.append(task)  # Adds the created task to the list of tasks
    return task  # Returns the created task as the response


# Endpoint to retrieve all tasks
@app.get(
    "/tasks/", response_model=List[Task]
)  # Defines a GET endpoint at "/tasks" with List[Task] as the response model
def read_tasks():  # Defines a function to handle GET requests to retrieve all tasks
    return tasks  # Returns the list of tasks as the response


# Endpoint to retrieve a specific task by its ID
@app.get(
    "/tasks/{task_id}", response_model=Task
)  # Defines a GET endpoint at "/tasks/{task_id}" with Task as the response model
def read_task(
    task_id: UUID,
):

    # Defines a function to handle GET requests to retrieve a specific task by ID
    for task in tasks:  # Iterates through the list of tasks
        if task.id == task_id:  # Checks if the task ID matches the requested task ID
            return task  # Returns the task if found
    raise HTTPException(
        status_code=404, detail="Task not found"
    )  # Raises an HTTPException with status code 404 if task not found


# Endpoint to update a specific task by its ID
@app.put(
    "/tasks/{task_id}", response_model=Task
)  # Defines a PUT endpoint at "/tasks/{task_id}" with Task as the response model
def update_task(
    task_id: UUID, task_update: Task
):  # Defines a function to handle PUT requests to update a specific task by ID
    for idx, task in enumerate(tasks):  # Iterates through the list of tasks with index
        if task.id == task_id:  # Checks if the task ID matches the requested task ID
            updated_task = task.copy(
                update=task_update.dict(exclude_unset=True)
            )  # Copies the task and updates it with the provided data
            tasks[idx] = updated_task  # Updates the task in the list of tasks
            return updated_task  # Returns the updated task as the response
    raise HTTPException(
        status_code=404, detail="Task not found"
    )  # Raises an HTTPException with status code 404 if task not found


# Endpoint to delete a specific task by its ID
@app.delete(
    "/tasks/{task_id}", response_model=Task
)  # Defines a DELETE endpoint at "/tasks/{task_id}" with Task as the response model
def delete_task(
    task_id: UUID,
):  # Defines a function to handle DELETE requests to delete a specific task by ID
    for idx, task in enumerate(tasks):  # Iterates through the list of tasks with index
        if task.id == task_id:  # Checks if the task ID matches the requested task ID
            del tasks[idx]  # Deletes the task from the list of tasks
            return task  # Returns the deleted task as the response
    raise HTTPException(
        status_code=404, detail="Task not found"
    )  # Raises an HTTPException with status code 404 if task not found


# Running the FastAPI application using uvicorn
if __name__ == "__main__":
    import uvicorn  # Importing uvicorn for running the FastAPI application

    uvicorn.run(app, host="0.0.0.0", port=8000)  # Starts the FastAPI application server
