data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")
designations = []
codes = []
for item in data:
    if item.isdigit():
        codes.append(item)
    else:
        designations.append(item)
print(f'лист дезигнаторы: {designations}\nлист коды: {codes}')

operators = dict(zip(designations,codes)) # через дикт и зип (дикт- мучу слоаврь а зип объединяю 2 листа)

print(f'удаленные операторы:\nФонекс с кодом {operators.pop("Fonex")}, Кател с кодом {operators.pop("Katel")}')
print(f'промежуточный итог: {operators}')


#юзая ключ мы ссылаемся на коды и превращем их в сеты
#operators[key] - ссылка на вэлью то есть то что лежит внутри словаря и этот вэлью мы как раз таки и превращем в сет
for key in operators:
    operators[key]={operators[key]}

#дальше изи при помощи ключа я добавляю в уже существующий сет еще один сет
operators['O!'].add('0700')
operators['O!'].add('0500')
operators['Megacom'].add('0555')
operators['Megacom'].add('0558')
operators['Beeline'].add('0777')
operators['Beeline'].add('0111')

print(f"0!-{operators['O!']}")
print(f"Beeline-{operators['Beeline']}")
print(f"Megacom-{operators['Megacom']}")
