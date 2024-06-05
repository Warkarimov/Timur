english = set()
deutsch = set()
m = int(input())
n = int(input())
for i in range(n):
    second_name = input()
    english.add(second_name)
for i in range(m):
    second_name1 = input()
    deutsch.add(second_name1)
if english ^ deutsch:
    print(len(english ^ deutsch))
else:
    print('NO')