print('Выберите номер задачи:')
print('Задача 1: Определение скорости')
print('Задача 2: Определение массы')
print('Задача 3: Определение температуры по Цельсию')
print('Задача 4: Определение работы')
print('Задача 5: Определение кинетической энергии')
print('Задача 6: Определение потенциальной энергии')
print('Задача 7: Определение давления')
print('Задача 8: Определение теплоты')
print('Задача 9: Определение частоты')
print('Задача 10: Определение объема')
while True:
    z=int(input())
    if z ==1:
        from zadacha1 import zadacha1
        break
    elif z ==2:
        from zadacha2 import zadacha2
        break
    elif z ==3:
        from zadacha3 import zadacha3
        break
    elif z ==4:
        from zadacha4 import zadacha4
        break
    elif z ==5:
        from zadacha5 import zadacha5
        break
    elif z ==6:
        from zadacha6 import zadacha6
        break
    elif z ==7:
        from zadacha7 import zadacha7
        break
    elif z ==8:
        from zadacha8 import zadacha8
        break
    elif z ==9:
        from zadacha9 import zadacha9
        break
    elif z ==10:
        from zadacha10 import zadacha10
        break
    else:
        print('Такой задачи не существует')
        print('Выберите номер задачи:')
    
