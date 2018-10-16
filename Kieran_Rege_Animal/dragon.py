from animal import Animal
class dragon(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health=170
    def fly(self):
        self.health-=10
        return self
    def displayHealth(self):
        print self.health
        print ("I am a Dragon")
        return self
dr=Dragon("Dragon1")
dr.fly().fly().displayHealth()