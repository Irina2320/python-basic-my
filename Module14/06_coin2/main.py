import math

print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
s = math.sqrt(x**2 + y**2)
if s <= float(input('Введите радиус: ')):
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
print('Дистанция до монетки:', round(s, 3),"метров")
