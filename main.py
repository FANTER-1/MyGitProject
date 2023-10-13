# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#print (0.1+0.1*5-0.3*4)

#print ((3.14+0.3)

# a = -13
# b = 7
# e = (a - b)

# print ((31%2) + (-31 % 2))

# pi = 3.14159
# print (round(pi**2/2))

# Входные данные:
# numbers = '1 2 3 4 5 6 7'
# numbers_split = numbers.split(" ")
# numbers_joined = ' /n '.join(numbers_split)
# print(numbers_joined)
# Вывод программы:
# numbers = '1 2 3 4 5 6 7'
# print(numbers.split(' ')[::])
# print(numbers.split(' ')[1])
# print(numbers.split(' ')[2])
# print(numbers.split(' ')[3])
# print(numbers.split(' ')[4])
# print(numbers.split(' ')[5])
# print(numbers.split(' ')[6])

# numbers = '1 2 3 4 5 6 7'
# a = numbers.split( )
# for item in a:
#     print(item)

# pi = 31.4159265
# print ("%.4e" % (pi))

# hours = 1
# minutes = 2
# second = 3
# print("%02d:%02d:%02d" % (hours, minutes, second))

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[ 1 : 4 ])

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[ : : 3 ])

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[ -4 : : -1 ])

# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[ -1 : 3 : -1 ])

# L = ['3.3', '4.4', '5.5', '6.6']
# print(map(float, L))

# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split()
# list_of_numbers = list(map(int, list_of_strings))
#
# print(sum(list_of_numbers[::3]))

# L = list(map(float, input().split()))
# L[0], L[-1] = L[0], L[-1]
# L.append(sum(L))
#
# print(L)

# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))

# text = input("Введите текст")
# unique = list(set(text))
# print("Количество уникальных символов: ", len(unique))

# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set = set(b) # используем множественное присваивание
# b_set = set(a)
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)

# str1 = input("Введите первую строку")
# str2 = input("Введите вторую строку")
# split1 = str1.split()
# split2 = str2.split()
# set1 = set(str1)
# set2 = set(str2)
# symm_diff = set1.symmetric_difference(set2)

# text_1 = input("Введите первый текст")
# text_2 = input("Введите второй текст")
# set_text_1 = set(text_1.split())
# set_text_2 = set(text_2.split())
# print(text_1)
# print(text_2)
# set_text_1_2 = list(map(int, set_text_1.symmetric_difference(set_text_2)))
# set_text_1_2.sort()
# print(set_text_1_2)

# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))

# a = 5
# b = 3+2
#
# print(id(a) - id(b))

# shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
# list_id_before = id(shopping_center[-1])
#
# shopping_center[-1].append("Uniqlo")
# list_id_after = id(shopping_center[-1])
#
# print(list_id_before == list_id_after)

# x = 2000 ; x = 1900
# def is_leap_year(x):
#     return (x % 400 == 0) or (( x % 4 == 0) and ( x % 100 != 0))
# print((is_leap_year(x = 2000)))

# '3' in str(N) and '7' in str(N)

# s = 5
# a = 10
# if a > 0:
#    s = s + a
# else:
#    s = s - a
#
# print(s)

# mx = 0
# s: int = 0
# x = int(input())
# if x < 0:
#     s = x
#
# b = 7
# b /= b
#
# if x > mx:
#      mx = x
#
# print(s)
# print(mx)

# def are_both_odd(A, B):
#     return A % 2 == 1 and B % 2 == 1
# print(are_both_odd(A = 2, B = 4))

# if x > 0:
#     if y > 0:               # x > 0, y > 0
#          print("Первая четверть")
#     else:                   # x > 0, y < 0
#          print("Четвертая четверть")
# else:
#     if y > 0:               # x < 0, y > 0
#          print("Вторая четверть")
#     else:                   # x < 0, y < 0
#          print("Третья четверть")
# if x > 0 and y > 0:
#     print("Первая четверть")
# if x > 0 and y < 0:
#     print("Четвертая четверть")
# if x < 0 and y > 0:
#     print("Вторая четверть")
# if x < 0 and y < 0:
#     print("Третья четверть")

# def get_wind_class(speed): #объявление функции
#     if 1 <= speed <= 4: #только аргумент
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return"strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# print(get_wind_class(3)) #мы просим программу напечатать то, что в скобках

# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     username = 'user'
#     password = 'password'
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
#     print(check_user(username='user', password='password'))

# A = int(input('Введите первое число\n'))
# B = int(input('Введите второе число\n'))
# C = int(input('Введите третье число\n'))
#
# if ((A < 45) and (B >= 45) and (C >=45)) or \
#     ((A >= 45) and (B < 45) and (C >=45)) or \
#     ((A >= 45) and (B >= 45) and (C < 45)):
#     print('Есть число меньше 45 и только одно')
# else:
#     print('Числа меньше 45 нет или их несколько')

# A = int(input('Введите число\n'))
#
# if not (-10 <= A <= -1 or 2 <= A <= 15):
#     print("Число не принадлежит интервалу")
# else:
#     print("Число принадлежит интервалу")

# n = 15
# first_digit = n // 10
# second_digit = n % 10
#
# print((first_digit == 5) or (second_digit == 5))

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# print(len(list_) == len(set(list_)))

# num = 12345678
#
# print(str(num) == str(num)[::-1])

# P = 1
# N = 5
#
# for i in range(1, N+1):
#     P *= i
#
# print(P)

# N = 12
# for i in range(1 , N + 1):
#     print('*' * i)

# n = 1
# while n**2 < 1000:
#     n += 1
# print("Искомое число", n - 1)

# n = 1
# while True:
#     if n**2 >= 1000:
#         print("Искомое число", n - 1)
#         break
#     n += 1

# random_matrix = [
#    [9, 2, 1],
#    [2, 5, 3],
#    [4, 8, 5]
# ]
#
# min_value_rows = []
# min_index_rows = []
# max_value_rows = []
# max_index_rows = []
#
# for row in random_matrix:
#     min_index = 0
#     min_value = row[min_index]
#     max_index = 0
#     max_value = row[max_index]
#
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print("Минимальные элементы:", min_value_rows)
# print("Их индексы:", min_index_rows)
# print("Максимальные элементы:", max_value_rows)
# print("Их индексы:", max_index_rows)

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# for i, value in enumerate(list_):
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", value)  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", list_[i])
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", list_[i])
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

# while True:
#     if n % 3 == 0:
#          n = n // 3
#          if n == 1:
#               break
#     else:
#          break

# def check_h(n):
#     while n > 1:
#         n = int(input("Введите число\n"))
#
#         while True:
#             if n % 2 == 0:
#                 n = n // 2
#             else:
#                 n = (n * 3 + 1) // 2
#             print(n)
#
#             if n == 1:
#                 print("Done")
#                 break
#         if n == 1:
#             return True
#     return False
# print(check_h(n = 10))

# def print_ladder (n):
#     for i in range(1 , n + 1):
#         print('*' * i)
# print_ladder(3)

# def print_2_add_2():
#     result = 2 + 2
#     print(result)
#
# print_2_add_2()

# def hello_world():
#     print("Hello world")
#
# hello_world()

# def check_num(a, n):
#    if a % n == 0:
#        print(f"Число {n} является делителем числа {a}")
#    else:
#        print(f"Число {n} не является делителем числа {a}")
#
# check_num(4, 2)  # Число 2 является делителем числа 4
# check_num(5, 2)  # Число 2 не является делителем числа 5

# def reverse_stair(n):
#     for i in range(n, 0, -1):
#         print('*' * i)
# reverse_stair(5)

# def pow_func(base, n=2):
#    print(base ** n)
#
# print(pow_func(3))

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))

# outside_result = pow_func(3)
# print(outside_result)

# def get_multipliers(a):
#     count = 0
#     for n in range(1, a + 1):
#         if a % n == 0:
#             count += 1
#
#     return count
# get_multipliers(5)  # 2
# get_multipliers(4)  # 3

# def check_palindrome(str_):
#    str_ = str_.lower()
#    str_ = str_.replace(" ", "")
#
#    if str_ == str_[::-1]:
#        return True
#    else:
#        return False
#
# check_palindrome("test")  # False
# check_palindrome("Кит на море не романтик")  #

# x = 3
# def function():
#     print(x)
#     return x
#
# print(function())

# x = 3
#
#
# def func():
#    print(x)
#    x = 5
#    x += 5
#    return x
#
#
# print(func())

# def mul(*nums):
#     p = 1
#     for n in nums:
#         p *= n
#     return p

# def rec_sum(n):
#    if n == 1:  # терминальный случай
#        return 1
#    return n + rec_sum(n - 1)  # рекурсивный вызов
#
# def reverse_str(string):
#    if len(string) == 0:
#        return ''
#    else:
#        return string[-1] + reverse_str(string[:-1])
#
# reverse_str('test')  # tset

# def sum_digit(n):
#    if n < 10:
#        return n
#    else:
#        return n % 10 + sum_digit(n // 10)
#
# sum_digit(123)  # 6

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

# def repeat_list(list_):
#    list_values = list_.copy()
#    while True:
#        value = list_values.pop(0)
#        list_values.append(value)
#        yield value
#
# for i in repeat_list([1, 2, 3]):
#    print(i)

# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз

# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper