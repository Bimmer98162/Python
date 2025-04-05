tp1 = (1, 2, 3, "a", "b", "c")
tp2 = (4,)
print(tp1 + tp2)
print(id(tp1 + tp2))
print(id(tp1))
tp1[2] = 4
print(tp1)