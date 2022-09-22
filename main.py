#!/usr/bin/env python3
# coding=utf-8

a = int(input('Введите A: '))
b = int(input('Введите B: '))
x = int(input('Введите X: '))
if x > 4:
    y = (5 * x * x + b * b)/(a * a + b * b)
else:
    y = 6 * (x * x - a * a)

print("y = %.1f" % y)
