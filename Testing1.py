

'''

Implement a recursive function to calculate the factorial of a non-negative integer.
Instructions:
Write a recursive function      factorial(n) that returns the factorial of the non-negative integer      n.
The factorial of      n (denoted as      n!) is defined as:
n! = n * (n-1)! for n > 0
0! = 1
Write test cases to verify the function works correctly for different values of      n.

'''

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

print("Factorial is, ", factorial(0))


'''
What is the time complexity of the Quick Sort algorithm, and how would you implement it in Python?
Give an example
'''

def quicksort(array):
    # I want to check if the loist is already sorted
    if len(array) <= 1:
        return array

    leader = array[len(array) // 2]
    left = [x for x in array if x < leader]
    middle = [x for x in array if x == leader]
    right = [x for x in array if x > leader]

    return quicksort(left) + middle + quicksort(right)

numbers = [10,7,8,9,1,5]
sorted_list = quicksort(numbers)

print("Sorted list: ", sorted_list)