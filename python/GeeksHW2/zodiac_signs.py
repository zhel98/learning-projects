#просим юзера ввести день и месяц рождения, сохраняем эти данные в переменные day и month соответственно
day = int(input ("Введите день рождения: "))
month = int(input ("Введите месяц рождения: "))

#булеанская переменная, которая будет хранить информацию о том, являются ли введенные данные корректными или нет
isValid = True

if month < 1 or month > 12:
    isValid = False
elif month == 2:
    if day < 1 or day > 28:
        isValid = False
elif month in [1, 3, 5, 7, 8, 10, 12]:
    if day < 1 or day > 31: #мес которые имеют 31 день
        isValid = False
else:
    if day < 1 or day > 30: #мес которые имеют 30 дней
        isValid = False
# если isValid=False, то выполняется код внутри if, если isValid=True, то выполняется код внутри else

if not isValid: 
    print("Некорректные данные")
else:#по таблице мутим знаки задиаки
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        print("Ваш знак зодиака: Овен")
    elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
        print("Ваш знак зодиака: Телец")
    elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
        print("Ваш знак зодиака: Близнецы")
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        print("Ваш знак зодиака: Рак")
    elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
        print("Ваш знак зодиака: Лев")
    elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
        print("Ваш знак зодиака: Дева")
    elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
        print("Ваш знак зодиака: Весы")
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        print("Ваш знак зодиака: Скорпион")
    elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
        print("Ваш знак зодиака: Стрелец")
    elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
        print("Ваш знак зодиака: Козерог")
    elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        print("Ваш знак зодиака: Водолей")
    elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
        print("Ваш знак зодиака: Рыбы")
