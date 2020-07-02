from operator import itemgetter
a = [1,2,3,4]
print(itemgetter(0, 1)(a))


a = [1,[2,3],4,5]
print(itemgetter(0, 1)(a))

a = {'a': 1, 'b': 2}
print(itemgetter('a', 'b')(a))
