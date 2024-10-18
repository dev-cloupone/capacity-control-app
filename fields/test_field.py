import io
import unittest
from django.test import TestCase, override_settings
from .models import Field
from .import_data import import_fields

@override_settings(SETTINGS_MODULE='your_app.test_settings')
class ImportFieldsTestCase(TestCase):
    def setUp(self):
        # Simular dados CSV como uma string
        self.csv_data = "Talhão,Hectare\n" \
                        "Talhão1,10\n" \
                        "Talhão2,20\n"

    def test_import_fields(self):
        # Simular dados CSV como uma string
        csv_file = io.StringIO(self.csv_data)

        # Chamar a função de importação
        import_fields(self.csv_data)

        # Verificar se os dados foram inseridos corretamente no banco de dados
        self.assertEqual(Field.objects.count(), 2)

        field1 = Field.objects.get(name="Talhão1")
        self.assertEqual(field1.size, 10)

        field2 = Field.objects.get(name="Talhão2")
        self.assertEqual(field2.size, 20)

if __name__ == '__main__':
    unittest.main()