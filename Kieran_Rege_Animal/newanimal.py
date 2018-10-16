from animal import Animal
class monkey(Animal):
    def __init__(self, name):
        super(Monkey, self).__init__(name)
        self.health=200
    def swing(self):
        self.health+=10
        return self
    def displayHealth(self):
        print self.health
        print ("I am a Monkey")
        return self
m=Monkey("Monkey1")
m.swing().pet().fly()displayHealth()