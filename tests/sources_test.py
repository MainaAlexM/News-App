import unittest
from app.models.news import News



class SourcesTest(unittest.TestCase):

    '''
    Sources class behavior Test
    '''

    def setUp(self):
        '''
        Set up Test
        '''
        self.new_source = News("cnn", "CNN")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, News))