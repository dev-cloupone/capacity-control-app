import io
import unittest
from django.test import TestCase, override_settings
from .models import Supplie
from .import_data import import_supplies

@override_settings(SETTINGS_MODULE='your_app.test_settings')
class ImportSuppliesTestCase(TestCase):
    def setUp(self):
        # Simular dados CSV como uma string
        self.csv_data = "Talhão,Tamanho,Insumo por hectare,Valor insumo,Total insumo\n" \
                        "Talhão1,10,5,50,500\n" \
                        "Talhão2,20,10,100,2000\n"

    def test_import_supplies(self):
        # Simular dados CSV como uma string
        csv_file = io.StringIO(self.csv_data)


        # Chamar a função de importação
        import_supplies(self.csv_data)

        # Verificar se os dados foram inseridos corretamente no banco de dados
        self.assertEqual(Supplie.objects.count(), 2)

        supplie1 = Supplie.objects.get(name="Talhão1")
        self.assertEqual(supplie1.field_size, 10)
        self.assertEqual(supplie1.quantity_per_hectare, 5)
        self.assertEqual(supplie1.value, 50)
        self.assertEqual(supplie1.total, 500)

        supplie2 = Supplie.objects.get(name="Talhão2")
        self.assertEqual(supplie2.field_size, 20)
        self.assertEqual(supplie2.quantity_per_hectare, 10)
        self.assertEqual(supplie2.value, 100)
        self.assertEqual(supplie2.total, 2000)

if __name__ == '__main__':
    unittest.main()
