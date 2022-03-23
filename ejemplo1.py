class Persona:
    def __init__(self, name:str, lastname:str, age:int, hobbies:str) -> None:
        self._name = name
        self._lastname = lastname
        self._age = age
        self._hobbies = hobbies
    
    def hablar(self):
        print(f"Hey my name is {self._name} {self._lastname.capitalize()}, I'm {self._age} years old \n I love {self._hobbies}")

##########
from Primermodulo import Persona
x= Persona("Juan", "Perez", 22, "voley")
x.hablar()
