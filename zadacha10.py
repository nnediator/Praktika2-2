def zadacha10():
    while True:
        print('Введите радиус основания цилиндра:')
        a=int(input())
        if a <= 0:
            print('Радиус должен быть больше нуля.')
        else:
            break
    while True:
        print('Введите высоту цилиндра:')
        b=int(input())
        if b <=0:
            print('Высота должна быть больше нуля.')
        else:
            break
    t=3.14*a*a*b
    print('Объем цилиндра равен', t)
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha10()

