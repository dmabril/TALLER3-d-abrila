# guarderia.py

from models.boa import Boa  
from models.huron import Huron

class Guarderia:
    def __init__(self):
        # Crear 2 boas
        self.boas = [
            Boa("Morita", 1.5, 2, "Brazil", 1.50),
            Boa("Snake", 3.0, 3, "Perú", 0.04)
        ]
        self.hurones = [
            Huron("Gregorio", 2.0, 4, "USA", 2000.10),
            Huron("Frodo", 2.5, 2, "Canada", 1000.10)
        ]

    def alimentar_boa(self, boa, cantidad_ratones):
        try:
            if boa is None:
                return "Esta Boa no existe!"
            
            # Verificar si la boa es válida y está en la lista
            if boa not in self.boas:
                return "Esta Boa no existe!"
            
            # Alimentar a la boa y manejar su respuesta
            return boa.alimentar(cantidad_ratones)
        
        except Exception as e:
            # Captura de cualquier error inesperado
            return f"Error inesperado: {e}"

