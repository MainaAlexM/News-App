import unittest
from app.models import Top

class TopTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Top class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_top = Top('ABC News','George Washington','The fall of the Kingdoms','lorem ipsum','www.wdhd.com','www.whjd.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_top,Top))