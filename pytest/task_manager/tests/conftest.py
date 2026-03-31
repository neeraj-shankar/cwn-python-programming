import pytest
from app.task_manager import TaskManager

@pytest.fixture
def task_manager():
    return TaskManager()