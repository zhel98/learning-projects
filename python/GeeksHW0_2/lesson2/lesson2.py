#наследование

#родительский | супер класс
class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
    def action(self):
        return f"{self.name} base action!"
    
Kirito = Hero("Ardager", 100, 1000)

#дочерний | подкласс
class MageHero(Hero):

    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp
    
    def action(self): 
        print(f'im {self.name} this is my action!')

asuno = MageHero("Asuno", 100, 1000, 999)
# print(Kirito.action())
# print(asuno.action())

class Fly:
    def action(self):
        print("I can fly!")

class swim:
    def action(self):
        print("I can swim!")

class Animal(swim, Fly):
    pass

# duck = Animal()
# duck.action()

class A:
    def action(self):
        print("A")

class B (A):
    def action(self):
        super().action()
        print("B")

class C(A):
    def action(self):
        super().action()
        print("C")

class D(B, C):
    def action(self):
        super().action()
        print("D")
# test = D()
# test.action()
# print(D.__mro__)
i=0
while True:
    i+=1
    if i == 10+1:
        break
    print(i)