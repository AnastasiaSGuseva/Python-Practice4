"""
1. Вычислить число π c заданной точностью d.

*Пример:* 

- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

"""


d = float(input('Задайте точность вычисления: '))
i = 0


while 10**i != d:
    i += (-1)

i = abs(i)
pi = 0


for n in range(10**(i + 1)):
    pi = pi + 4 * (((-1)**n) / (2*n + 1))


print(round(pi, i))
