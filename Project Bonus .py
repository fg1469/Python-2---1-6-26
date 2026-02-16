
'''
Build a program that manages student records using a linked list. The user can add, search, delete, or display student information.
Students will implement a singly linked list where each node stores a student’s ID, name, and grade. The program should allow various operations using decision structures (menu-driven)
Steps:
Define a Student node structure/class with fields: ID, Name, Grade, and next.
Create a menu using if-else or switch statements:
1. Add Student
2. Search Student by ID
3. Delete Student
4. Display All Students
5. Exit
Implement each function:
Add: Insert a new node at the end.
Search: Traverse and check if the ID matches.
Delete: Adjust pointers to remove a node.
Display: Print all records.
Loop until the user chooses Exit.

=========================================================================================================
'''

# Node class for each student
class Node:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None


# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Add Student - (insert at end)
    def add(self, student_id, name, grade):
        new_node = Node(student_id, name, grade)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    # 2. Search Student by ID
    def search(self, student_id):
        current = self.head

        while current:
            if current.student_id == student_id:
                return current
            current = current.next

        return None

    # 3. Delete Student
    def delete(self, student_id):
        current = self.head
        previous = None

        while current:
            if current.student_id == student_id:
                # If deleting head
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    # 4. Display All Students
    def display(self):
        if self.head is None:
            print("No items found .")
            return

        current = self.head
        while current:
            print(f"Student ID: {current.student_id}, Name: {current.name}, Grade: {current.grade}")
            current = current.next


# Menu-driven program
def main():
    educational_records = LinkedList()

    while True:
        print("\n===== Educational Records System =====")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input(" (User) Choose(s) : ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")

            educational_records.add(student_id, name, grade)
            print("Student added successfully.")

        elif choice == "2":
            student_id = input("Enter & Search Student by ID : ")
            student = educational_records.search(student_id)

            if student:
                print(f" ID matches: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
            else:
                print("Student not found.")

        elif choice == "3":
            student_id = input("Enter Student ID to delete: ")
            if educational_records.delete(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            print("\nStudent Records:")
            educational_records.display()

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please try again.")


# Run program
if __name__ == "__main__":
    main()
