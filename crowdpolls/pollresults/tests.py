from django.test import TestCase
from pollresults.forms import LeadForm

# Create your tests here.

class IndexTestGetCase(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/')
    
    def test_index_should_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_should_use_home_template(self):
        self.assertTemplateUsed(self.response, 'pollresults/home.html')

    def test_should_have_lead_form(self):
        self.assertEqual(type(self.response.context['form']),LeadForm)
        self.assertContains(self.response, '<form')

class IndexTestPostCase(TestCase):
    
    def setUp(self):
        self.valid_params = {'first_name':'Donald',
                             'last_name':'Glover',
                             'email':'glover@badass.com'}

        self.invalid_params = {'email':"aaa"}


    def test_valid_should_redirect(self):
        response = self.client.post('/', self.valid_params, follow=True)
        self.assertRedirects(response,'success')

    def test_valid_should_use_success_template(self):
        response = self.client.post('/', self.valid_params, follow=True)
        self.assertTemplateUsed(response, 'pollresults/success.html')

    def test_invalid_should_not_redirect(self):
        response= self.client.post('/', self.invalid_params)
        self.assertEqual(response.status_code,200)

