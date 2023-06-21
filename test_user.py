from unittest import TestCase
from AcmeWinesOrderAnalyzer import Users 


obj = Users("", "", "", "")
class TestUser(TestCase):
   
   
    def test_age_should_be_greater_than_21(self):
       
       user=obj.is_21_or_older("01/01/2001")
       self.assertTrue(user)

    
    def test_age_should_not_be_less_than_21(self):
       
       user=obj.is_21_or_older("01/01/2023")
       self.assertFalse(user)

    def test_state_should_not_be_in_restricted_states(self):
       
       user=obj.is_restricted_state("FL")
       self.assertTrue(user)
    
    def test_if_state_is_in_restricted_states(self):
       
       user=obj.is_restricted_state("CA")
       self.assertTrue(user)

    def test_if_zipcode_has_a_consecutive_number(self):
       
       user=obj.check_consecutive_numbers("12345")
       self.assertTrue(user)
    
    def test_if_zipcode_has_not_a_consecutive_number(self):
       
       user=obj.check_consecutive_numbers("15824")
       self.assertFalse(user)

    def test_birthday_should_not_be_on_1st_monday_of_month(self):
       
       user=obj.is_first_monday("06/12/2023")
       self.assertFalse(user)
    
    def test_if_birthday_on_1st_monday_of_month(self):
       
       user=obj.is_first_monday("06/05/2023")
       self.assertTrue(user)
    
    def test_email_should_be_valid(self):
       
       user=obj.is_valid_email("tzirw@example.com")
       self.assertTrue(user)
    
    def test_email_should_not_be_valid(self):
       
       user=obj.is_valid_email("acmewines.com")
       self.assertFalse(user)
    
    