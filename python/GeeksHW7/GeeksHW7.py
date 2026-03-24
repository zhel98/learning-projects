

celevoe_chislo = int(input("Введите целовое число: "))
numbers = []
for i in range(5):
    num = int(input("введите число которое хотите добавить в список: "))
    numbers.append(num)
print(f'ваш список чисел: {numbers}')

numbers.sort(key=lambda x: abs(x - celevoe_chislo))
print(f'({celevoe_chislo}, {numbers})')
