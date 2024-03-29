class Animal:
    def __init__(self,name):
        self.name=name
    def talk(self):
        raise NotImplementedError("error")
class cat (Animal):
    def talk(self):
        return "meow"
class dog (Animal):
    def talk(self):
        return "woof"

animals=[
    cat("pawan"),cat("shwetabh"),dog("abhishek")
    ]
for animal in animals:
    print(animal.name,"-",animal.talk())