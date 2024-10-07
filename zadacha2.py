def zadacha1():
    print('Введите силу в ньютонах:')
    a=int(input())
    if a <= 0:
        a=a*(-1)
    print('Введите ускорение в метрах на секунду в квадрате:')
    b=int(input())
    if b <= 0:
        b=b*(-1)
    t=a/b
    print('Масса равна', t, 'кг')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha1()
