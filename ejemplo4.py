class Persona:
    def __init__(self, name:str, lastname:str):
        self.name = name
        self.lastname = lastname

    def Hablar(self):
        print(f'Hola mi nombre es {self.name} y mi apellido es {self.lastname}')
		
##########################################

from clase_importa_modulo import Persona

persona1 = Persona('Juan', 'Perez')
persona1.Hablar()
