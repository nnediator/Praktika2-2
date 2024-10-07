def zadacha7():
    while True:
        print('Введите модуль силы в ньютонах:')
        a=int(input())
        if a <= 0:
            print('Модуль силы должен быть больше нуля.')
        else:
            break
    while True:
        print('Введите площадь в квадратных метрах:')
        b=int(input())
        if b <=0:
            print('Площадь должна быть больше нуля.')
        else:
            break
    t=a/b
    print('Давление равно', t, 'Па')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha7()
