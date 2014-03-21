from django.test import TestCase
from unittest import skip
from pollresults.forms import LeadForm

# Create your tests here.

class IndexTestGetCase(TestCase):
    
    def setUp(self):
        self.response = self.client.get('/')
    
    def test_index_should_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_should_use_home_template(self):
        self.assertTemplateUsed(self.response, 'pollresults/home.html')

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

@skip('no real tests here yet')
class RegisterTestGetCase(TestCase):

    def test_that_a_valid_form_saves_a_user(self):
        # test that a valid form saves a user
        # test that the 'registered' key is set to true
        pass

    def test_that_a_valid_form_redirects(self):
        # you are currently not doing this, which is very bad form
        # it's good form to redirect after successful form submission
        # in order to prevent people from submitting the same form over
        # and over again
        pass

    def test_that_an_invalid_form_does_something(self):
        # test that and invalid form redericts to the same page
        # test that the 'registered' key is set to false
        # we don't need to test that this doesn't save a user, because then 
        # we'd be testing django
        pass
    

@skip('no real tests here yet')
class LoginTestCase(TestCase):

    def test_that_a_valid_active_user_can_login(self):
        # test they get logged in
        # test they get sent back to home
        pass

    def test_that_an_inactive_user_doesnt_go_to_index(self):
        pass

    def test_that_an_invalid_form_loads_same_page_with_errors(self):
        pass

class LogoutTestCase(TestCase):

    def test_a_logged_in_user_gets_logged_out(self):
        pass

    def test_a_logged_out_user_does_something_predictable(self):
        # remember you need to test every line of code
        # one of your lines is the @login_required decorator
        # write a test making sure that the right thing happens when this is true
        # write another test making sure the right thing happens if false!
        # right now, if I go to /log_out and I'm not logged in I get an error
        pass
