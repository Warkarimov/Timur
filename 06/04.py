pupils = set()
one_language_pupils = set()
m = int(input())
n = int(input())
for i in range(n + m):
    second_name = input()
    if second_name in pupils:
        one_language_pupils.add(second_name)
        pupils.discard(second_name)
    else:
        pupils.add(second_name)
if len(pupils) == 0:
        print('NO')
else:
    print(len(pupils))

