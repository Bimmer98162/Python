def length(lst : list):
    leng = 0
    for i in lst:
        leng += 1
    return leng

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(length(lst))