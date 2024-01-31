class Hero:

    # variabel statik -> yang nempel pada class(Hero)
    jumlah = 0

    def __init__(self,nama,health):
        
        # instance variabel -> yang nempel pada objek() 
        self.nama = nama
        self.health = health

        # variabel instance private
        self.__private = 'private'
        # variabel instance protected 
        self._protected = 'protected'

zren = Hero('zren',100)

print(zren.__dict__)
print(zren._protected)
zren._protected = 'testing'
print(zren.__dict__)
print(zren._protected)

'''
print(zren.__dict__)
zren.__private = 'testing'
print(zren.__dict__)
print(zren.private)

{zre.__private} jika membuat variabel diluar class
maka dia akan mengoreksi ke arah variabel luat class'''

"""intinya kalo protected itu value nya jangan dirubah / hati2 terhadap variable / valuenya tsb, 
kalo private jelas jangan di acak2, soalnya di python sendiri ga ada variable khusus buat di private/protected
,beda sama di bahasa sebelah"""