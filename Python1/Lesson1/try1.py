import math
r = 5
v = 4/3 * math.pi * r**3
print(v)

cover = 24.95
discount = cover * 0.6
first = 3
extra = 0.75
num = 60
book_cost = discount * num
shipping = first + (num - 1) * extra
total = book_cost + shipping
print(total)

