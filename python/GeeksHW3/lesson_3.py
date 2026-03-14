#операторы, принадлежности, назначения, циклы
"оператор принадлежности in "
# print ('p' in 'python')
# print ('q' in 'python')

# print (11 in range(1,11))
# print(2 in range(1,11))
# print(5.5 in range(1,11))

# while True:
#     time = int(input("введите время:"))
#     if time == "stop":
#         break
#     if(time >= 18 and time <= 23):
#         print("Сейчас вечер")
#     elif(time >= 6 and time < 18):
#         print("Сейчас утро")
#     else:
#         print("Здравствуйте")

#просим юзера ввести день и месяц рождения, сохраняем эти данные в переменные day и month соответственно
# counter = 0
# while True:
#     if counter == 12:
#         break
#     day = int(input ("Введите день рождения : "))
#     month = int(input ("Введите месяц рождения: "))

#     #булеанская переменная, которая будет хранить информацию о том, являются ли введенные данные корректными или нет
#     isValid = True
    
#     if month < 1 or month > 12:
#         isValid = False
#     elif month == 2:
#         if day < 1 or day > 28:
#             isValid = False
#     elif month in [1, 3, 5, 7, 8, 10, 12]:
#         if day < 1 or day > 31: #мес которые имеют 31 день
#             isValid = False
#     else:
#         if day < 1 or day > 30: #мес которые имеют 30 дней
#             isValid = False
#     # если isValid=False, то выполняется код внутри if, если isValid=True, то выполняется код внутри else

#     if not isValid: 
#         print("Некорректные данные")
#     else:#по таблице мутим знаки задиаки
#         if (month == 3 and day >= 21) or (month == 4 and day <= 20):
#             print(f"Ваш знак зодиака: Овен (осталось попыток - {12 - counter })")
#         elif (month == 4 and day >= 21) or (month == 5 and day <= 21):
#             print(f"Ваш знак зодиака: Телец (осталось попыток - {12 - counter })")
#         elif (month == 5 and day >= 22) or (month == 6 and day <= 21):
#             print(f"Ваш знак зодиака: Близнецы (осталось попыток - {12 - counter })         ")
#         elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
#             print(f"Ваш знак зодиака: Рак (осталось попыток - {12 - counter })")
#         elif (month == 7 and day >= 23) or (month == 8 and day <= 21):
#             print(f"Ваш знак зодиака: Лев (осталось попыток - {12 - counter })")
#         elif (month == 8 and day >= 22) or (month == 9 and day <= 23):
#             print(f"Ваш знак зодиака: Дева (осталось попыток - {12 - counter })")
#         elif (month == 9 and day >= 24) or (month == 10 and day <= 23):
#             print(f"Ваш знак зодиака: Весы (осталось попыток - {12 - counter })")
#         elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
#             print(f"Ваш знак зодиака: Скорпион (осталось попыток - {12 - counter })")
#         elif (month == 11 and day >= 23) or (month == 12 and day <= 22):
#             print(f"Ваш знак зодиака: Стрелец (осталось попыток - {12 - counter })")
#         elif (month == 12 and day >= 23) or (month == 1 and day <= 20):
#             print(f"Ваш знак зодиака: Козерог (осталось попыток - {12 - counter })")
#         elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
#             print(f"Ваш знак зодиака: Водолей (осталось попыток - {12 - counter })")
#         elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
#             print(f"Ваш знак зодиака: Рыбы (осталось попыток - {12 - counter })")
#         counter += 1
    
# "for"
for number in range (1, 11):
    if number == 7:
        break
    if number % 2 == 0:
        continue
    print(number)


