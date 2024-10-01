from collections import deque
import pytest

class Stack:
    def __init__(self):
        self.stack = deque()

    def add(self, data):
        self.stack.append(data)

    def get(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty. No value to remove.")
    
    def isEmpty(self):
        return not self.stack
    
    def count(self):
        return len(self.stack)
    
    def printStack(self):
        print(self.stack)


class Queue:
    def __init__(self, max_size=None):
        self.buffer = deque()
        self.max_size = max_size

    def add(self,data):
        if self.count() == self.max_size:
            print("Max size reached. Cannot enqueue.")
        else:
            self.buffer.appendleft(data)
    
    def get(self):
        if self.buffer:
            return self.buffer.pop()
        else:
            print("Queue is empty. No value to remove.")

    def isEmpty(self):
        return not self.buffer
    
    def isFull(self):
        return self.count() == self.max_size
    
    def count(self):
        return len(self.buffer)
    
    def printQueue(self):
        print(self.buffer)


def test_stack_add():
    stack = Stack()
    stack.add(10)
    stack.add(20)
    stack.add(30)
    assert stack.count() == 3
    assert stack.get() == 30
    assert stack.get() == 20
    assert stack.get() == 10
    assert stack.isEmpty() == True

def test_stack_get_empty():
    stack = Stack()
    result = stack.get()
    assert result is None  # As there is a print statement in `get` function when stack is empty
    assert stack.isEmpty() == True

def test_stack_isEmpty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack.add(1)
    assert stack.isEmpty() == False

def test_stack_count():
    stack = Stack()
    stack.add(1)
    stack.add(2)
    stack.add(3)
    assert stack.count() == 3
    stack.get()
    assert stack.count() == 2

def test_queue_add():
    queue = Queue()
    queue.add(10)
    queue.add(20)
    queue.add(30)
    assert queue.count() == 3
    assert queue.get() == 10
    assert queue.get() == 20
    assert queue.get() == 30
    assert queue.isEmpty() == True

def test_queue_get_empty():
    queue = Queue()
    result = queue.get()
    assert result is None  # As there is a print statement in `get` function when queue is empty
    assert queue.isEmpty() == True

def test_queue_isEmpty():
    queue = Queue()
    assert queue.isEmpty() == True
    queue.add(1)
    assert queue.isEmpty() == False

def test_queue_isFull():
    queue = Queue(max_size=2)
    assert queue.isFull() == False
    queue.add(1)
    queue.add(2)
    assert queue.isFull() == True
    queue.get()
    assert queue.isFull() == False

@pytest.fixture
def test_queue_count():
    queue = Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)
    assert queue.count() == 3
    queue.get()
    assert queue.count() == 2

def test_queue_max_size():
    queue = Queue(max_size=2)
    queue.add(1)
    queue.add(2)
    queue.add(3)  # Should not add because max_size is 2
    assert queue.count() == 2