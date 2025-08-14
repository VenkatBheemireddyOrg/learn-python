import sys

def add(num1, num2):
    x = num1 + num2
    return x

def sub(num1, num2):
    y = num1 - num2
    return y

def mul(num1, num2):
    z = num1 * num2
    return z

num1 = int(sys.argv[1])    #by default arguments will be taken as string, so
operator = sys.argv[2]     #convert to integer
num2 = int(sys.argv[3])

if operator == "add":
    output = add(num1, num2)
    print(operator, output)


if operator == "sub":
    output = sub(num1, num2)
    print(operator, output)

if operator == "mul":
    output = mul(num1, num2)
    print(operator, output)


