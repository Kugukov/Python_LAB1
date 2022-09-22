#!/usr/bin/env python3
# coding=utf-8

def main():
    try:
        a = int(input('Введите A: '))
        b = int(input('Введите B: '))
        x = int(input('Введите X: '))
        try:
            if x > 4:
                y = (5 * x * x + b * b) / (a * a + b * b)
            else:
                y = 6 * (x * x - a * a)
            print("y = %.1f" % y)
        except:
            print("Нет решения!")
    except:
        print("Неверные входные данные!")


if __name__ == '__main__':
    main()
