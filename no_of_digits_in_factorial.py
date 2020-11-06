from math import factorial

result = []
num_factorial = int(input('Enter the number: '))
factorial_result = factorial(num_factorial)

for num in str(factorial_result):
    result.append(num)

len_factorial = len(result)
print(f'There are {len_factorial} digits in the factorial of {num_factorial}')
