
l=[ ]

for i in range(101,200):
    for j in range(2,i-1):
        if i % j==0:
            break
    else:                  #for......else 中，else语句会在 for 不通过 break 跳出而中断的情况下执行。
        l.append(i)
print(l)
print('总数为:%d'%len(l))