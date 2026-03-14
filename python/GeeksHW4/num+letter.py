data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

# 1-2. Разделяем строки и все остальное
for item in data_tuple:
    if type(item) == str: #проверяет если айтем является числом
        letters.append(item) #добавляет в лист letters
    else:
        numbers.append(item) #добавляет в лист numbers

print("После разделения:") #промежуточный результат принтим
print("letters =", letters) 
print("numbers =", numbers)

# 3. Удаляем 6.13 из numbers
numbers.remove(6.13)

# Удаляем True из numbers и добавляем в конец letters
numbers.remove(True)
letters.append(True)

# Вставляем 2 между 3 и 1 
# list.insert(index, element)
numbers.insert(1, 2)

#промежуточный результат 2
print("\nПосле изменений:") 
print("letters =", letters)
print("numbers =", numbers)

# 4. Сортируем numbers
numbers.sort()

# Переворачиваем letters
letters.reverse()

# Меняем буквы местами, чтобы получилось как в задании
letters[1] = 'G'
letters[4] = 'K'
letters[6] = 'c'

#промежуточный резултат 3
print("\nПосле сортировки и разворота:")
print("letters =", letters)
print("numbers =", numbers)

# 5. Делаем список квадратов чисел 
# Функция len()  возвращает количество элементов в объекте
for i in range(len(numbers)): #1,4,9 = 3числа то есть 3 раза производится итерация возвести в степень 2 = 9
    numbers[i] = numbers[i] ** 2

print("\nКвадраты чисел:")
print("numbers =", numbers)

# 6. Превращаем списки в кортежи
letters = tuple(letters)
numbers = tuple(numbers)

print("\nИтог:")
print("letters =", letters)
print("numbers =", numbers)