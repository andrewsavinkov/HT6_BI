# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
# 
# n=4
# def create_lst(n):
#     lst=[]
#     for i in range(1, n+1):
#         n=(1+1/i)**i
#         n=round(n, 2)
#         lst.append(n)
#     print(lst)
#     print(f'Сумма {sum(lst)}')

# create_lst(n)
# Упрощенное решение:
# my_list=[round((lambda x: (1+1/x)**x)(x), 2) for x in range(1, n+1)]
# print(my_list)
# print(f'Сумма: {sum(my_list)}')

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint

# def random_list(length):
#     array = []
#     for i in range(length):
#         array.append(randint(0, 10))
#     print(array)
#     return array

# def sum_of_uneven(input_list):
#     sum = 0
#     for i in range(1, len(input_list), 2):
#         sum=sum+input_list[i]
#     return sum

# rnd=random_list(10)
# print(sum_of_uneven(rnd))
# Упрощенное решение:

# from random import randint

# length = 10
# rnd_lst=[randint(0,10) for x in range(length)]
# uneven_lst=[rnd_lst[x] for x in range(length) if x%2!=0]
# print(rnd_lst)
# print(uneven_lst)
# print(sum(uneven_lst))

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# lst=[2, 3, 4, 5, 6, 7, 8]
# # lst.__delitem__(len(lst)-1)
# # print(lst)

# def pair_mult(input_list):
#     lst=[]
#     if not len(input_list) % 2:
#         for i in range(len(input_list)//2):
#             lst.append(input_list[0]*input_list[len(input_list)-1])
#             input_list.__delitem__(0)
#             input_list.__delitem__(len(input_list)-1)
#         print(lst)
#     else:
#         for i in range(len(input_list) // 2):
#             lst.append(input_list[0] * input_list[len(input_list) - 1])
#             input_list.__delitem__(0)
#             input_list.__delitem__(len(input_list) - 1)
#         lst.append(input_list[len(input_list) // 2]**2)
#         print(lst)

# pair_mult(lst)
# Упрощенное решение:
# from random import randint
# length=10
# lst=[randint(0, 10) for x in range(length)]
# print(lst)

# new_lst=[(lambda x, y: x*y)(lst[x], lst[len(lst)-x-1]) for x in range(len(lst)//2)]
# print(new_lst)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst=[1.1, 1.2, 3.1, 5, 10.01]
# def diff_of_float(input_list):
#     new_lst=[]
#     help_lst=[]
#     diff=0
#     for i in input_list:
#         new_lst.append(str(i).split('.'))

#     for i in range(len(input_list)):
#         help_lst.append(round(input_list[i]%int(new_lst[i][0]), 2))
#     while 0 in help_lst:
#         help_lst.__delitem__(help_lst.index(0))

#     print(f'{input_list} => {max(help_lst)-min(help_lst)}')
# diff_of_float(lst)

# Упрощенное решение:
# my_lst=[1.1, 1.2, 3.1, 5.3, 10.01]
# def dec_part(some_double):
#     str_nums_lst=str(some_double).split('.')
#     if len(str_nums_lst)==1:
#         str_number=0
#     else:
#         str_number='0.'+str_nums_lst[1]
#         str_number=float(str_number)
#     return str_number 

# new_list=list(map(dec_part, my_lst))
# print(f'\t\tmax element:\t{max(new_list)}\n \
#         \tmin element:\t{min(new_list)}\n \
#         \ttheir diff:\t{max(new_list)-min(new_list)}')