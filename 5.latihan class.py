class Hero:
     
     def __init__(self,input_nama,input_health,input_attack,input_defense):
          self.nama = input_nama
          self.health = input_health
          self.attack = input_attack
          self.defense = input_defense

     def serang(self,lawan): # argumen "lawan boleh terserah" 
        print(self.nama + ' menyerang ' + lawan.nama)
        lawan.diserang(self, self.attack)

     def diserang(self,lawan,attack_lawan):
          print(self.nama + ' diserang ' + lawan.nama)
          attack_diterima = attack_lawan/self.defense
          print('serangang diterima : ' + str(attack_diterima))
          self.health -= attack_diterima
          print('darah ' + self.nama + ' tersisa ' + str(self.health))
          


vexana = Hero('Vexana',100,87,54)
tigrel = Hero('Tigreal',100,38,100)
#brody = Hero('Brody',100,89,34)

vexana.serang(tigrel)


'''float tidak bisa digabungkan dengan str 
harus dicasting menjadi str'''