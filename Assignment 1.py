

'''
Task: Implement a singly linked list class with the following methods:
append(data): Adds a new node with the specified data at the end of the list.
prepend(data): Adds a new node with the specified data at the beginning of the list.
print_list(): Prints all the elements in the list.
'''

# Create a class for handling your Node functionality
class Node:
    def __init__(self, data):
        # Store the data values inside the node
        self.data = data
        # This is the pointer to the next Node. It's currently set to None
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # the head of the list is empty currently
        self.head = None

    # Create append function below
    def append(self, data):
        #create a new node
        new_node = Node(data)

    # if the list is empty, the new node will become the head
        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

    # set the last node next pointer to the new node
        current.next = new_node


    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        # update the head to be the new node
        self.head = new_node

    def print_list(self):
        current = self.head
        while current:
                print(current.data)
                current = current.next


testing = SinglyLinkedList()
testing.append(10)
testing.append(20)
testing.append(30)
testing.prepend(5)
testing.print_list()


