class Talk:
    """A class for Talks"""
    def __init__(self,speaker,title,tags): #__init__ double underscore is called dunder, init is called whenever object is to be created. its ike constructor
        self.speaker = speaker #self is alternative of this but we can use anything as self but it should be present 
        self.title = title
        self.tags = tags
    def get_speaker_firstname(self):
        return self.speaker.split()[0]
    def get_tags(self):
        return self.tags.split(',')
bdf1 = Talk('Guido van Rossum','The History of python','Python,history,c,advanced')
bdf1.get_tags()
bdf1.get_speaker_firstname()
print(bdf1.speaker)
print(bdf1.title)
print(bdf1.tags)
talk = Talk('Arun K P','python,bioscience','bio')
talk.x = 1
talk.y = 'a'

