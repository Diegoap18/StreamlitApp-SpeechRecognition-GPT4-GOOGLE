'''
This script is to high light the most important words in text.
this way you can identify on front-end the most popular word and also define a context
for words.

Author Diego A Pereira.
'''

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
stop_words = set(stopwords.words('portuguese'))


def highlight_important_words(text):
    ''' This Function is reponsible to highlight the text from 
    frequence of words, counts the words and most find is showed on front end.'''
    texto = text
    text1 = re.sub(r'[^\w\s]', '', texto)
    words = word_tokenize(text1)
    fdist = FreqDist(words)
    important_words = [word for word, freq in fdist.most_common(10) if word not in stop_words]
    
    return important_words
    

def text_highlights(texto):
    ''' This Function is reponsible to highlight the text from 
    frequence of words, counts the words and most find is showed on front end. include also the categorical terms that if found
    will be in evidence on text.'''
    categorical_terms = ['google','gpt','chatgpt', 'speech']
   
    for term in categorical_terms:
        texto = re.sub(term, f"***{term}***", texto)

    return texto
    
def text_highlights_html(texto):
    ''' This Function is reponsible to highlight the text from 
    frequence of words, counts the words and most find is showed on front end. this have proposal the return in HTML parameters.'''
    categorical_terms = ['google','gpt','chatgpt', 'speech']
    
    for term in categorical_terms:
        texto = re.sub(term, f"<strong>{term}<strong/>", texto)

    return texto