month = input('Введите месяц рождения - ')
day = float(input('Введите дату рождения - '))

    # Функция для проверки максимального числа в месяце
def is_valid_date(month, day):
    month_days = {
        'январь': 31,
        'февраль': 29, 
        'март': 31,
        'апрель': 30,
        'май': 31,
        'июнь': 30,
        'июль': 31,
        'август': 31,
        'сентябрь': 30,
        'октябрь': 31,
        'ноябрь': 30,
        'декабрь': 31
    }
    if month not in month_days:
        return False
    return 1 <= day <= month_days[month]


while True:
    month = input("Введите месяц: ").lower().strip()
    day = int(input("Введите число: "))
    
    if not is_valid_date(month, day):
        print("Ошибка: такой даты не существует! Попробуйте ещё раз.")
        continue
    
    break 


if (month == "март" and day >= 21) or (month == "апрель" and day <= 20):
    print ('Овен')
elif (month == "апрель" and day >= 21) or (month == "май" and day <= 21):
    print ('Телец')
elif (month == "май" and day >= 22) or (month == "июнь" and day <= 21):
    print ('Близнецы')
elif (month == "июнь" and day >= 22) or (month == "июль" and day <= 22):
    print ('Рак')
elif (month == "июль" and day >= 23) or (month == "август" and day <= 23):
    print ('Лев')
elif (month == "август" and day >= 24) or (month == "сентябрь" and day <= 23):
    print ('Дева')
elif (month == "сентябрь" and day >= 24) or (month == "октябрь" and day <= 23):
    print ('Весы')
elif (month == "октябрь" and day >= 24) or (month == "ноябрь" and day <= 22):
    print ('Скорпион')
elif (month == "ноябрь" and day >= 23) or (month == "декабрь" and day <= 22):
    print ('Стрелец')
elif (month == "декабрь" and day >= 23) or (month == "январь" and day <= 20):
    print ('Козерог')
elif (month == "январь" and day >= 21) or (month == "февраль" and day <= 19):
    print ('Водолей')
elif (month == "февраль" and day >= 20) or (month == "март" and day <= 20):
    print ('Рыбы')