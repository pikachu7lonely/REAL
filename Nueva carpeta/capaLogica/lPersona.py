from capaDatos.dPersona import DPersona

class LP:
    def __init__(self):
        self.dPersona = DPersona()

    def mostrarPersona(self):
        return self.dPersona.mostrarPersona()
    
    def insertarPersona(self, persona: dict):
        return persona 
    
    def insertarPersona(self, persona: dict):
        self.dPersona.insertarPersona(persona)
        