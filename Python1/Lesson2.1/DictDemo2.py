import copy
dict1 = {1 : ["python", "java"], 2 : "name"}
dict2 = dict1
dict3 = dict1.copy()
dict4 = copy.deepcopy(dict1)
print(id(dict1[1]))
print(id(dict2))
print(id(dict3[1]))
print(id(dict4))
