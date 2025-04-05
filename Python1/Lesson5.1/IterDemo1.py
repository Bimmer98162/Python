my_dict = {"a" : 1, "b" : 2, "c" : 3}
key_iterator = iter(my_dict.keys())
next_key = next(key_iterator)
print(next_key)

item_iterator = iter(my_dict.items())
next_item = next(item_iterator)
print(next_item)

zip_iterator = zip(my_dict.values(), my_dict.keys())
next_zip = next(zip_iterator)
print(next_zip)