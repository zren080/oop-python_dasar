class Hero: # template
    # class variabel / statik
    jumlah = 0 # jumlah akan nempel pada class

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variabel -> hanya dimiliki oleh variabel(hero1/hero2 DST)
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print('Membuat hero dengan nama ' + inputName)

print(Hero.jumlah)
hero1 = Hero('Vexana',100,84,80)
print(Hero.jumlah)
hero2 = Hero('Martis',100,79,94)
print(Hero.jumlah)
hero3 = Hero('Tigreal',100,59,100)
print(Hero.jumlah)

