class Persona:
    def __init__(self, apellido:str, nombre:str):
        self._apellido = apellido
        self._nombre= nombre


    def hablar(self):
        return print(f'El Apellido y Nombre ingresado es {self._nombre} {self._apellido}')


from moduloClases import Persona

persona = Persona('Menem', 'Carlos')

print(persona.hablar())
