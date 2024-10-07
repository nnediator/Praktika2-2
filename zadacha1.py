def zadacha1():
    while True:
        print('Введите расстояние в киллометрах:')
        a=int(input())
        if a <= 0:
            print('Расстояние должно быть больше нуля.')
        else:
            break
    while True:
        print('Введите время в часах:')
        b=int(input())
        if b <= 0:
            print('Время должно быть больше нуля.')
        else:
            break
    t=a/b
    print('Скорость равна', t, 'км/ч')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha1()
