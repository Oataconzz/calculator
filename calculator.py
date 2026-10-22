def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    a=float(input("first number: "))
    b=float(input("second number: "))
    op=input("(+ - * /)")
    if op == "+":
        print("Result:", add(a, b))
    elif op == "-":
        print("Result:", sub(a, b))
    elif op == "*":
        print("Result:", mult(a, b))
    elif op == "/":
        print("Result:", div(a, b))
    else:
        print("Unknown operator:", op)