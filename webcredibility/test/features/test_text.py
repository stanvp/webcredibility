# -*- coding: utf-8 -*-
'''
Created on Feb 5, 2012

@author: stanvp
'''
import unittest

from webcredibility.features.text import *
from webcredibility.model import *

class TestText(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_punctuation_marks(self):
        document = Document(content="This is simple text, with two question marks? One dot. Two commas, and one exclamation-question!?")
        
        self.assertEqual(punctuation_marks(document), {'#questions': 2, '#exclamations': 1, '#commas': 2, '#dots': 1})
        
    def test_part_of_speach(self):
        document = Document(content="This is simple text, with two question marks? One dot. Two commas, and one exclamation-question!?")
        print part_of_speach(document)
        self.assertEqual(part_of_speach(document), {'#questions': 2, '#exclamations': 1, '#commas': 2, '#dots': 1})            

    def test_spelling_errors(self):
        document = Document(content="Helo what is youre name?")
        
        self.assertEqual(spelling_errors(document), {'#spelling_errors': 2})  
        
    def test_text_complexity(self):        
        document1 = Document(content="Qualitative dimensions of text complexity, such as levels of meaning, structure, language conventionality and clarity, and knowledge demands. Lexile codes provide more information about a book's characteristics, such as its developmental appropriateness, reading difficulty, and common or intended usage.")      
        document2 = Document(content="Helo what is youre name?.")
        
        self.assertEqual(text_complexity(document1), {'@text_complexity': 1.7870392631614347})        
        self.assertEqual(text_complexity(document2), {'@text_complexity': 0.8450980400142567})
        
    def test_sentiment(self):
        document = Document(content="The movie was great!")
        
        self.assertEqual(sentiment(document), {'?polarity': 1})
        
        text = """
plot : a young man who loves heavy metal music and especially the band steel dragon , to whom he's devoted a tribute band in which he sings , gets launched into stardom when the real group get rid of their lead singer and call on him to take his place . 
critique : i'm a sucker for movies like this . 
a young man with a humble background and lofty dreams , works hard , devotes the time , the energy and the patience , and ultimately hits it big-time . 
in the case of this film , our boy loves a certain heavy metal band and as luck would have it ( yup , luck always finds its way into these types of equations , although generally tied very closely to hard work ) , they need a new singer . 
his entry and adaptation to the whole " rock 'n roll " lifestyle fills the rest of the film and is really fun to watch . 
although i will preface this by saying that one thing that would definitely enhance your appreciation for this film is your own love ( or past love ) of heavy metal music and the whole scene around it . 
metal was one of my first loves as a teen and even though the genre of music isn't that prominent anymore , i still check out my motley crue , twisted sister and anthrax cds every now and again . 
that's not to say that you won't like this film if you don't like the music , but the music and live performances from the band , play a big part in the movie , and i for one , had a blast watching and listening to it all . 
but the even greater draw in this film is the standout performance given here by mark wahlberg . 
wow , hand this fella some major props , as he totally becomes this heavy metal geek/god ( incidentally , metal god was the film's original title , and a much better one if you ask me ) . 
he is this movie and i was quite taken by his character pretty much the whole way through . 
he came off like a regular guy with extremely passionate goals and work ethic , who was willing to do anything in order to fulfill his dreams . 
aniston was also surprisingly good as the girlfriend ( and the romance angle between them was sweet ) , but she didn't pull me in hard enough during their emotional scenes . 
i was also impressed by some of the " real " musicians who played in the film ( zakk wylde from ozzy osbourne , jeff pilson from dokken , stephan jenkins from third eye blind , blas elias from slaughter ) , but actor dominic west as kirk cuddy made the biggest impression among the band members . 
it's to note that this film was based on a real-life tale of a young man who used to sing in a judas priest cover band and then went on to become their actual singer ( their original singer also admitted to being gay , as in this film ) . 
just for the record , i'm certainly not recommending this film for its originality or surprise elements , since most of this stuff has already been covered in some way or another in other movies , but because it's a fun , uplifting , well-paced movie with a solid central showing by wahlberg and energetic live performances . 
oh yeah , and for those who dig the " heavier " side of music , the soundtrack also rocks ! ! 
you see . . . dreams 
can come true . . . 
where's joblo coming from ? 
almost famous ( 8/10 ) - blow ( 8/10 ) - boogie nights ( 9/10 ) - detroit rock city ( 8/10 ) - girlfight ( 6/10 ) - goodfellas ( 10/10 )         
        """
        document1 = Document(content=text)
        
        self.assertEqual(sentiment(document1), {'?polarity': 1})                

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()