def multi(Int):
    if Int > 1:
        return multi(Int - 1) * Int
    else:
        return 1


dic = [multi(i) for i in range(0, 10)]
print(dic)
# record = open('text', 'wt')
for i in range(10, 2540160):
    Sum = 0
    # print('{:7}'.format(i), end='', file=record)
    for every in str(i):
        # print(' {} '.format(every), end='', file=record)
        Sum += dic[int(every)]
    # print(file=record)
    if Sum == i:
        print('{:7}'.format(i))
