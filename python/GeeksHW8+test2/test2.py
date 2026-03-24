# Условия программы:
# Программа должна работать в бесконечном цикле с возможностью выхода
# Запрашивать у пользователя любое слово на латинице или кириллице, а также смешанно.
# Считывать строчные и прописные буквы, вне зависимости от ввода результат должен возвращаться в нижнем регистре
# Программа также должна работать со смешанными языками


# ru_raskladka = "йцукенгшщзхъёфывапролджэячсмитьбю/"
# eng_raskladka = "qwertyuiop[]\\asdfghjkl;'zxcvbnm,./" #два слэша потому что \a читается как один символ
# # print(len(ru_raskladka))
# # print(len(eng_raskladka))
# ru2eng = dict(zip(ru_raskladka, eng_raskladka))
# eng2ru = dict(zip(eng_raskladka, ru_raskladka))
# # print(ru2eng)
# # print(eng2ru)


# while True:
#     slovo = input("слово твое броузи (q-выход): ").lower()
#     if slovo == 'q':
#         break
#     novoe_slovo = ""
#     for i in slovo:
#         if i in ru2eng:
#             novoe_slovo += ru2eng[i]
#         elif i in eng2ru:
#             novoe_slovo += eng2ru[i]
#         else:
#             novoe_slovo += i
#     print(novoe_slovo)




# Напишите функцию "Вычисление скидки" Функция должна: принимать баллы за ДЗ, баллы за тест. На основе полученных данных вычислить сумму скидки по таблице и вернуть сумму скидки.

def calculate_discount(hw_score, test_score):
    if 65 <= hw_score <= 80 and 75 <= test_score <= 100:
        return 3000
    elif 65 <= hw_score <= 80 and 55 <= test_score <= 74:
        return 2000 
    elif 45 <= hw_score <= 64 and 75 <= test_score <= 100:
        return 2000 
    elif 45 <= hw_score <= 64 and 55 <= test_score <= 74:
        return 1000 
    else:
        return 0

hw = int(input("Введите баллы за ДЗ: "))
test = int(input("Введите баллы за тест: "))

discount = calculate_discount(hw, test)
print(f"Ваша скидка: {discount} сом")