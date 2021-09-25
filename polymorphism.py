class animal():
    def animal_Sound(self):
        print("The animal makes a sound \n")
class pig(animal):
    def animal_Sound(self):
        print("The pig says: wee wee \n")
class dog(animal):
    def animal_Sound(self):
        print("The dog says: bow wow \n")

a1=animal()
pig_=pig()
dog_=dog()
a1.animal_Sound()
pig_.animal_Sound()
dog_.animal_Sound()