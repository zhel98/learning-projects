from abc import ABC, abstractmethod
#батя и мама класс
class Hero(ABC):
    #конструктор класса
    def __init__(self, name, level, __health, strength):
        self.name = name
        self.level = level
        self.__health = __health
        self.strength = strength
    
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")


    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1 #патаму шта атрибут health приватный нужно через селф к нему обращаться
    
    @abstractmethod
    def attack(self):
        pass

#конструктор класса не нужен нет новых атрибутов у дочки
class Warrior(Hero):

    def attack(self):
        print(f"Воин атакует мечом")

class Mage(Hero):

    def attack(self):
        print(f"Маг использует магию")

class Assassin(Hero):

    def attack(self):
        print(f"Ассасин атакует из-под тишка")

WarriorEldar = Warrior("Eldar-Warrior", 100,100,100)
MageEldar = Mage("Eldar-Mage", 100,100,100)
AssassinEldar = Assassin("Eldar-Assasin",100,100,100)

    
WarriorEldar.attack()
WarriorEldar.greet()
WarriorEldar.rest()

MageEldar.attack()
MageEldar.greet()
MageEldar.rest()

AssassinEldar.attack()
AssassinEldar.greet()
AssassinEldar.rest()