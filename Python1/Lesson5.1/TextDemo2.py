my_list = [1,2,3,4,5]
iterator = iter(my_list)
for item in iterator:
    print(item)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break