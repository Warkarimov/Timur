n = int(input())
count = 0
for j in range(1, n + 1):
    num = n % j
    if num == 0:
        print(str(j), '', end = '')
        count += j
else:
    if count == (n + 1):
        print('\nПростое')
    else:
        print('\nНет')

