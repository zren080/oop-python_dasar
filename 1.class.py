class Hero:
    pass

hero1 = Hero() # objek / instance (instansiate)
hero2 = Hero()
hero3 = Hero()

hero1.name = 'Vanesa'
hero2.health = 100

hero2.name = 'kadita'
hero2.health =  96

hero3.name = 'tigreal'
hero3.health = 1000

print(hero1) #menampilkan objek
print(hero1.__dict__) #melihat dictonary
print(hero1.name) #menampilkan attributes