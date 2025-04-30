import datetime

from Animal import Animal
from Cat import Cat

dog = Animal("Dog", "Male")
print(dog.race)
print(dog.sex)

cat = Cat("Cat", "Female")
print(cat.race)
print(cat.sex)
cat.set_race("Pussy")
print(cat.race)

print(datetime.datetime.now())