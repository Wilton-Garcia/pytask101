from fastapi import FastAPI

app = FastAPI()

TASKS = [
    {
        "id":1,
        "name":"task 1",
        "description":"This is a task",
        "status":"not done"
    },
     {
        "id":2,
        "name":"task 2",
        "description":"This is other task",
        "status":"not done"
    },
     {
        "id":3,
        "name":"task 2",
        "description":"This is the third task",
        "status":"not done"
    }
]

@app.get("/tasks")
def list():
    return TASKS