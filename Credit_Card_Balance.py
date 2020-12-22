import math
print('Welcome to the Quadroot calculator')
a = int(input('Enter the value for a: '))
b = int(input('Enter the value for b: '))
c = int(input('Enter the value for c: '))
discriminant = b**2 - 4 * a * c
if discriminant < 0:
    print('ERROR! The quadratic function has complex roots.')
elif discriminant > 0:
    y = int((-b + math.sqrt(discriminant)) / 2 * a)
    z = int((-b - math.sqrt(discriminant)) / 2 * a)
    print('The quadratic function has two(2) distinct roots.')
    print('The roots are: ')
    print(y, ',', z)
    print('Therefore: x:x =', y, ',', z)
else:
    y = int((-b + math.sqrt(discriminant)) / 2 * a)
    z = int((-b - math.sqrt(discriminant)) / 2 * a)
    print('The quadratic function has two(2) equal roots.')
    print('The roots are: ')
    print(y, ',', z)
    print('Therefore: x:x =', y, ',', z)
