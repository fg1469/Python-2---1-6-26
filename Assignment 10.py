


'''
Implement a basic binary tree and include methods for in-order, pre-order, and post-order traversal.
Instructions:
Implement a class Node that represents a node in the binary tree.
Implement a class BinaryTree that supports inserting nodes and three types of traversal methods: in-order, pre-order, and post-order.
Write test cases to verify the implementation.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# It is suggested to implement recursion to facilitate the process
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)

        else:
            self.recursion_insertion(self.root, value)

    def recursion_insertion(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self.recursion_insertion(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self.recursion_insertion(current.right, value)

    def inorder(self, node, result):
        if node:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)

    def preorder(self, node, result):
        if node:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

    def postorder(self, node, result):
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)


        tree = BinaryTree()
        list1 = [50,30,70,20,40,60,80]

        for t in list1:
            tree.insert(t)

        inorder_list = []
        tree.inorder(tree.root, inorder_list)
        print("Inorder List is:", inorder_list)

