data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for item in data:
    if item.isdigit():
        codes.append(item)
    else:
        designations.append(item)
print(f'лист дезигнаторы: {designations}\nлист коды: {codes}')

operators = dict()
i=0
while i < len(codes):
    key = designations[i] # у словаря операторы будут значения Key - название операторов (дезингаторов)
    value = codes[i] # а вэлью будут коды телефеонов
    operators[key]=value # присобачиваем ключи и вэлью друг дружке
    i+=1
print(f'словарь операторы: {operators}')


print(f'удаленные операторы:\nФонекс с кодом {operators.pop("Fonex")}, Кател с кодом {operators.pop("Katel")}')
print(f'мистер пропер веселей мистер пропер в два раза быстрей мистер пропер: {operators}')

#как првевратить operators из словря в сет?
operators = set()
print(operators)

