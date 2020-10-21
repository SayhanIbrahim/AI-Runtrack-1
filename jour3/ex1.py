example_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
list1 = []
for i, k in enumerate(example_dict):
    print(i, k)
for i, (k, v) in enumerate(example_dict.items()):
    mult = k * v
    list1.append(mult)
print(list1)
