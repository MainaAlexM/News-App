import unittest
from newsApp.models.articles import Articles

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
        self.new_article =  Articles("","","","","") # create an articles object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_article.title,"")
        self.assertEqual(self.new_article.description,"")
        self.assertEqual(self.new_article.urlToImage,"")
        self.assertEqual(self.new_article.publishedAt,"")
        self.assertEqual(self.new_article.url,"")
