class Persona:
    def __init__(self, nombre:str, apellido:str):
        self._nombre = nombre
        self._apellido = apellido
    
    def __str__(self) -> str:
        return f"Me llamo {self._nombre} {self._apellido}"
    
    def hablar(self, frase:str):
        print(frase)


#######

from paquete import Persona

persona_1 = Persona("Juan", "Perez")

print(persona_1)
persona_1.hablar("Puedo hablar")
