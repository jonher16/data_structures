import pytest

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printTree(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.printTree()

    def getLevel(self):
        level = 0
        while self.parent:
            level += 1
            self = self.parent
        return level
    
def build_product_tree():

    root = TreeNode('Electronics')

    laptop = TreeNode('Laptop')
    laptop.addChild(TreeNode('Mac'))
    laptop.addChild(TreeNode('Surface'))
    laptop.addChild(TreeNode('Thinkpad'))

    smartphone = TreeNode('Smartphone')
    smartphone.addChild(TreeNode('iPhone'))
    smartphone.addChild(TreeNode('Samsung S Series'))
    smartphone.addChild(TreeNode('Google Pixel'))

    tablet = TreeNode('Tablet')
    tablet.addChild(TreeNode('iPad'))
    tablet.addChild(TreeNode('Samsung Galaxy Tab'))
    tablet.addChild(TreeNode('Lenovo Tab'))


    root.addChild(laptop)
    root.addChild(smartphone)
    root.addChild(tablet)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    root.printTree()
    

@pytest.fixture
def test_TreeNode_initialization():
    node = TreeNode('root')
    assert node.data == 'root'
    assert node.children == []
    assert node.parent is None

def test_TreeNode_addChild():
    parent = TreeNode('parent')
    child = TreeNode('child')
    parent.addChild(child)
    assert child.parent == parent
    assert child in parent.children

def test_TreeNode_getLevel():
    root = TreeNode('root')
    child1 = TreeNode('child1')
    child2 = TreeNode('child2')
    grandchild = TreeNode('grandchild')

    root.addChild(child1)
    child1.addChild(child2)
    child2.addChild(grandchild)

    assert root.getLevel() == 0
    assert child1.getLevel() == 1
    assert child2.getLevel() == 2
    assert grandchild.getLevel() == 3

def test_build_product_tree_structure():
    root = build_product_tree()

    # Test root node
    assert root.data == 'Electronics'
    assert len(root.children) == 3
    assert [child.data for child in root.children] == ['Laptop', 'Smartphone', 'Tablet']

    # Test Laptop subtree
    laptop = root.children[0]
    assert laptop.data == 'Laptop'
    assert len(laptop.children) == 3
    assert [child.data for child in laptop.children] == ['Mac', 'Surface', 'Thinkpad']

    # Test Smartphone subtree
    smartphone = root.children[1]
    assert smartphone.data == 'Smartphone'
    assert len(smartphone.children) == 3
    assert [child.data for child in smartphone.children] == ['iPhone', 'Samsung S Series', 'Google Pixel']

    # Test Tablet subtree
    tablet = root.children[2]
    assert tablet.data == 'Tablet'
    assert len(tablet.children) == 3
    assert [child.data for child in tablet.children] == ['iPad', 'Samsung Galaxy Tab', 'Lenovo Tab']