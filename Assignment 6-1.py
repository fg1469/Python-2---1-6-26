

'''
Problem: Reverse a Singly Linked List using Recursion - Choose your own list and reverse it recursively
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

    def remove(self, data):

        def remove(self, data):

            previous = None
            current = self.head

            while current:

                # Node found
                if current.data == data:

                    # To remove head
                    if previous is None:
                        self.head = current.next
                    else:
                        previous.next = current.next

                    return  # stop after first omission

                previous = current
                current = current.next

    def print_list(self):
        current = self.head
        while current:
                print(current.data)
                current = current.next

    def reverse_list(self):
        def zoomer(current, prev):
            if not current:
                return prev

            next_node = current.next
            current.next = prev

            return zoomer(next_node, current)

        self.head = zoomer(self.head, None)


# ---------------- TESTING ----------------

testing = SinglyLinkedList()

testing.append(10)
testing.append(20)
testing.append(30)
testing.prepend(5)

print("Prior to removal: ")
testing.print_list()

testing.remove(20)

print("Post-removal: ")
testing.print_list()

testing.reverse_list()
testing.print_list()