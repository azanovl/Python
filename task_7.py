from math import factorial

def fact(n):
    for i in range(n+1):
        yield  factorial(i)

n = 0
for i in fact(int(input("Введите чило для определения факториала: "))):
    if n > 0:
         print(f"{n}! = {i}")
    n += 1