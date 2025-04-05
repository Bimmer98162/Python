lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
lst2.append(7)
#lst2.append(lst1)
#print(lst1)
#print(lst2)
print(id(lst1))
print(id(lst2))


#遍历
for item in lst1:
    print(item)

