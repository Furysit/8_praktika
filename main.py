print("HEllo, it's a simple calculator")
a = int(input("Please enter A:"))
b = int(input("Please enter B:"))

c = input("Please enter what you want to do (+,-,*,/):")

def summa(a,b):
    return a+b
def minus(a,b):
    return a-b
def umnozh(a,b):
    return a*b
def delenie(a,b):
    return a/b


if c == '+':
    otvet =summa(a,b)
elif c == '-':
    otvet =minus(a,b)
elif c == '*':
    otvet =umnozh(a,b)
elif c == '/':
    otvet = delenie(a,b)

print(otvet)