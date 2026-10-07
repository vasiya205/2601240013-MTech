from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):

    def __init__(self) -> None:
        self.items: list[T] = []

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def front(self) -> T:
        if not self.items:
            raise IndexError("Queue is empty")
        return self.items[0]
