import io
import unittest
from django.test import TestCase, override_settings
from .models import Activity
from .import_data import import_partner

@override_settings(SETTINGS_MODULE='your_app.test_settings')
class ImportpartnerTestCase(TestCase):
    def setUp(self):
        # Simular dados CSV como uma string
        self.csv_data = "Atividade,Tamanho,Valor atividade,Total atividade\n" \
                        "Atividade1,10,50,500\n" \
                        "Atividade2,20,100,2000\n"

    def test_import_partner(self):
        # Simular dados CSV como uma string
        csv_file = io.StringIO(self.csv_data)

        # Chamar a função de importação
        import_partner(csv_file)

        # Verificar se os dados foram inseridos corretamente no banco de dados
        self.assertEqual(Activity.objects.count(), 2)

        activity1 = Activity.objects.get(name="Atividade1")
        self.assertEqual(activity1.size, 10)
        self.assertEqual(activity1.value, 50)
        self.assertEqual(activity1.total, 500)

        activity2 = Activity.objects.get(name="Atividade2")
        self.assertEqual(activity2.size, 20)
        self.assertEqual(activity2.value, 100)
        self.assertEqual(activity2.total, 2000)

if __name__ == '__main__':
    unittest.main()
