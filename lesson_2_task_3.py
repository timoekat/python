
def area (a):
    square = a*a
    return square

a = float(input("Введите сторону квадрата: "))
if a != int(a):
    a = int(a) + 1  
else:
    a = int(a)

result = area(a)

print(result)

