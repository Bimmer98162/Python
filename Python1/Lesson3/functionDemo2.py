#写一个函数，接收一个列表作为参数，在函数内部对列表进行修改，不会影响到原始列表
def new_list(lst):

    return lst + ["new list"]

o_lst = [1, 2, 3]
new_lst = new_list(o_lst)
print(o_lst)
print(new_lst)