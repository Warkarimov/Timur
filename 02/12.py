s = input()
a = len(s)
if a < 3:
    print(str(a * 40) + 'коп.')
elif a < 25:
    sum = str(int(a * 40))
    print(sum[0] + 'руб.' + sum[1] + sum[2] + 'коп.')
elif a < 250:
    sum = str(int(a * 40))
    print(sum[0] + sum[1] + 'руб.' + sum[2] + sum[3] + 'коп.')
elif a < 2500:
    sum = str(int(a * 40))
    print(sum[0] + sum[1] + sum[2] + 'руб.' + sum[3] + sum[4] + 'коп.')
elif a < 25000:
    sum = str(int(a * 40))
    print(sum[0] + sum[1] + sum[2] + sum[3] + 'руб.' + sum[4] + sum[5] + 'коп.')
else:
    print('0 руб.')