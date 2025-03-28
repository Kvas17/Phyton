zarplata = float(input('Введите заработанную плату в месяц:'))
ipoteka = float(input('Введите сколько процентов уходит на ипотеку:'))
jizn = float(input('Введите сколько процентов уходит на жизнь'))
premiya = float(input('Введите количество премий за год:'))
naipoteku = (zarplata * ipoteka / 100)
najizn = (zarplata * jizn / 100)
sberejeniagod = ((zarplata - naipoteku - najizn) * 12)
otpremia = zarplata / 2
naipoteku12 = (naipoteku * 12)
nakoplenia = (sberejeniagod + otpremia)
print (f'На ипотеку было потрачено: {naipoteku12}')
print (f'Общие сбережения: {nakoplenia}')




