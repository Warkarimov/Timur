pupils = set()
tree_language_pupils = set()
two_language_pupils = set()
m = int(input())
n = int(input())
k = int(input())
for i in range(n + m + k):
    second_name = input()
    if second_name in two_language_pupils:
        tree_language_pupils.add(second_name)
        two_language_pupils.discard(second_name)
    elif second_name in pupils:
        two_language_pupils.add(second_name)
        pupils.discard(second_name)
    else:
        pupils.add(second_name)
if two_language_pupils:
    print(len(two_language_pupils))
else:
    print('NO')