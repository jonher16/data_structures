import pytest
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        itr = self.head
        for _ in range(index):
            itr = itr.next
        return itr.data

    def addAtHead(self, val):
        new_node = Node(val, self.head)
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1

    def addAtTail(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node = Node(val, prev.next)
            prev.next = new_node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1

# Test Cases for MyLinkedList Class
@pytest.fixture
def linked_list():
    """Fixture to initialize a new linked list before each test."""
    return MyLinkedList()

def test_add_at_head(linked_list):
    linked_list.addAtHead(1)
    assert linked_list.get(0) == 1  # The head should be 1

    linked_list.addAtHead(2)
    assert linked_list.get(0) == 2  # The new head should be 2
    assert linked_list.get(1) == 1  # The next element should be 1

def test_add_at_tail(linked_list):
    linked_list.addAtTail(1)
    assert linked_list.get(0) == 1  # The head should be 1

    linked_list.addAtTail(2)
    assert linked_list.get(1) == 2  # The tail should be 2

def test_get_element_by_index(linked_list):
    linked_list.addAtHead(10)
    linked_list.addAtTail(20)
    linked_list.addAtTail(30)
    assert linked_list.get(0) == 10  # Get the first element
    assert linked_list.get(1) == 20  # Get the second element
    assert linked_list.get(2) == 30  # Get the third element
    assert linked_list.get(3) == -1  # Index out of range should return -1

def test_add_at_specific_index(linked_list):
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)  # Insert 2 at index 1
    assert linked_list.get(0) == 1  # The head should still be 1
    assert linked_list.get(1) == 2  # The new value at index 1 should be 2
    assert linked_list.get(2) == 3  # The value at index 2 should be 3

    linked_list.addAtIndex(0, 0)  # Insert 0 at index 0 (new head)
    assert linked_list.get(0) == 0  # The head should now be 0
    assert linked_list.size == 4  # The size should be updated correctly

def test_delete_at_specific_index(linked_list):
    linked_list.addAtHead(1)
    linked_list.addAtTail(2)
    linked_list.addAtTail(3)
    linked_list.addAtTail(4)

    linked_list.deleteAtIndex(2)  # Delete element at index 2 (value 3)
    assert linked_list.get(2) == 4  # Now, the third element should be 4
    assert linked_list.size == 3  # The size should be updated correctly

    linked_list.deleteAtIndex(0)  # Delete the head
    assert linked_list.get(0) == 2  # The new head should be 2
    assert linked_list.size == 2  # The size should be updated correctly

    linked_list.deleteAtIndex(1)  # Delete the tail
    assert linked_list.tail.data == 2  # The new tail should be 2
    assert linked_list.size == 1  # The size should be updated correctly

def test_edge_cases(linked_list):
    assert linked_list.get(0) == -1  # Getting from an empty list should return -1
    linked_list.deleteAtIndex(0)  # Deleting from an empty list should do nothing

    linked_list.addAtIndex(1, 10)  # Adding at invalid index should do nothing
    assert linked_list.size == 0  # The list size should still be 0