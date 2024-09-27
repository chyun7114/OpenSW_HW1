def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "can't divided by 0"

    return a / b

x = int(input("Input the first number : "))
y = int(input("Input the second number : "))

print(f'add two numbers : {add(x, y)}')
print(f'substract two numbers : {sub(x, y)}')
print(f'multiply two numbers : {mul(x, y)}')
print(f'divide two numbers : {div(x, y)}')