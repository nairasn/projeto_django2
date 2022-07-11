from django.test import TestCase
from dados.models  import Cliente

class ClienteTestCase(TestCase):
        
    def setUp(self):
        Cliente.objects.create(
            nome='Naira',
            idade=29
        )
                
    def test_return_str(self):
        c1 = Cliente.objects.get(nome='Naira')
        self.assertEquals(c1.__str__(), 'Naira')