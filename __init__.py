import copy
a = {'a': 1, 'b': {'c': [1,2]}}

b = copy.copy(a)

b['b']['c'].append(3)

print(a, b)