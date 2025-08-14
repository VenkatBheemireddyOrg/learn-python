import sys

def add(num1, num2)
    x = num1 + num2
    return x

def sub(num1, num2)
    y = num1 - num2
    return y

def mul(num1, num2)
    z = num1 * num2

num1 = sys.argv[1]
operator = sys.argv[2]
num2 = sys.argv[3]

if operator == "add":
    output = add(num1, num2)
    print(operator, output)


