x = float(input("x : "))
if x > 1:
    y = 3 * x - 5
    print(y)
elif -1 < x < 1:
    y = x + 2
    print(y)
elif x < -1:
    y = 5 * x + 3
    print(y)

s = int(input("s: "))
if s >= 90:
    print("Harvard")
elif 75<= s <=89:
    print("Cambridge")
elif 60 <= s <= 65:
    print("UCL")