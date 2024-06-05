nums_1 = set()
nums_2 = set()
space = False
space_count = 0
while True:
    num = input()
    if not num:
        space_count += 1
        space = True
        if space_count > 1:
            break
        else:
            continue
    if space:
        nums_2.add(num)
    else:
        nums_1.add(num)
if nums_1 & nums_2:
    print(nums_1 & nums_2)
else:
    print('Empty')
