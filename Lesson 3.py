# my_list = [1, 'hello', 2,0, True, None, 1, 1]
#
# sentence = 'Python is awesome!'
# print(sentence.split(' ', maxsplit=1))


# print(my_list[0])
# print(my_list[-1])

# print('before', my_list)
# print(id(my_list))
#
# my_list[0] = 25
# print(my_list)
# print(id(my_list))


# my_list.append(sentence)
# print(my_list)
# print(len(my_list))
#
# my_list.insert(0,sentence)
# print(my_list)
# print(len(my_list))

# print(my_list.count(1))

# print(my_list.index(None))

#
# my_list.insert(0,sentence)
# print(my_list)
# print(len(my_list))
# print(my_list.count(1))
# print(my_list.index(1))


# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))
# print(min(my_list))
# print(max(my_list))


# my_list1 = [1, 2, 3, 4, 5, [1, 2, 3, 4, 5, [1, 2]]]
# # print(sum(my_list))
# # print(min(my_list))
# # print(max(my_list))
# # print(my_list1[-1][1])
# print(my_list1[-1][-1][0])
# my_list1.reverse()
# print(my_list1)
# #
# numbers = [1, 2, 3, 4, 5]
# # for num in numbers:
# #     print(num**2)
# new_l = [i*i for i in numbers if i%2]
# print(new_l)
# # #
# new_l = [i*i for i in numbers if i%2==0]
# print(new_l)
#
# new_l = [i for i in numbers if i%2]
# print(new_l)

# my_tuple = 1, 2, 3
# print(my_tuple)
# print(type(my_tuple))

# my_tuple = (1, True, 'name', None, 'name', 'name', 25 )
# print(my_tuple)
#
# name = 'Mark',
# print(name)
# print(type(name))

# name = ('Mark'),
# print(name)
# print(type(name))

# name = ('Mark')
# print(name)
# print(type(name))

# my_tuple = ('apple', 'banana', 'cat')
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)
#
# my_tuple[0] = 'ananas'
# print(my_tuple)

# letters = list(my_tuple)
# letters[0] = 'ananas'
# print(letters)

# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# print(my_tuple.index('name'))
# print(my_tuple.count('name'))
#

# my_tuple = (1, True, 'name', None, 'name', 'name', 25)
# result = tuple([item for item in my_tuple if isinstance(item,int)])
# print(result)
#
# print(f'sum is: {sum(result)}')
# print(f'min is: {min(result)}')
# print(f'max is: {max(result)}')
# print(f'length of my_tuple is: {len(my_tuple)}')
# print(f'length of result is: {len(result)}')

# for (index, item) in enumerate(my_tuple):
#     print(index, item)

# i = 0
# while i < len(my_tuple):
#     print(i, my_tuple[i])
#     i+=1

# fruits = ('apple', ['ananas', 'mango'], 'melon')
# fruits[1][0] = 'cherry'
# print(fruits)


# a = 5
# b = 10
# a, b = b, a
# print(f'a = {a}')
# print(f'b = {b}')

# def sum_it(*args):
#     total = 0
#     print(args)
#     for num in args:
#         total = total + num
#     return total
# print(sum_it(4, 5, 10, 6, 20))
# print(sum_it(4, 5, 10, 6, 20, 4, 5, 10, 6, 20))

# def func(*args):
#     l = []
#     print(len(args))
#     for item in args:
#         l.append(item*item)
#     return l
# print(func(2, 5, 6, 8, 10))

# my_dict = {}
# print(type(my_dict))

# my_dict = {
#     'Name': 'Emma',
#     'Last_name': 'Dinovo',
#     'age': '30',
#     'Department': 'IT'
# }

# print(my_dict)
# print(id(my_dict))
# print(my_dict['Name'])
# print(my_dict['Last_name'])

# print(my_dict.age)

# my_dict['Last_name'] = 'Dinov'
# print(my_dict)
# print(id(my_dict))

# my_dict['salary'] = 5000
# print(my_dict)
#
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict.pop('salary'))
# print(my_dict)
# print(my_dict.get('salary', 'Not found'))

# keys = ['name', 'salary', 'department']
# values = ['Alex', '5000', 'IT']
# employee = dict(zip(keys, values))
# print(employee)

# employee1 = dict(name='Jon', salary='5000', department='IT')
# print(employee1)

# my_list = [1, 2, 3, 4, 5, 8, 9, 9, 9, 8, 8, 5, 1]
# print(set(my_list))

set1 = {1, 2, 3, 'one', 'ten', 6}
set2 = {1, 2, 3, 'one', 'ten', 100, 525}
# set3 = {1, 2, 3}

print(set1.issubset(set2))
print(set2.issuperset(set1))
print(set2.intersection(set1))
print(set2.difference(set1))
print(set1.symmetric_difference(set2))

# print(set1)
# print(id(set1))
# print(set1.remove(1))
# print(set1)
# print(id(set1))
# print(set1.add(8))
# print(set1)
# print(id(set1))

# fs = frozenset({1, 2, 3})
# print(fs)
# fs.remove(1)
# print(fs)

# fs.add(4)
# print(fs)
































