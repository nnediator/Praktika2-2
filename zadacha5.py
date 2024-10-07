def zadacha5():
    while True:
        print('Введите массу объекта в киллограмах:')
        a=int(input())
        if a <= 0:
            print('Масса должна быть больше нуля.')
        else:
            break
    print('Введите скорость объекта:')
    b=int(input())
    t=(a*b*b)/2
    print('Кинетическая энергия равна', t, 'Дж')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha5()
