class Hero:
    
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    # void function, method tanpa retrun & argumen
    def no_args(self):
        print('ini method no argumen, dengan hero ' + self.name)
    # method degnan argumen
    def healthup(self,up):
        self.health += up

    # method dengan retrun. Bisa juga di tambahkan dengan retrun
    def getHealth(self):
        return self.health

hero1 = Hero('Vexana',100,84,80)
hero2 = Hero('Martis',100,79,94)
hero3 = Hero('Tigreal',100,59,100)

hero1.no_args()
hero1.healthup(40) # tidak bisa langsung di print
print(hero1.health)
print(hero1.getHealth())
