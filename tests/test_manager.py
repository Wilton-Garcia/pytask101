from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
from task_manager.manager import app, TASKS

def test_when_return_should_be_200():
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.status_code == HTTP_200_OK

def test_should_return_json_format():
    client = TestClient(app)
    response = client.get("/tasks")
    assert response.headers["Content-Type"] == "application/json"

def test_when_task_list_should_return_a_list():
    client = TestClient(app)
    response = client.get("/tasks")
    assert isinstance(response.json(), list)

def test_when_list_task_a_task_should_have_id():
    TASKS.append({"id": 1})
    client = TestClient(app)
    response = client.get("/tasks")
    assert "id" in response.json().pop()
    TASKS.clear()

def test_when_list_task_a_task_should_have_name():
    TASKS.append({"name":"name one"})
    client = TestClient(app)
    response = client.get("/tasks")
    assert "name" in response.json().pop();
    TASKS.clear()

def test_task_when_list_task_a_task_should_have_description():
    TASKS.append({"description": "this is a task"})
    client = TestClient(app)
    response = client.get("/tasks")
    assert "description" in response.json().pop()
    TASKS.clear()

def test_task_when_list_task_a_task_should_have_status():
    TASKS.append({"status":"done"})
    client = TestClient(app)
    response = client.get("/tasks")
    assert "status" in response.json().pop()