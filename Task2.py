import math
import sys

print("Введіть коефіцієнти")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if(a==0):
    print("Лінйне рівняння")
    sys.exit(0)
if(b==0):
    res = (c/a)**0.5
    print("Результат 1: " + str(res))
    print("Результат 2: " + str(res*(-1)))
    sys.exit(0)
if (a == 0 and b == 0):
    print('Бескінечність')
    sys.exit(0)

discr = b ** 2 - 4 * a * c
print("Дискримінант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Коренів немає")