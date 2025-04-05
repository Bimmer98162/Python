#1，2，3，4能组成多少个不相同且无重复的三位数？并打印出来
n = 0
for i in range(100, 999, 1):
    a = i // 100
    b1 = i % 100
    b = b1 // 10
    c = i % 10
    if 1 <= a <= 4 and 1 <= b <= 4 and 1 <= c <= 4 and a != b and b != c and a != c:
        n += 1
        print(i)
print(f"有 {n} 个不相同且无重复的三位数")