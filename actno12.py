def calculator(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


sum_add, sum_sub = calculator(5, 5)
print("addition:", sum_add)
print("subtraction:", sum_sub)
