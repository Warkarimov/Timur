money = int(input())
while True:
    money = int(money / 8)
    if money < 8:
        print(money)
        break
    else:
        continue