# %%
# +
from nltk.stem import WordNetLemmatizer, SnowballStemmer
import nltk
from gensim.parsing.preprocessing import STOPWORDS
from nltk.probability import FreqDist
from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer
import os
import gensim
from nltk.corpus import stopwords
import os
from nltk.stem import SnowballStemmer
from nltk.stem.porter import *
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import matplotlib.style as style
import time
import nltk
import nltk
import numpy as np
import collections.abc
import os
import pandas as pd
import re
import numpy as np
import warnings
import string
from pandas.core.frame import DataFrame
from typing import Callable

def remove_line_breaks(text):
    text = text.replace('\r', ' ').replace('\n', ' ')
    return text

#remove punctuation
def remove_punctuation(text):
    re_replacements = re.compile("__[A-Z]+__")  # such as __NAME__, __LINK__
    re_punctuation = re.compile("[%s]" % re.escape(string.punctuation))
    '''Escape all the characters in pattern except ASCII letters and numbers'''
    tokens = word_tokenize(text)
    tokens_zero_punctuation = []
    for token in tokens:
        if not re_replacements.match(token):
            token = re_punctuation.sub(" ", token)
        tokens_zero_punctuation.append(token)
    return ' '.join(tokens_zero_punctuation)

def remove_special_characters(text):
    text = re.sub('[^a-zA-z0-9\s]', '', text)
    return text

def lowercase(text):
    text_low = [token.lower() for token in word_tokenize(text)]
    return ' '.join(text_low)

def remove_stopwords(text):
    stop = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    text = " ".join([word for word in word_tokens if word not in stop])
    return text

#remobe one character words
def remove_one_character_words(text):
    '''Remove words from dataset that contain only 1 character'''
    text_high_use = [token for token in word_tokenize(text) if len(token)>1]      
    return ' '.join(text_high_use)   

# %%
# Stemming with 'Snowball stemmer" package
def stem(text):
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    text_stemmed = [stemmer.stem(token) for token in word_tokenize(text)]        
    return ' '.join(text_stemmed)

def lemma(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    word_tokens = nltk.word_tokenize(text)
    text_lemma = " ".join([wordnet_lemmatizer.lemmatize(word) for word in word_tokens])       
    return ' '.join(text_lemma)


#break sentences to individual word list
def sentence_word(text):
    word_tokens = nltk.word_tokenize(text)
    return word_tokens
#break paragraphs to sentence token 
def paragraph_sentence(text):
    sent_token = nltk.sent_tokenize(text)
    return sent_token    


def tokenize(text):
    """Return a list of words in a text."""
    return re.findall(r'\w+', text)

def remove_numbers(text):
    no_nums = re.sub(r'\d+', '', text)
    return ''.join(no_nums)



def clean_text(text):
    _steps = [
    remove_line_breaks,
    remove_one_character_words,
    remove_special_characters,
    lowercase,
    remove_punctuation,
    remove_stopwords,
    stem,
    remove_numbers
]
    for step in _steps:
        text=step(text)
    return text   
def extracted_cell(train: DataFrame) -> DataFrame:
    """
Params:
train: Rows: Single-level Index: Integer
       Columns: Single-level Index: ['text: string', 'username: unknown', 'hashtags: unknown', 'created_at: unknown', 'user followers count: integer', 'replycount: integer', 'retweetcount: integer', 'likecount: integer', 'quotecount: integer', 'language: unknown', 'quotedtweet: unknown', 'inReplyToTweetId: float', 'inReplyToUser: unknown', 'mentionedUsers: unknown']

Returns:
Rows: Single-level Index: Integer
Columns: Single-level Index: ['text: string', 'username: unknown', 'hashtags: unknown', 'created_at: unknown', 'user followers count: integer', 'replycount: integer', 'retweetcount: integer', 'likecount: integer', 'quotecount: integer', 'language: unknown', 'quotedtweet: unknown', 'inReplyToTweetId: float', 'inReplyToUser: unknown', 'mentionedUsers: unknown', 'clean_text: string']
"""
    train['clean_text'] = pd.Series([clean_text(i) for i in train['text']])
    return train
