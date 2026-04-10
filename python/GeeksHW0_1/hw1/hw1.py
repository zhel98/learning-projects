class Hero:
    # Конструктор: задаем начальные данные героя
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    # 1. Приветствие
    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    # 2. Атака
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1 

    # 3. Отдых 
    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


# Создаем двух героев (2 объекта)
warrior = Hero("бухарь", 10, 100, 20)
mage = Hero("типок", 80, 50, 5)

# Вызываем методы для первого героя
print(f"{warrior.name} ДО: HP {warrior.health}, Str {warrior.strength}")
warrior.greet()
warrior.attack()
warrior.rest()
print(f"{warrior.name} ПОСЛЕ: HP {warrior.health}, Str {warrior.strength}\n")

# Вызываем методы для второго героя
print(f"{mage.name} ДО: HP {mage.health}, Str {mage.strength}")
mage.greet()
mage.attack()
mage.rest()
print(f"Статистика {mage.name} ПОСЛЕ: HP {mage.health}, Str {mage.strength}")