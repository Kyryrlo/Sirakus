﻿print("*** ИГРЫ С ЧИСЛАМИ ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    try:
        a = int(input("Введите целое число => "))
        break
    except ValueError:
        print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Не имеет смысла что-то делать с нулём")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a #c=b=a=453->45->4->0
    paaris=0
    paaritu=0
    while b > 0:
        if b % 2 == 0:
            paaris += 1
        else:
            paaritu += 1
        b = b // 10
    print("Чётных цифр:", paaris)
    print("Нечётных цифр:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Переворачиваем* введённое число")
    print()
    b=0             # c=453 a=453 b=0
    while a > 0:    # a=453 a=45 a=4
        n = a % 10  # n=453 n=5 n=4
        a = a // 10 # a=45 a=4 a=0
        b = b * 10  # b=0 b=30 b=350
        b += n      # b=3 b=35 b=354
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print(("Проверяем гипотезу Сиракуз"))
    print()
    # c=453
    if c % 2 == 0:
        print("с - чётное число. Делим на 2.")
    else:
        print("с - нечётное число. Умножаем на 3, прибавляем 1 и делим на 2.")
    while c != 1:
        if c % 2 == 0:
            c = c / 2
        else:
            c = (3*c + 1) / 2
        print(str(c), ",", end="")
    print()
    print("Гипотеза верна")
