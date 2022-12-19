#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Введите элементы списка через пробел:')
lst = list(map(int, input().split()))

result = 1
for x in lst[1::2]:
    result *= x
print('1. Произведение элементов списка с четными номерами:', result)

if lst.count(0) > 1:
    x1 = lst.index(0)
    x2 = len(lst) - lst[::-1].index(0)
    result = sum(lst[x1:x2])
    print('2. Сумма элементов списка, расположенных между первым и последним нулевыми элементами:', result)
else:
    print('2. "нулевых элементов меньше двух!"')

lst.sort(reverse=True)
print('3. Преобразованный список:', lst)