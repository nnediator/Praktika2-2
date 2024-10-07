def zadacha4():
    print('Введите значение силы в ньютонах:')
    a=int(input())
    while True:
        print('Введите расстояние в метрах:')
        b=int(input())
        if b <= 0:
            print('Расстояние должно быть больше нуля.')
        else:
            break
    A=a*b
    print('Работа равна', A, 'Дж')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha4()
