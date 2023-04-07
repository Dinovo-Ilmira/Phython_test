# health = int(input('Enter your range health: '))
# if health <= 0:
#     print('False')
# else:
#     print('True')

# num = int(input('Enter your number: '))
# if num%2:
#     print('Even number')
# else:
#     print('Odd number')

# num = int(input('Enter your number: '))
# if num%2 == 0:
#     print('Even number')
# else:
#     print('Odd number')

# year = int(input())
# if year%4 == 0:
#     if year%100 == 0:
#         if year%400 == 0:
#             print('Високосный')
#         else:
#             print('Невисокосный')
#     else:
#         print('Високосный')
# else:
#     print('Невисокосный')

# year = int(input('Enter year: '))
# if not year%4 and year%100 or not year%400:
#     print('Високосный')
# else:
#     print('Невисокосный')




# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# i = 1
# while i <= num:
#     print(text)
#     i += 1


# text = input("Enter your text: ")
# num = int(input('Enter the number of repetitions: '))
# for i in range(1, num+1):
#     print(i, text)




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
# result = eval(f'{num1} {operator} {num2}')
# if num2 == 0 and operator == '/':
#    try:
#          result = num1/num2
#          print(f'Result = {result}')
#    except ZeroDivisionError:
#          print('На ноль делить нельзя!')
# else:
#     print(f'{num1} {operator} {num2} = {result}')

# num1 = int(input('Пожалуйста, введите первое число: '))
#     num2 = int(input('Пожалуйста, введите второе число: '))
# except ValueError as e:
#     print(f'Введенное значение не является числом: {e}')
#     sys.exit()
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# if operator not in '+-*/%':
#     print("Вы ввели не правильный оператор!")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print("Делить на ноль нельзя!")
# else:
#     result = eval(f'{num1} {operator} {num2}')
#     print(f'{num1} {operator} {num2} = {result}')


#  num1 = int(input('Пожалуйста, введите первое число: '))
#     num2 = int(input('Пожалуйста, введите второе число: '))
# except ValueError as e:
#     print(f'Введенное значение не является числом: {e}')
#     sys.exit()
# operator = input('Пожалуйста, введите один из следующих операторов - \'+\', \'-\', \'/\', \'*\', \'%\': ')
# if operator not in '+-*/%':
#     print("Вы ввели не правильный оператор!")
#     sys.exit()
# result = 0
# if num2 == 0 and operator == '/':
#     try:
#         result = num1 / num2
#     except ZeroDivisionError:
#         print('На ноль делить нельзя!')
#         sys.exit()
# elif operator == '+':
#     result = num1 + num2
# elif operator == '*':
#     result = num1 * num2
# elif operator == '-':
#     result = num1 - num2
# elif operator == '%':
#     result = num1 % num2
# else:
#     result = num1/num2
# print(f'{num1} {operator} {num2} = {result}')
#













