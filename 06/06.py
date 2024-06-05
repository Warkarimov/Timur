n = int(input())
m = int(input())
home_books = set()
school_books = set()
for i in range(n):
    name = input()
    home_books.add(name)
for i in range(m):
    name = input()
    if name in home_books:
        print('Yes')
    else:
        print('No')