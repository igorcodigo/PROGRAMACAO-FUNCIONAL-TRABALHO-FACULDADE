def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(x, y):
    return x * y

def define_operation(fn, a, b):
    return fn(a, b)

result_addition = define_operation(addition, 10, 2)
print(result_addition)

result_subtraction = define_operation(subtraction, 10, 2)
print(result_subtraction)

result_multiplication = define_operation(multiplication, 10, 2)
print(result_multiplication)
