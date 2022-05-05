class Source:
    '''
    Source class to define source objects
    '''

    def __init__(self,id,name,category):
        self.id = id
        self.name = name
        self.category = category

class Article:
    '''
    Article class to define article objects
    '''

    def __init__(self, name, author, title,  description, link, image, publishDate):

        self.name = name 
        self.author = author
        self.title = title
        self.description = description
        self.link = link
        self.image = image
        self.publishDate = publishDate

class Top:
    '''
    Top headlines class to define headlines objects
    '''

    def __init__(self, source, author, title,  description, link, image):

        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.link = link
        self.image = image