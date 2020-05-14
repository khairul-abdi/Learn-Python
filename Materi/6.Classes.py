class Dog:

  def __init__(self, name, age, fulcolor):
    self.name = name
    self.age = age
    self.fulcolor = fulcolor

  def bark(self, str):
    print("BARK!" + str)

mydog = Dog("Fido", 24, "red")

print(mydog.name)
