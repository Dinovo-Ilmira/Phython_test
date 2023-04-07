# print('Hello world!')
# print('Hello world!')
# print('Hello world!')
import sys

# name = input()
# print(f'Hello {name}')
#
# age = int(input())
# name = input()
# print(f'Hello, I am {name}. I am {age} years old')

# print(1,2,3, sep='!', end='?')

# num1 = 10
# num2 = 5
# print(num1+num2)
# print(num1-num2)
# print(num1*num2)
# print(num1**num2)
# print(num1/num2)
# print(num1//num2)
# print(num1%num2)

# print(0.1+0.1+0.1)

# a = [1, 4, 6, 10, 33]
# for i in a:
#     if i % 2 == 0:
#         print(i, end=' ')

# a = [1, 4, 6, 10, 33]
# for i in a:
#     if i % 2 != 0:
#         print(i, end=' ')

# a = [1, 4, 6, 10, 33]
# for i in a:
#     if i % 2 != 0:
#         print(i, end='/')

# print("'Hello world!'")
#
# print('"Hello world!"')

# print(2*(2+5))
# print(3*2**2)
# print(6/2*3)
# print(2+3-5)
# print(2-1+6)

# print(abs(-7))
# print(min(4,8,11))
# print(max(5,8,15))
# print(pow(2,3))
# print(round(3.5))
# print(round(3.445))
# print(round(3.445, 2))

# a = 15
# b = 10
# a += b
# print(a)

# c = 20
# e = 15
# # c -=e
# # c *=e
# # c /=e
# print(c)

# text = 'Hello world!'
# text1 = "Hello world!"
# text2 = """Hello world
# 123
# My"""
# print(text2)

# text3 = input()
# print(text3)

# name = 'Ilmira'
# lastname = 'Dinovo'
# balance = 50
# print('Dear, Ilmira Dinovo your banc account 50 $')

# print('Hello'*5)

# name = input('Enter your name: ')
# lastname = input('Enter you lastname: ')
# balance = int(input('Enter your balance: '))
# print(f'Hello, {name} {lastname}, your banc account balance: {balance}')

# text = 'Hello world!'
# print(len(text))

# text = 'Hello world!'
# print(len(text))
# print('e' in text)
# print('a' in text)

# text = 'Hello world'
# print(text[len(text)-1])

# compare = 3 == 3
# print(compare)
#
# compare = 3 == 4
# print(compare)
#
# compare = 3 != 4
# print(compare)

# compare = 3 != 3
# print(compare)
#
# compare = 3 > 4
# print(compare)
#
# compare = 3 < 4
# print(compare)
#
# compare = 3 <= 4
# print(compare)

# x = 5
# print(x>3 and x<8)
# print(x>3 and x>8)
# print(x>3 or x<8)
# print(x>3 or x>8)
# print(x>3 and not x<8)
# print(x>3 and not x>8)

# if x == 5:
#     print('Five')
# else:
#     print('Not five')

# if 'x' == 5:
#     print('Five')
# else:
#     print('Not five')
#

# if x != 5:
#     print('Five')
# else:
#     print('Not five')
#

# x = 5
# if x == 5:
#     print('Five')
# else:
#     print('Not five')
#
# x = 5
# if x != 5:
#     print('Five')
# else:
#     print('Not five')


# x = 6
# if x == 5:
#     print('Correct')
# else:
#     print('Incorrect')
#
# x = 6
# if x != 5:
#     print('Correct')
# else:
#     print('Incorrect')

# num = 5
# if num == 5:
#     print('Five')
# elif num > 5:
#     print('More than five')
# else:
#     print('Less than five')
#
# num = 6
# if num == 5:
#     print('Five')
# elif num > 5:
#     print('More than five')
# else:
#     print('Less than five')
#
# num = 3
# if num == 5:
#     print('Five')
# elif num > 5:
#     print('More than five')
# else:
#     print('Less than five')


# age = int(input('Please, enter your age: '))
# if age >= 18:
#     print('Welcome!')
# else:
#     print('Go home,baby!')

# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# result = num1 / num2
# print(f'Result = {result}')

# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# if num2 == 0 and operator == '/':
#    try:
#          result = num1/num2
#          print(f'Result = {result}')
#    except ZeroDivisionError:
#          print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# num1 = int(input('Number 1: '))
# num2 = int(input('Number 2: '))
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#    try:
#          result = num1/num2
#          print(f'Result = {result}')
#    except ZeroDivisionError:
#          print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# num1 = 0
# num2 = 0
# try:
#     num1 = int(input('Number 1: '))
#     num2 = int(input('Number 2: '))
# except ValueError:
#     print('You enter not a number!')
#     sys.exit()
# operator = input('Operator: ')
# if (num2 == 0 and operator == '/') or num1 > 5:
#    try:
#          result = num1/num2
#          print(f'Result = {result}')
#    except ZeroDivisionError:
#          print('На ноль делить нельзя!')
# else:
#     result = num1 * num2
#     print(f'Result = {result}')

# num = 0
# while num < 5:
#     print(num)
#     num = num + 1
# #     # num += 1

# num = 0
# while num <= 5:
#     print(num)
#     num = num + 1

# message = 'Hello'
# i = 1
# while i < 6:
#       print(i, message)
#       if i == 3:
#           break
#       i += 1

# message = 'Hello'
# i = 0
# while i < 6:
#       i += 1
#       if i == 3:
#           continue
#       print(i, message)

# for i in range(6):
#     print(i)

# for i in range(1, 6):
#     print(i)
#
# for i in range(1, 6, 3):
#     print(i)

# for i in 'Hello':
#     print(i)

# for i in 'Hello':
#     print(i)

# message = 'Hello'
# print(message[0: 5: 2])

# start = 5
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# def num():
#     return 2 * 2
# start = num()
# stop = 15
# step = 3
# for i in range(start, stop, step):
#     print(i)

# i = 0
# x = 0
# while i < 4:
#     x +=i
#     i +=1
#     print(x)
#
# i = 0
# x = 0
# while i < 4:
#     print(i)
#     x +=i
#     i +=1
#     print(f'x = {x}, i = {i}')
#
# message = 'Hello'
# if message:
#     print(message)
# else:
#     print('The string is empty')

# message = ''
# if message:
#     print(message)
# else:
#     print('The string is empty')

# num = 5
# if num%2 !=0:
#     print('Нечетное')
# else:
#     print('Четное')

# num = 4
# if num % 2:
#     print('Нечетное')
# else:
#     print('Четное')

# def num(num1, num2):
#     return num1 - num2
#
# # print(num(10,5))
# # print(num(9,7))
#
# start = num(8, 5)
# stop = 15
# step = 3
# for i in range (start, stop, step):
#     print(i)























