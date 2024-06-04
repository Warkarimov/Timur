n = int(input())
total = 0
for i in range(1,n + 1):
    iq = int(input())
    total += iq
    iq_s = total / i
    if iq > iq_s:
        print('>')
    elif iq < iq_s:
        print('<')
    else:
        print('0')