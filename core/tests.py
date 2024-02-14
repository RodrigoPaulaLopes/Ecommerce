from django.test import Client, TestCase


class IndexTest(TestCase):
    
    def setUp(self) -> None:
        client = Client()
        
    def tearDown(self) -> None:
        pass
        
    def index_status_200(self):
        
        resp = self.client.get('/')
        
        self.assertEquals(resp.status_code, 200)
        
    def index_template_used(self):
     
        resp = self.client.get('/')
        
        self.assertTemplateUsed(resp, 'index.html')



