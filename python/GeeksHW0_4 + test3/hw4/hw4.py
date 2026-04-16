rates = {
    "KGS": 1,
    "USD": 89,
    "EUR": 96,
    "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
       
    def convert_to_kgs(self):
       if self.currency not in rates:
           raise ValueError("не та валюта")
       rate = rates[self.currency]
       return self.amount * rate

   
    def __add__(self, other):
        total= self.convert_to_kgs() #смысл проверять, все в сомы перевести
        total += other.convert_to_kgs()
        return Money(total,"KGS")
    
    
    def __str__(self): #принт не может вытащить объект приходится переводить
        return f"{self.amount} {self.currency}"
    
    
    def __sub__(self, other):
        total2 = self.convert_to_kgs()
        total2 -= other.convert_to_kgs()
        return Money (total2,"KGS")
    
    
    def __mul__(self, other):
        total3= self.amount*other
        return Money(total3,self.currency)
    
    
    def __truediv__(self, other):
        total4 = self.amount/other
        return Money(total4,self.currency)


    
m1 = Money(20,"KGS")
number = float(input("число: "))
# multiply = m1 * number #походу обязательно в таком порядке селф первый идет
deli = m1 / number
print(deli)