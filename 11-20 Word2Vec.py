import re
import string
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
# import matplotlib.pyplot as plt

from gensim.models.wrappers import FastText
from gensim.models import Word2Vec
import pandas as pd
stop_words = set(stopwords.words("english"))
