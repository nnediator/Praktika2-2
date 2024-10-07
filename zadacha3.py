def zadacha3():
    print('Введите температуру в градусах Фаренгейта:')
    a=int(input())
    t=a+273
    print('Температура равна', str(t), '°C')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha3()
