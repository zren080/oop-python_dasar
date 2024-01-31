class Karakter(object):



    def __init__(self, inputNama, inputDarah, inputLevel, inputSkill, inputSenjata, inputDamage, inputVest):



        self.nama    = inputNama

        self.darah   = inputDarah

        self.level   = inputLevel

        self.skill   = inputSkill

        self.senjata = inputSenjata

        self.damage  = inputDamage

        self.vest    = inputVest



    def menyerang(self, lawan):

        print("\n" + self.nama, "Menyerang", lawan.nama, "dengan", self.senjata + ",", lawan.nama, "terkena", self.damage, "damage")

        lawan.diserang(self)



    def diserang(self, lawan):

        damageSerangan = lawan.damage

        self.darah    -= damageSerangan

        print(self.nama, "diserang", lawan.nama, "dan mendapat", lawan.damage, "damage ( Darah", self.nama, "tersisa", self.darah, ")")



hayato = Karakter("Hayato", 200, "Max", 3, "Scar", 35, 350)

kelly  = Karakter("Kelly", 200, "Max", 2, "AWM", 150, 350)



while True:



    hayato.menyerang(kelly)

    kelly.menyerang(hayato)



    if hayato.darah <= 0:

        print("\n=================== Hayato Mati ===================")

        break

    elif kelly.darah <= 0:

        print("\n=================== Kelly Mati ===================")

        break