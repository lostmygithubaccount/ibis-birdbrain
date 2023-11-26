"""
Tasks in Ibis Birdbrain...
"""

# imports
from ibis_birdbrain.messages import Message


# classes
class Task:
    """Ibis Birdbrain task."""

    name: str
    function: str

    def __init__(self, name: str, function: str) -> None:
        self.name = name
        self.function = function

    def __call__(self, m: Message) -> Message:
        ...

    def __str__(self):
        return f"name: {self.name}\nfunction: {self.function}\n"

    def __repr__(self):
        return str(self)


class Tasks:
    """A collection of tasks."""

    tasks: dict[str, Task]

    def __init__(self, tasks: list[Task] = []) -> None:
        """Initialize the tasks."""
        self.tasks = {t.name: t for t in tasks}

    def __call__(self, m: Message) -> Message:
        """Run the tasks."""
        ...

    def add_task(self, task: Task):
        """Add a task to the collection."""
        self.tasks[task.name] = task

    def append(self, task: Task):
        """Add a task to the collection."""
        self.add_task(task)

    def __getitem__(self, id: str | int) -> Task:
        """Get a task from the collection."""
        if isinstance(id, int):
            return list(self.tasks.values())[id]
        return self.tasks[id]

    def __setitem__(self, name: str, task: Task) -> None:
        """Set a task in the collection."""
        self.tasks[name] = task

    def __len__(self) -> int:
        """Get the length of the collection."""
        return len(self.tasks)

    def __iter__(self):
        """Iterate over the collection."""
        return iter(self.tasks.keys())

    def __str__(self):
        return "\n".join([str(t) for t in self.tasks.values()])

    def __repr__(self):
        return str(self)


# exports
__all__ = ["Task", "Tasks"]
