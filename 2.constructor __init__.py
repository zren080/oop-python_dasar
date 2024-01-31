''' # cara pertama
class Hero:
    
    def __init__(self):
        print('hello world')

hero1 = Hero()
hero2 = Hero()
'''
'''fungsi self setara dengan hero1'''
# cara kedua        
class Hero:
    
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero('Vexana',100,84,80)
hero2 = Hero('Martis',100,79,94)


print(hero1.__dict__)

# cara mengambil bebarapa attribute
def karakter_2():
    darah = hero2.health
    defense = hero2.armor
    return darah,defense

print(karakter_2())
#print(karakter_2) -> cara melihat addres memory yang digunakan

'''Init disini adalah constructor,
kalau gak butuh constructor gak pakai juga gak apa-apa, misalkan mau bikin class yang isinya static'''
'''Bang, itu kalo misal ada beberapa _init_ apakah bisa?
setau saya, method constructor itu cuma 1 dalam suatu class. CMIIW '''
'''attribute -> sesuatu yang nempel pada mehtod
   method itu adalah fungsi atau gabungan dari beberapa pengoperasian'''
'''abstarack -> mentah'''









