width = int(input ('Введите ширину, см '))
lenght = int(input ('Введите длину, см '))
height = int(input ('Введите высоту, см '))
if width < 15 and height < 15:
    print ('Коробка №1')
elif (width > 15 or lenght > 15 or height > 15) and (width < 50 and lenght < 50 and height < 50):
    print ('Коробка №2')
elif lenght > 200:
    print ('Ищите упаковку для лыж')
else:
    print ('Стандатрная коробка №3')