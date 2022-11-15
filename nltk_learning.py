from nltk.tokenize import sent_tokenize, word_tokenize
# import nltk

# idea: make 2 lists that shows the non-stem and stem words and mark it with stem and non-stem

text = 'Hello. I went out with my friends the other day'
text2 = "Last night, I went to Mrs. Martinez's housewarming. It was a disaster."
text3 = 'Enchanté, comment allez-vous? Tres bien. Mersi, et vous?'

#tokenize:split it into smaller parts- paragraphs to sentences, sentences to words. 
# We have two kinds of tokenizers- for sentences and for words.

#Pt 1,  NLTK Sentence Tokenizer
token1 = sent_tokenize(text) # sent_tokenize:sentence tokenizer, splits its into smaller parts
token2 = sent_tokenize(text3,'french') # to tokenize other languages

abbreviations = "She holds an MDS. in Oral Pathology"

token3 = sent_tokenize(abbreviations) #issues when there is abbreviations

#Pt2, NLTK Word Tokenizer
token4 = word_tokenize(text2)  # takes the sentence and break it down into words
token5 = word_tokenize(text3, 'french') #to word tokenize other languages

#Finding Synonyms from NLTK wordnet
from nltk.corpus import wordnet
o = 3
i=0
a=0

syn1 = wordnet.synsets('love')
syn1_1 = syn1[o].definition()
syn1_examples = syn1[o].examples()

syn2=wordnet.synsets('life')
syn2_1=syn2[i].definition()
syn2_examples=syn2[i].examples()

syn3 = wordnet.synsets('AI')
syn3_1=syn3[a].definition()
syn3_examples=syn3[a].examples()

happy = wordnet.synsets('happy')

stem_sentence = word_tokenize(text)

def sentence_stem():
    for word in stem_sentence:
        print(f"{word}: {ps.stem(word)}")

#Stemming in NLTK: removing the words suffix and returning it to its root
from nltk.stem import PorterStemmer,WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
love = ps.stem('loving')
run = ps.stem('running')

#Lemmatization:group together inflected forms of a word.
#links words with similar meanings to one word and maps various words onto one root.

#stemming can create words that do not actually exist
identify = ps.stem('indetify')
#Python lemmatization will only ever return words that do exist. lemmas are actual words.
identify2 = lemmatizer.lemmatize('identify')

belief = lemmatizer.lemmatize('believes')
belief2 = ps.stem('believes')

#Using Python lemmatization to find nouns
# pos is a speech parameter, which is noun by default. 
# This means Python will try to find the closest noun.
cross = lemmatizer.lemmatize('crossing', pos='n')  # noun
# closest verb
cross2 = lemmatizer.lemmatize('crossing', pos='v')  # verb
#closest adjective
cross3 = lemmatizer.lemmatize('crossing', pos='a')  # adjective
#closest adverb
cross4 = lemmatizer.lemmatize('crossing', pos='r')  # adverb

#Since Python consider what type of word it is(noun,verb,adjective),
#it needs to know the context of the word
red = lemmatizer.lemmatize('redder', 'a')

#To get the list of synonyms:
synonyms = []
for syn in wordnet.synsets('good'):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

#To get the list of antonyms, we first need to check the lemmas- are there antonyms?
antonyms = []
for syn in wordnet.synsets('depressed'):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

#Stemming Words from Other Languages
from nltk.stem import SnowballStemmer
lan = SnowballStemmer.languages

rom_stemmer = SnowballStemmer('romanian')
rom = rom_stemmer.stem('englezească')  # English

# filter NLTK stop words from text before processing it.
from nltk.corpus import stopwords
stopwords=set(stopwords.words('english'))
# stopword = stopwords.words('english')
example_text = "Today is a great day. It is even better than yesterday. And yesterday was the best day ever!"
text_tokenize = word_tokenize(example_text)
wordsFiltered = []
filteredwords = []
def filtered():
    for w in text_tokenize:
        if w not in stopwords:
            wordsFiltered.append(w)
        else:
            filteredwords.append(w)
    print(wordsFiltered)
    print(filteredwords)

#NLTK can classify words as verbs, nouns, adjectives, and more
#Image saved in 'teaching my self' named 'words_nltk_can_classify'
from nltk.tokenize import PunktSentenceTokenizer
# import nltk
from nltk.tag import pos_tag

word_pos = []
ppp = sent_tokenize(text)
def word_posed():
    for i in ppp:
        x = nltk.pos_tag(word_tokenize(i))
        word_pos.append(x)
    print(word_pos)

tokenss = word_tokenize('hello hi')
for word,tag in pos_tag(tokenss):
    print(word,tag)





