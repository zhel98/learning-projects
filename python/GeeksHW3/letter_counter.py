# Программа должна:
# спросить слово
# если пользователь хочет выйти — завершиться
# взять это слово
# посмотреть на каждую букву
# определить, какая буква гласная, какая согласная
# вывести:
        # общее количество букв
        # количество гласных
        # количество согласных
        # процент гласных и согласных

glasnye = "aeiouауоыиэяюёе"#легче прописать гласные так как их меньше, чем согласных
while True:
    word = input("Введите слово или стоп для выхода: ").lower()
    if word == "стоп":
        break
    glasnye_count = 0
    soglasnye_count = 0

    for letter in word: #проходим по каждой букве в слове
    #isalpha проверяет, является ли символ буквой (булинское значение True или False)
        if letter.isalpha():
            if letter in glasnye:
                glasnye_count += 1 #счетик гласных
            else:
                soglasnye_count += 1 #счетик согласных
    total_letters = glasnye_count + soglasnye_count #общщее кол-во букв

    #вывод результатов
    print(f"Общее количество букв: {total_letters}")
    print(f"Количество гласных: {glasnye_count}")
    print(f"Количество согласных: {soglasnye_count}")
    #процентики
    if total_letters > 0:
        glasnye_percent = (glasnye_count / total_letters) * 100 #пропорция считаю
        soglasnye_percent = (soglasnye_count / total_letters) * 100
        print(f"Процент гласных: {glasnye_percent:.2f}%") #:.2f - хочица два знака после запятой
        print(f"Процент согласных: {soglasnye_percent:.2f}%")
    else:
        print("Нет букв для анализа.")