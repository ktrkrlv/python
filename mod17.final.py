# 17.9.1
import random


def quick_sort(input_mas):
    if len(input_mas) <= 1:
        return input_mas
    elem = random.choice(input_mas)
    left = list(filter(lambda x: x < elem, input_mas))
    center = [i for i in input_mas if i == elem]
    right = list(filter(lambda x: x > elem, input_mas))
    return quick_sort(left) + center + quick_sort(right)


def binary_search(mas, n, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # ошибка
    middle = (right + left) // 2  # середина
    if mas[0] == n:
        return 'Введенное число совпадает с первым в массиве, i числа справа: 1'
    if mas[0] > n:
        return 'Введенное число - минимальное, i числа справа: 0'
    if mas[-1] < n:
        return f'Введенное число - максимальное, i числа слева: {len(mas)-1}'
    if mas[-1] == n:
        return f'Введенное число совпадает с последним в массиве, i числа слева: {len(mas)-2}'
    if mas[middle] == n:
        return f'i числа, меньше введенного: {middle-1}\ni числа, больше или равного введенному: {middle+1}'
    if mas[middle+1] >= n > mas[middle]:
        return f'i числа, меньше введенного: {middle}\ni числа, больше или равного введенному: {middle+1}'
    if mas[middle-1] < n <= mas[middle]:
        return f'i числа, меньше введенного: {middle-1}\ni числа, больше или равного введенному: {middle}'
    elif n < mas[middle]:  # если элемент меньше элемента в середине, рекурсивно ищем в левой половине
        return binary_search(mas, n, left, middle - 1)
    else:  # иначе - в правой
        return binary_search(mas, n, middle + 1, right)


input_mas = list(map(int, input("Введите целые числа через пробел: ").split()))
n = int(input("Введите целое число: "))

mas = quick_sort(input_mas)
print(mas)
print(binary_search(mas, n, 0, len(mas)-1)) # запускаем алгоритм на левой и правой границе

