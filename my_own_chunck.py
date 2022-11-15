import re
import random
from nltk.tokenize import word_tokenize
import nltk
from nltk.tokenize import PunktSentenceTokenizer

text = "abnormally soft absentmindedly accidentally actually adventurously afterwards almost always annually anxiously arrogantly awkwardly"
tokenized = word_tokenize(text)

def test(token):
    tagged = nltk.pos_tag(token)
    #the words/txts under 's' that will appear is just the other text that has been
    #the words/txts under 'chunks' is what fits what we are trying to find
    #noticed that a comma isn't required
    #try others such as RBS to test *
    chunkGram = r""" VBZ: {<JJ>+}
                        RB: {<RB>*}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked  = chunkParser.parse(tagged)
    print(chunked)
    chunked.draw()
    

test(tokenized)
