#有一个已经按从小到大排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
x = int(input("x= "))
lst = [2, 8, 17, 46, 58]
i = 0
while x > lst[i] and i < len(lst):
    i += 1
lst.insert(i, x)
print(lst)