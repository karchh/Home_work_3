# ДОМАШКА 3
# Сдайте задание до: 5 дек., 20:00 +03:00 UTC


# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка с нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# x = [2, 3, 6, 10, 12, 16, 5]
# #print(x)
# summ = 0
# for i in range(1, len(x), 2):
#     #if i % 2 == 1:
#         summ += x[i]
# print(f"{x} -> сумма элементов на нечётных позициях: {summ}")


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]


# def mult_lst(lst):
#     l = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
#     new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(l)]
#     print(new_lst)
#
# lst = list(map(int, input("Введите числа через пробел: \n").split()))
# mult_lst(lst)



# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
#   [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# lst = list(map(float, input("Введите числа через пробел: \n").split()))
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print(max(new_lst) - min(new_lst))

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без применения встроенных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10


s = ""
n = int(input("Введите десятичное число: "))
while n != 0:
    s = str(n % 2) + s
    n //= 2
print("Двоичное число: ", (s))

