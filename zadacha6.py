def zadacha6():
    while True:
        print('Введите массу в киллограммах:')
        a=int(input())
        if a <= 0:
            print('Масса должна быть больше нуля.')
        else:
            break
    print('Введите высоту в метрах:')
    b=int(input())
    print('Введите ускорение свободного падения в метрах на секунду в квадрате:')
    c=int(input())   
    t=a*b*c
    print('Потенциальная энергия равна', t, 'Дж')
    while True:
        p = input("Введите q для выхода: ")
        if p == 'q':
            print("Выход из программы...")
            break  
        else:
            print('Вы ввели:' + p)
zadacha6()
