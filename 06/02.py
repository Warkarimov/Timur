n = int(input())
cities = set()
for i in range(1, n + 1):
    city = input()
    if city in cities:
        print('Try Another')
        break
    else:
        cities.add(city)
else:
    print('OK')
