# Q1. What is the syntax for adding an element to a list in Python?
l1 = [56,78,12]
l1.append(45)
print(l1)  

# Q2. What is the difference between remove() and pop() functions in Python?
# remove use to delet a first occurance of specific value
l2 = [1, 4,2, 4, 3]
l2.remove(4)
print(l2) 


# The pop() function is used to remove and return an element from a specific index in a list

l3 = [1, 2, 3]
removed_element = l3.pop()
print(l3)   

# Q3. Write a Python code to sort a list in descending order.
l4 = [1,45,12,78,56,32,13,80,54,33]
l4.sort(reverse=True)
print(l4)

# Q4. Write a Python code to count the number of occurrences of an element in a list.
l5 = [1,2,3,1,5,1,6,8,1,7,1]
print(l5.count(1))


# Q5. Write a Python code to reverse a list.
l6 = [1,72,3,14,25,6,7]
print(l6[::-1])