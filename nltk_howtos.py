from nltk.book import * #from NLTK's book module load all items
# print(text1) # to find infos for texts

#Searching Texts
#this will returns every time when a certain is used and the context of it
# monstrus = text1.concordance('monstrous')
# affection = text2.concordance('affection')
# lived = text3.concordance("lived")

#Concordance gives the occurence and context of a given word
#by using text.similar() we can find other words that appear in a similar range of contexts

# monstrous2 = text1.similar('monstrous')
# monstrous3 = text2.similar('monstrous')

#Examine contexts of multiple
# very_monstrous = text2.common_contexts(['very','monstrous']) #it will appear in the appear in the order the words

#Dispersion Plot is the location and instance a word has appeard in a text from when the word first appears

# text4_plot = text4.dispersion_plot(['citizens','democracy','freedom','duties','America']) #each stripe represents an instance of a word
#for this, the Python libraries Matplotlib and Numpy must be installed first

#A token is the technical name for a sequence of characters
# returns a set of a distinct vocabs in text3 in alphabetical order, since a (set) will only return unique values
text3_sort = sorted(set(text3))
text3_len = len(text3_sort)
text3_richness = len(set(text3))/len(text3) #this will return 6% which shows that only 6% of the words are distinct

def lexical_diversity(text):
    return len(set(text)) / len(text)
def percentage(count, total):
    return 100 * count / total
