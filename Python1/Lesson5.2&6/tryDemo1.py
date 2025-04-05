try:
    try:
        print(a)
        print(5/0)
    except NameError:
        print("NameError")

except:
    print("不能除0")