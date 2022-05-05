import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('ABC News','George Washington','The fall of the Kingdoms','lorem ipsum','www.wdhd.com','www.whjd.com','2020-09-13')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))