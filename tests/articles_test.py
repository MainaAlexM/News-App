import unittest
from app.models.articles import Articles

class TestArticles(unittest.TestCase):
    '''
    Test class that defines test cases for the articles class behaviors.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_article =  Articles("BBC", "Kate Stallman", "Ukraine's night", "/bbc", "/image", "18-04-2022", "Something", "Loading") # create an articles object


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
