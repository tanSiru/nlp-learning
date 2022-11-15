import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords

#TERMS
#tokenize: a form of grouping things
#tokenize: word tokenize(seperates by word) & sentence tokenize(seperates by sentences)

#lexicon: words and their meaning(this also depends on context)
#investor VS english
# investor 'bull' =  someone who is positive about the market
# english 'bull' =  an animal 

#corpora: body of text. ex:medical journal, presidential speeches
#stopwords: words that may have sarcastic meaning so it is ignored, words that don't add meaning to the text(filler words)

example_sent = "This is an example showing stop words filtiration."
stop_word = set(stopwords.words('english'))

word = word_tokenize(example_sent)
# filtered_sent = []
# for w in word:
#     if w not in stop_word:
#         filtered_sent.append(w)

filtered_sent = [w for w in word if w not in stop_word]

#stemming: to take the root of a word
#exampl: stemming 'riding' would give 'rid'
#why stem: because there will be many variations of a word by the meaning of it won't change,
#so we can just group by the stem 
#example: I was taking a ride in the car & I was riding in the car 
from nltk.stem import PorterStemmer
ps = PorterStemmer()
example_words = ['python','pythoner','pythoning','pythoned','pythonly']
def stemming():
    stemmed_words = {}
    for w in example_words:
        stemmed_words[w] = ps.stem(w)

new_text = 'It is very important to be pythonly while pythoning you are using python. All pythoners have pythoned poorly at least once.'
def stemming_sent():
    words = word_tokenize(new_text)
    for w in words:
        print(ps.stem(w))

from nltk.corpus import state_union 
# PunktSentenceTokenizer: a unsupervised machine learning sentence tokenizer, it comes pre-trained but it can re-trained
from nltk.tokenize import PunktSentenceTokenizer # a different tokenizer


#train_set: used in models and algorithm to predict outcomes
#test_set: used to test the accuracy or efficiency of the train_set
train_set = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_set)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

'''
1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP$	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP$	Possessive wh-pronoun
36.	WRB	Wh-adverb
'''

def process_content(text):
    try:
        #the texts will be in setences since sentence tokenized in 'tokenized'
        for i in text:
            words = word_tokenize(i)
            #this will return a tuple of the word with the speech tag
            tagged = nltk.pos_tag(words)


            #"Chunk" can be any name,doesn't really mattern 
            #"Chunk" is just what it will be called when the chunk is found
            #put what needs to found in {}
            #when any form of pos is mentioned, use <>
            #<RB.>: RB followed by any character
            #RB.?: any form of a adverb
            #<RB.?>*: if there is any, any form of a adverb and we're finding 0 or more of these
            #<NNP>+: requiring there to be a NNP(1 or more )
            #<NN>?: a possible NN
            #<NNP > <NN >?: a MUST NNP followed by a POSSIBLE NN 
            # chunkGram = r""" Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
            #<.*>+: 1 or more of anything, basically chunks everything
            #}{: chinking, what we want to keep out
            #<VB.?|IN|DT>+: get rids of any these 
            chunkGram = r""" Chunk: {<.*>+}
                            }<VB.?|IN|DT|TO>+{"""

            #search more on this
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked  = chunkParser.parse(tagged)

            #matplotlib is needed for this(maybe idk)
            chunked.draw()

    except Exception as e:
        print(str(e))



#chunking: finding/identifying the parts of speech and short phrases(usually noun phrases)
#in nltk chunking is spliting and grouping different categories of tokens
#it is basically finding the modifiers/descriptive words surronding a noun
#learn more on regular expression

def named_entity_rec(text):
    try:
        for i in text[5:]:
            words = word_tokenize(i)
            tagged = nltk.pos_tag(words)


            #search NE type examples
            #binary: it doesn't specify which type of ne it is and it just groups all ne together
            namedEnt = nltk.ne_chunk(tagged,binary=True)

            namedEnt.draw()

    except Exception as e:
        print(str(e))

# named_entity_rec(tokenized)

from nltk.stem import WordNetLemmatizer#similar to stemming except actual words will be returned

lem = WordNetLemmatizer()
#default pos is 'n'(noun)
word1=lem.lemmatize('better',pos='a')
word2=ps.stem('cacti')

print(word1,'lem')
print(word2,'ps')

print(nltk.__file__)