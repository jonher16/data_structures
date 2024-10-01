import pytest

class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        
        if data == self.data:
            return
    
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinarySearchTreeNode(data)

        if data > self.data:
            
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def printTree(self, level=0, prefix="Root: "):

        # Print the current node's data formatted with indentation
        print(" " * (level * 4) + prefix + str(self.data))
        
        # Recursively print the left subtree, if it exists
        if self.left:
            self.left.printTree(level + 1, prefix="L--- ")
        
        # Recursively print the right subtree, if it exists
        if self.right:
            self.right.printTree(level + 1, prefix="R--- ")
    
    def inOrderTraversal(self):

        elements = []
        
        #Visit Left Tree
        if self.left:
            elements += self.left.inOrderTraversal()

        #Visit Root Node
        elements.append(self.data)

        #Visit Right Tree
        if self.right:
            elements += self.right.inOrderTraversal()
        
        return elements

    def preOrderTraversal(self):

        elements = []

        #Visit Root Node
        
        elements.append(self.data)

        #Visit Left Tree
        if self.left:
            elements += self.left.preOrderTraversal()

        #Visit Right Tree
        if self.right:
            elements += self.right.preOrderTraversal()
        
        return elements
    
    def postOrderTraversal(self):

        elements = []

        #Visit Left Tree
        if self.left:
            elements += self.left.postOrderTraversal()

        #Visit Right Tree
        if self.right:
            elements += self.right.postOrderTraversal()

        #Visit Root Node
        elements.append(self.data)
        
        return elements


    def find_min(self):

        if self.left:
            return self.left.find_min()
        else:
            return self.data
        
    def find_max(self):

        if self.right:
            return self.right.find_max()
        else:
            return self.data
        
    def calculate_sum(self):
        elements = self.inOrderTraversal()
        return sum(elements)
    
    def delete(self, data):
        if data < self.data:
            if self.left:
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete(data)
        else:
            if not self.left and not self.right:
                return None
            elif not self.left:
                return self.right
            elif not self.right:
                return self.left
            else:
                min_value_right = self.right.find_min()
                self.data = min_value_right
                self.right = self.right.delete(min_value_right)

        return self
            


            
        
    
def buildTree(elements):

    root = BinarySearchTreeNode(elements[0])
    for element in elements[1:]:
        root.addChild(element)
    return root

if __name__ == '__main__':

    numbers = [17, 4, 1, 20, 9, 23, 18 ,34]

    print(numbers)
    numbers_tree = buildTree(numbers)
    numbers_tree.printTree()

    print("In Order Traversal: ", numbers_tree.inOrderTraversal())
    print("Pre Order Traversal: ", numbers_tree.preOrderTraversal())
    print("Post Order Traversal: ", numbers_tree.postOrderTraversal())
    print("Min:", numbers_tree.find_min(), "Max:", numbers_tree.find_max(), "Sum:",numbers_tree.calculate_sum())


@pytest.fixture
def sample_bst():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    return buildTree(elements)

# Test: In-Order Traversal
def test_in_order_traversal(sample_bst):
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 23, 34]

# Test: Pre-Order Traversal
def test_pre_order_traversal(sample_bst):
    assert sample_bst.preOrderTraversal() == [17, 4, 1, 9, 20, 18, 23, 34]

# Test: Post-Order Traversal
def test_post_order_traversal(sample_bst):
    assert sample_bst.postOrderTraversal() == [1, 9, 4, 18, 34, 23, 20, 17]

# Test: Find Minimum Value
def test_find_min(sample_bst):
    assert sample_bst.find_min() == 1

# Test: Find Maximum Value
def test_find_max(sample_bst):
    assert sample_bst.find_max() == 34

# Test: Calculate Sum of All Nodes
def test_calculate_sum(sample_bst):
    assert sample_bst.calculate_sum() == 126

# Test: Adding a New Node
def test_add_node(sample_bst):
    sample_bst.addChild(15)  # Add a new node with value 15
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 15, 17, 18, 20, 23, 34]
    assert sample_bst.calculate_sum() == 141

# Test: Adding a Duplicate Node (Should Not Change Tree)
def test_add_duplicate_node(sample_bst):
    sample_bst.addChild(17)  # 17 is already in the tree
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 23, 34]
    assert sample_bst.calculate_sum() == 126  # Sum should not change

# Test: Building a Tree from a Single Element
def test_single_node_tree():
    tree = buildTree([42])
    assert tree.find_min() == 42
    assert tree.find_max() == 42
    assert tree.calculate_sum() == 42
    assert tree.inOrderTraversal() == [42]

# Test: Deleting a Leaf Node
def test_delete_leaf_node():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    sample_bst = buildTree(elements)
    sample_bst = sample_bst.delete(34)
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 23]
    assert sample_bst.find_max() == 23

# Test: Deleting a Node with One Child
def test_delete_node_with_one_child():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    sample_bst = buildTree(elements)
    sample_bst = sample_bst.delete(23)
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 34]
    assert sample_bst.find_max() == 34

# Test: Deleting a Node with Two Children
def test_delete_node_with_two_children():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    sample_bst = buildTree(elements)
    sample_bst = sample_bst.delete(20)
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 23, 34]
    assert sample_bst.calculate_sum() == 106  # Sum after deletion

# Test: Deleting the Root Node
def test_delete_root_node():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    sample_bst = buildTree(elements)
    sample_bst = sample_bst.delete(17)
    # The new root should be 18 (inorder successor)
    assert sample_bst.data == 18
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 18, 20, 23, 34]

# Test: Deleting Non-existent Node
def test_delete_nonexistent_node():
    elements = [17, 4, 1, 20, 9, 23, 18, 34]
    sample_bst = buildTree(elements)
    sample_bst = sample_bst.delete(999)
    # Tree should remain unchanged
    assert sample_bst.inOrderTraversal() == [1, 4, 9, 17, 18, 20, 23, 34]