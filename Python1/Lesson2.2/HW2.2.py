num = []
n = 0
for a in [1, 2, 3, 4]:
    for b in [1, 2, 3, 4]:
        for c in [1, 2, 3, 4]:
            if a != b and b != c and a != c:
                num.append(a * 100 + b * 10 + c)
                n +=1
print(num)
print(f"有 {n} 个不相同且无重复的三位数")