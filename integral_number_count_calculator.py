while True:
    result = []
    N = int(input('Enter integral number: '))
    if N % 2 == 1:
        print('Yes')
    else:
        print('No')

    for element in str(N):
        result.append(element)

    no_of_digits = len(result)
    print(f'There are {no_of_digits} digit(s) in the integral number {N}')
