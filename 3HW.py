"""
3 Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

*Пример*

- при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

"""


a = input('Введите последовательность чисел через пробел: ').split()
int_a = [int(i) for i in a]
b = []


for i in range(len(int_a)):
    count = int_a.count(int_a[i])
    if count == 1:
        b.append(int_a[i])


print(int_a)
print(b)
