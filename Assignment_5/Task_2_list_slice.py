# Task 2: Demonstrate List Slicing

numbers = list(range(1, 11))

print("Original list", numbers)

first_five = numbers[:5]
reversed_list = first_five[::-1]

print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)