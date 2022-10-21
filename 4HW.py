"""
4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и записать в файл многочлен степени k.

*Пример:* 

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
- k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

"""

import random

k = int(input('Введите натуральную степень k = '))
koef_list = []


for i in range(k+1):
    koef_list.append(random.randrange(0, 100))

result_str = []

for i in range(k, -1, -1):
    if i == 0:
        str_ = f'{koef_list[i]}'
    elif i == 1:
        str_ = ('{}x'.format(koef_list[i]))
    else:
        str_ = ('{}x^{}'.format(koef_list[i], i))
    result_str.append(str_)



simbols = [' + ', ' - ']
res = ''
for i in result_str:
    if i == result_str[-1]:
        res = res + i
    else:
        res = res + i + random.choice(simbols)
print(res, ' = 0')
