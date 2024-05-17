class animal : 
    def __init__(self ,habitat):
        self.habitat = habitat

    def prih(self):
        print(self.habitat)


class dog(animal):
    def __init__(self):
        animal.__init__(self , "kennel")




x = dog()
x.prih()