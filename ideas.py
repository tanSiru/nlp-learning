"""
IDEA: 
take 2 paragaphs and compare their similarity by tokenizing their sentences
from the previously made websites by watching techwithtim, sotre some user paragraphs in their database
and use a get requests to get their paragraphs then use spacy and nltk to analyze their sentiments, similarity etc
add my own custom pipeline that analyze sentiments
"""

p1 = """
Dave watched as the forest burned up on the hill, only a few miles from her house. The car had been hastily packed and Marta was inside trying to round up the last of the pets. Dave went through his mental list of the most important papers and documents that they couldn't leave behind. He scolded himself for not having prepared these better in advance and hoped that he had remembered everything that was needed. He continued to wait for Marta to appear with the pets, but she still was nowhere to be seen.
"""

p2="""
The red ball sat proudly at the top of the toybox. It had been the last to be played with and anticipated it would be the next as well. The other toys grumbled beneath. At one time each had held the spot of the red ball, but over time they had sunk deeper and deeper into the toy box.
"""

"""
Metadata: the datas describing a file
ex: the metadata of a music file might it's size, date created, author, title, length 
"""

#Anything repeated more than once and uses the same logic is called a iteration
# for i in (1,2,3,4,5):
#     print(i)

"""
Iterator is an object which contains countables values  
it is used to iterate over iterable objects like list, tuples, sets, etc.


iter() keyword is used to create an iterator containing an iterable object.
next() keyword is used to call the next element in the iterable object.
After the iterable object is completed, to use them again reassign them to the same object.
"""


# iter_list = iter(['Geeks', 'For', 'Geeks'])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))

"""
It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in a defined function. 
Generators are implemented using a function. Just as iterators, generators also follow lazy evaluation. 
Here, the yield function returns the data without affecting or exiting the function.
It will return a sequence of data in an iterable format 
where we need to iterate over the sequence to use the data
 as they won’t store the entire sequence in the memory.
"""

def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i
  
  
a = sq_numbers(3)
  
print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))