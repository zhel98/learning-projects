from abc import ABC, abstractmethod

#батя и мама класс
class Hero:
    #конструктор класса
    def __init__(self, name, lvl, hp):
    #атрибуты
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action (self):
        print(f"{self.name} готов к бою!")


#дочка Маг
class MageHero (Hero):
    #конструктор класса
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    
    def action(self):
        print(f"{self.name} кастует заклинание")


#Мага дочка воин
class WarriorHero (MageHero):
    #конструктор класса
    def __init__ (self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp, mp)
    
    def action(self):
        print(f"{self.name} рубит мечом! Уровень: {self.lvl}")


#bank acc класс
class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance, password, bank_name):
        self.hero = hero
        self._balance = balance
        self.__password = password
        self.bank_name = bank_name

    def login(self, password):
        return password == self.__password
    
    @property #только чтение 
    def full_info(self):
        return f"Герой: {self.hero.name}, lvl: {self.hero.lvl}, balance: {self._balance}"
          
    @classmethod #банан слс
    def get_bank_name(cls):
        return cls.bank_name
    
    def bonus_for_level(self):
        return self.hero.lvl *10
    
    def __str__(self): #принт магия епта
        return f"{self.hero.name} balance: {self._balance}"
    
    def __add__(self,other): # магия плюсика прибавляем бабки
        if isinstance(other, BankAccount):
            if type(self.hero) == type (other.hero):
                return self._balance + other._balance #если все идеалдуу
            return "Дурень разные классы" #если первый if прошел а второй выдал False
        return "Только bank acc складываются" #если первая проверка не прошла
    
    def __eq__(self, other): # магия дабл равно если классы и уровни на уровне)
        if isinstance(other, BankAccount):
            return type(self.hero) == type(other.hero) and self.hero.lvl == other.hero.lvl
        return False

#Абстрактный класс SmsService
class SmsService(ABC):
    @abstractmethod
    def send_otp(self, phone):
        pass

class KGSms(SmsService):
    def send_otp(self, phone):
        return f"<text>Код: 1234</text><phone>{phone}</phone>"


class RUsms(SmsService):
    def send_otp(self, phone):
        return {"text": "Код: 1234", "phone": phone}

mage1 = MageHero("Маг1", 80, 500, 150)
mage2 = MageHero("Маг2", 80, 500, 200)
warrior = WarriorHero("Конааан Варвар", 50, 900, 20)

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

print(mage1.action())
print(warrior.action())
print(acc1)
print(acc2)

