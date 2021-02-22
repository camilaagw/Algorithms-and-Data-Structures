"""Implement a Queue using just Stacks (a popular question)."""

import pytest


class Stack:
    """Wrapper around a list object"""

    def __init__(self):
        self._list = list()

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception('Calling pop on empty stack')
        return self._list.pop()

    def isEmpty(self):
        return not self._list


class Queue:
    """Queue implemented with stacks"""

    def __init__(self):
        self.output = Stack()
        self.input = Stack()

    def enqueue(self, value):
        self.input.push(value)

    def dequeue(self):
        if self.isEmpty():
            raise Exception('Calling pop on empty queue')

        if self.output.isEmpty():
            while not self.input.isEmpty():
                self.output.push(
                    self.input.pop()
                )
        return self.output.pop()

    def isEmpty(self):
        return self.output.isEmpty() and self.input.isEmpty()


if __name__ == "__main__":
    my_queue = Queue()
    assert my_queue.isEmpty()

    # Test simple enqueue, dequeue
    for val in [42, "42"]:
        my_queue.enqueue(val)
        assert my_queue.dequeue() == val

    # Test  enqueue -> dequeue-enqueue -> dequeue
    values = [1, 2, 3, 4, 5, 6]
    for val in values:
        my_queue.enqueue(val)  # Enqueue
    for val in values:
        assert my_queue.dequeue() == val  # Dequeue
        my_queue.enqueue(val * 10)  # Enqueue
    for val in values:
        assert my_queue.dequeue() == val * 10  # Dequeue

    assert my_queue.isEmpty()

    with pytest.raises(Exception):
        my_queue.dequeue()
