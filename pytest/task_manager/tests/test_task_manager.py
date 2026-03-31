import pytest


def test_add_task(task_manager):
    task = task_manager.add_task("Learn pytest")
    assert task.title == "Learn pytest"
    assert not task.completed


def test_add_empty_task(task_manager):
    with pytest.raises(ValueError):
        task_manager.add_task("")


def test_complete_task(task_manager):
    task_manager.add_task("Task 1")
    task_manager.complete_task(0)

    assert task_manager.tasks[0].completed is True


def test_complete_invalid_index(task_manager):
    with pytest.raises(IndexError):
        task_manager.complete_task(10)


def test_delete_task(task_manager):
    task_manager.add_task("Task 1")
    task_manager.delete_task(0)

    assert len(task_manager.tasks) == 0


def test_get_completed_tasks(task_manager):
    task_manager.add_task("Task 1")
    task_manager.add_task("Task 2")

    task_manager.complete_task(1)

    completed = task_manager.get_completed_tasks()

    assert len(completed) == 1
    assert completed[0].title == "Task 2"