class Articles:
    '''
    method to get all the articles
    '''        
    def __init__(self, source_name, author, title, url, url_to_image, published_at, description, content):
        '''
        Initializing Articles object
        '''
        self.source_name=source_name
        self.author=author
        self.title=title
        self.url=url
        self.url_to_image=url_to_image
        self.published_at=published_at
        self.description=description
        self.content=content
