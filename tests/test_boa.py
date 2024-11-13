
import unittest
from models.boa import Boa

class Testboa(unittest.TestCase):

    def setUp(self):
        
        self.boa = Boa(  nombre = "Morita"
                         , peso = 1.5
                         , edad = 2
                         , pais_origen = "Brazil"
                         , impuestos = 20500.0
                        )

   
        
    def test_hacer_sonido(self):
        """Prueba el método hacer_sonido."""
        self.assertEqual(self.boa.hacer_sonido(), "¡Tssss!")




    def test_calcular_flete(self):
        self.assertEqual(self.boa.calcular_flete(), 30750) #Este valor es correcto
        #self.assertEqual(self.boa.calcular_flete(), 30750.1) #Este valor es incorrecto 

    

    def test_calcular_flete_negativo(self):

        self.boa = Boa(  nombre = "Morita"
                         , peso = 1.5
                         , edad = 2
                         , pais_origen = "Brazil"
                         , impuestos = -20500.0
                           )
        self.assertEqual(self.boa.calcular_flete(), -30750.0) #Este valor es correcto
        #self.assertEqual(self.boa.calcular_flete(), 30750.0) #Este valor es incocorrecto
        



    def test_calcular_flete_zero(self):
        self.boa = Boa(  nombre = "Morita"
                         , peso = 1.5
                         , edad = 2
                         , pais_origen = "Brazil"
                         , impuestos = 0
                           )

        self.assertEqual(self.boa.calcular_flete(), 0) #Este valor es correcto
        #self.assertEqual(self.boa.calcular_flete(), 30750.0) #Este valor es Incorrecto



    
    def test_getter_cantidad_ratones_comidos(self):
        self.assertEqual(self.boa.cantidad_ratones_comidos, 0)



    def test_setter_cantidad_ratones_comidos(self):
        self.boa.cantidad_ratones_comidos = 11
        self.assertEqual(self.boa.cantidad_ratones_comidos, 11)  #Este valor es Incorrecto, mas de 10 ratones 

    
    


if __name__ == '__main__':
    unittest.main()
