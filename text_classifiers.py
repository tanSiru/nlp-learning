import nltk
#pickle: a way saving the training algorithim so we don't have to train our algorithim every time
import pickle,random
#we will use this to use various Scikit-learn algorithims within nltk classifier itself
from nltk.classify.scikitlearn import SklearnClassifier
from nltk.tokenize import word_tokenize
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB #google whatever the fuck these are
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import  LinearSVC, NuSVC

#we will inherit from this class
from nltk.classify import ClassifierI
#this will be used for the voting system
from statistics import mode

class VoteClassifier(ClassifierI):
    #__init__ will run no matter, where as other methods needs to be called to be used
    #we will pass a list of classifiers
    def __init__(self,*classifiers):
        self._classifiers = classifiers

    #we pass through feautures so they can be classified
    def classify(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        #returning who got the most votes
        return mode(votes)

    def confidence(self,features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        # this count the occurence of the most popular vote
        choice_votes = votes.count(mode(votes))
        conf = choice_votes/len(votes)
        return conf

#implement a spell checker so that it can the user input to do a proper analysis

#this will be a list of tuples,tuples will consist of the word and feature/tag and we use those to train our models

#this basically takes a whole review/texts and label it with either pos or neg
#the category is either pos or neg
# documents = [(list(movie_reviews.words(fileid)),category)
#             #this is basically a nested loops
#             #categorying pos or neg
#              for category in movie_reviews.categories()
#              #the specific category
#             for fileid in movie_reviews.fileids(category)]

"""
documents = []
for category in movie_reviews.category():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)),category))
"""

documents = []
allowed_words_type = ["J"]
all_words = []

short_pos=open("short/positive.txt","r",encoding='latin-1').read()
for i in short_pos.split('\n'):
    documents.append((i, "pos"))
    words = word_tokenize(i)
    pos = nltk.pos_tag(words)
    #w is the tuple with the word and pos
    for w in pos:
        #this is taking the first letter of the pos, and check if it is "J"(adjective)
        if w[1][0] in allowed_words_type:
            all_words.append(w[0].lower())


short_neg=open("short/negative.txt","r",encoding='latin-1').read()
for i in short_neg.split('\n'):
    documents.append((i, "neg"))
    words = word_tokenize(i)
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_words_type:
            all_words.append(w[0].lower())

with open("documents.pickle","wb") as f:
    pickle.dump(documents,f)


all_words = nltk.FreqDist(all_words)


#we will use this to train our model
#we train it by seeing whether the word is more common in negative or positive reviews
#this is actually wrong, this returns the first 3000 unique words
# word_features = list(all_word.keys())[:3000]

#to get the actual most common words
#feature: the process of organizing what we think is important what is not
word_features = [tupl[0] for tupl in all_words.most_common(5000)]

def find_feature(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        #this will return a boolean value
        #the boolean will be determined by whether the word is in the 3000 most common words(word_feature)
        features[w] = (w in words)
    return features

#before it was just a review ands it words and its category
#this will now be a dict with the word and a boolean value that is determined by whether they are in the most common words
#a tuple with the dict and the category
feature_set=[(find_feature(rev),category) for (rev,category) in documents]
random.shuffle(feature_set)

# with open("featuresets.pickle","wb") as f:
#     pickle.dump(feature_set,f)
#
# with open("word_features.pickle","wb") as f:
#     pickle.dump(word_features,f)

#we will use this for our algorithim
#if a word appears more in a negative review that the word is more important to a negative review and vice versa for positive reviews
training_set = feature_set[:10000]
#we give it the feature_sets and we ask the computer for the category as a means of testing
testing_set = feature_set[10000:]

#naivebayes is a very simple algorithim but is easily scalable
# classifier = nltk.NaiveBayesClassifier.train(training_set)

with open("naivebayes.pickle","rb") as classifier_f:
    #rb: read in bytes
    classifier = pickle.load(classifier_f)

#this returns the most important words in both pos and neg
# classifier.show_most_informative_features(15)

"""
from my understanding:
steps and purpose of a classifier:
1)group words together(whether by giving them a true or false or pos or neg)
2)use these to determine which group a word belongs to
    for example, if a user wanted to know whether boring has a negative or positive meaning/connotion
    a classifier takes "boring" and see whether it appears in pos or neg more 
    the purposee of the true or false is to first search through whether the word has a significant meaning
    if it does, then return which group it belongs to and how much pos or neg it is 
    if it doesnt, then it will return a value around 50% as way of saying no important meaning 
"""

def classifiers():
    with open("naivebayes.pickle","wb") as save_classifier:
        # wb: write in bytes
        #we pass what the classifier we want to save and where to save it
        pickle.dump(classifier,save_classifier)


    #you pass in the classifier you are using and the set it is testing against
    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training_set)

    with open("MNB_classifier.pickle","wb") as save_classifier:
        pickle.dump(classifier,save_classifier)

    # GAU_classifier = SklearnClassifier(GaussianNB())
    # GAU_classifier.train(training_set)
    # print("GAU Naive acc:",nltk.classify.accuracy(GAU_classifier,testing_set))

    BER_classifier = SklearnClassifier(BernoulliNB())
    BER_classifier.train(training_set)

    with open("BER_classifier.pickle","wb") as save_classifier:
        pickle.dump(BER_classifier,save_classifier)

    LogisticRegression_class = SklearnClassifier(LogisticRegression())
    LogisticRegression_class.train(training_set)

    with open("LogisticRegression_class.pickle","wb") as save_classifier:
        pickle.dump(LogisticRegression_class,save_classifier)

    SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
    SGDClassifier_classifier.train(training_set)

    with open("SGDClassifier_classifier.pickle","wb") as save_classifier:
        pickle.dump(SGDClassifier_classifier,save_classifier)

    LinearSVC_classifier = SklearnClassifier(LinearSVC())
    LinearSVC_classifier.train(training_set)

    with open("LinearSVC_classifier.pickle","wb") as save_classifier:
        pickle.dump(LinearSVC_classifier,save_classifier)

    NuSVC_classifier = SklearnClassifier(NuSVC())
    NuSVC_classifier.train(training_set)

    with open("NuSVC_classifier.pickle","wb") as save_classifier:
        pickle.dump(NuSVC_classifier,save_classifier)

def accuracy():
    print("Nltk Naive acc:",nltk.classify.accuracy(classifier,testing_set))
    print("MNB Naive acc:",nltk.classify.accuracy(MNB_classifier,testing_set))
    print("BER Naive acc:",nltk.classify.accuracy(BER_classifier,testing_set))
    print("LogisticRegression Naive acc:",nltk.classify.accuracy(LogisticRegression_class,testing_set))
    print("SGD Naive acc:",nltk.classify.accuracy(SGDClassifier_classifier,testing_set))
    print("LinearSVC Naive acc:",nltk.classify.accuracy(LinearSVC_classifier,testing_set))
    print("NuSVC Naive acc:",nltk.classify.accuracy(NuSVC_classifier,testing_set))



"""
the purpose of having different alogrithims is to have a voting system
each classifier will cast a vote, either pos or neg, this can raise both accuracy and reliability of our models
this also allows us to have a confidence parameter
7/7 said pos: 100% confidence, 3/7 said pos:low confidence
"""

classifiers()
accuracy()


# voted_classifier = VoteClassifier(classifier,MNB_classifier,BER_classifier,LogisticRegression_class,SGDClassifier_classifier,LinearSVC_classifier,NuSVC_classifier)
# print("My Naive acc:", nltk.classify.accuracy(voted_classifier, testing_set))

def sentiment(text):
    feats = find_feature(text)
    return  voted_classifier.classify(feats)