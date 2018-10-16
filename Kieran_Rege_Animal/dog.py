from animal import Animal
class dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health=150
    def pet(self):
        self.health+=5
        return self
d=Dog("Dog1")
d.walk().walk().walk().run().run().pet().displayHealth()