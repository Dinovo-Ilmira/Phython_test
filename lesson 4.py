# def calc(a,b=1):
#     return a*b
# print(calc(b=5, a=4))

# def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old.'
# print(person(25, 'Anna', 'Smith'))
#
# print(person('Anna', 'Smith', 25))
#
# print(person(f_name='Anna', l_name='Smith', age=25))

# def person(age, f_name, l_name):
#     return f'Hello, my name is {f_name} {l_name}. I am {age} years old.'

# def pattern (lenth, char1, char2):
#     return (char1+char2) * lenth + char1
# print(pattern(8, '*', '-'))
#
# mult = lambda x, y: x*y
# print(mult(5, 6))
#
# mult = lambda x, y: x+y
# print(mult(5, 6))
#
# mult = lambda x, y: x-y
# print(mult(5, 6))


# l = [20, 'str', 5, 6, 'yes', 18, 19, 25, 22, 24, 'banana', 'apple', 40.5, 58.6]
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2 ==0, l))
# print(filtered)
# filtered = list(filter(lambda x: isinstance(x, int) and x % 2, l))
# print(filtered)
# print(*filtered)
# filtered = list(filter(lambda x: isinstance(x, float), l))
# print(filtered)

# filtered = list(filter(lambda x: isinstance(x, float) or isinstance(x,str), l))
# print(filtered)

# filtered = list(filter(lambda x: not isinstance(x, str), l))
# print(filtered)

l_1 = [1, 5, 6, 12, 16]
# l = [20, 'str', 5, 6, 'yes', 18, 19, 25, 22, 24, 'banana', 'apple', 40.5, 58.6]
# # filtered = list(filter(lambda x: isinstance(x, int) and x % 2 ==0, l))
# # print(filtered)
# power = list(map(lambda x: x**2 if isinstance(x, int) else x, l))
# print(power)

# power = list(map(lambda x: x**2, l_1))
#
# from functools import reduce
# result = reduce(lambda x, y: x - y, l_1)
# print(result)
#
# result = reduce(lambda x, y: x * y, l_1)
# print(result)
#
# def say_hello(name):
#     print(f'Hello {name}')
#
# def my_decorator(func):
#     def wrapper():
#         print('I am wrapper!')
#         func()
#         print('Wrapped')
#     return wrapper
#
# @my_decorator
# def say_hello(name):
#     print(f'Hello {name}')
#
# # say_hello('Sam')
# # say_hello = my_decorator(say_hello)
# # say_hello()
#
# def milk(func):
#     def wrapper():
#         print('hot milk')
#         func()
#     return wrapper
#
# def sugar(func):
#     def wrapper():
#         print('sugar')
#         func()
#     return wrapper
# @sugar
# @milk
# def coffee():
#     print('coffee')
# coffee()
#
# import time
#
# print(time.time())
# print(time.)

# import datetime
# print(datetime.date.today())
#
# bdate = 1988
# current_date = datetime.date.today()
# age = current_date.year - bdate
# current_month = current_date.month
# print(age)
# print(current_month)

import math

# import math as m
# print(m.prod(l_1))
#
# import modul
# print(modul.hello('sam'))
#
# from modul

# def sum(a, b)
#     from modul import54


























































