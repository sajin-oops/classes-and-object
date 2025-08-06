class Dog:
    species = "Golden Retriever"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} say's Woof!")

dog_1 = Dog("Milo",1)
dog_2 = Dog("Floria",2)

#Accessing attributes
print(f"{dog_1.name} is a {dog_1.species} and he is {dog_1.age} years old. ")
dog_1.bark()
print(f"{dog_2.name} is a  {dog_2.species} and he is {dog_2.age} years old.")
dog_2.bark()

'''
Milo is a Golden Retriever and he is 1 years old. 
Milo say's Woof!
Floria is a  Golden Retriever and he is 2 years old.
Floria say's Woof!
'''

