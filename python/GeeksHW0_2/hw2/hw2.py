import random
#батя и мама класс
class Hero:
    #консруктор супер класса
    def __init__(self, name, level, health, strength):
        #атрибуты hero
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    #методы класса hero
    def greet(self):
        print(f"Меня зовут {self.name} мой лвл: {self.level} и я тебя раскидаю")
        
    def attack(self):
        print(f"{self.name} наносит удар")
    
    def rest(self):
        print(f"{self.name} отдыхает")
        self.health  +=1 

#дочка воин
class Warrior (Hero):
    #конструктор
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name,level,health,strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} атакует")
    
#дочка маг
class Mage (Hero):
    #конструктор    
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} кастует заклинание!")

#дочка ассасин
class Assassin (Hero):
    #конструктор
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} атакует из-под тишка")


#создаем 3ех героев:
warriorHero = Warrior("воин", 25, 100, 100, 100)
mageHero = Mage("маг", 21, 100, 100, 100)
assassinHero = Assassin("наикрутейший ассасин jin-woo", 100, 100, 1000, 100)

#список героев
heroes = [warriorHero, mageHero, assassinHero]


#логика игры камень ножницы бумага


#кто победил?
def who_is_winner(userHero, randomHero):
    if type(userHero) == type(randomHero):
        return None #если прокнет тот же класс что и выбрал юзер
    #warrior побеждает ассасина
    if isinstance(userHero,Warrior) and isinstance(randomHero, Assassin):
        return userHero
    if isinstance(userHero, Assassin) and isinstance(randomHero, Warrior):
        return randomHero
    #Маг побеждает Воина
    if isinstance(userHero, Mage) and isinstance(randomHero, Warrior):
        return userHero
    if isinstance(userHero, Warrior) and isinstance(randomHero, Mage):
        return randomHero
    if isinstance(userHero, Assassin) and isinstance(randomHero,Mage ):
        return userHero
    if isinstance(userHero, Mage) and isinstance(randomHero, Assassin):
        return randomHero


#выбор героя
user_choice = input(f"Выбери свой класс : {warriorHero.name} / {mageHero.name} / {assassinHero.name} \n").lower() 
if user_choice == warriorHero.name:
    userHero = warriorHero
elif user_choice == mageHero.name:
    userHero = mageHero
elif user_choice == assassinHero.name:
    userHero = assassinHero
else:
    print("Ты дурень") 
    exit() 



#выбирает рэндомича героя
random_heroes = [hero for hero in heroes if hero != userHero]
randomHero = random.choice(random_heroes) 

userHero.attack()
randomHero.attack()

#определяем победителя
winner = who_is_winner(userHero, randomHero)

if winner is None:
    print("Ничья")
else:
    print(f"Победил: {winner.name}")
