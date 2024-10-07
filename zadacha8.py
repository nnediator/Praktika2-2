def zadacha8():
    while True:
        print('Введите массу в киллограмах:')
        a=int(input())
        if a <= 0:
            print('Масса должна быть больше нуля.')
        else:
            break
    while True:
        print('Введите удельную теплоемкость в Дж/(кг·°C):')
        b=int(input())
        if b <=0:
            print('Удельная теплоемкость должна быть больше нуля.')
        else:
            break
    print('Введите изменение температуры в °C:')
    c=int(input())
    t=a*b*c
    if t>=0:
        print('Количество теплоты, которое тело получило:', t, 'Дж')
    else:
        print('Количество теплоты, которое тело отдало:', t, 'Дж')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha8()
