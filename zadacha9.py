def zadacha9():
    while True:
        print('Введите период колебаний в секундах:')
        a=int(input())
        if a <= 0:
            print('Период должен быть больше нуля.')
        else:
            break
    t=1/a
    print('Частота равна', t, 'Гц')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha9()
