#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':

    lst = list(map(int, input('Введите элементы списка через пробел').split()))
    lst[lst.index(min(lst))], lst[-1] = lst[-1], lst[lst.index(min(lst))]
    print(lst)