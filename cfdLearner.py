import codecs
import pickle

import nltk
#from konlpy.corpus import kolaw
from konlpy.tag import Mecab # MeCab tends to reserve the original form of morphemes


def calc_cfd(doc):
    # Calculate conditional frequency distribution of bigrams
    words = [w for w, t in Mecab().pos(doc)]
    bigrams = nltk.bigrams(words)
    return nltk.ConditionalFreqDist(bigrams)


if __name__=='__main__':
    print("Loading training file ...")
    # Open the txt file with sentences extracted from corpus
    doc = codecs.open('sejongWmodern_10.txt', 'r', 'utf8').read()
    
    print("Calculating conditional frequency distribution ...")
    # Apply calc_cfd function to txt file, creating the bigram model
    cfd = calc_cfd(doc)
    
    print("Pickling cfd model ...")
    # Pickle the bigram model dictionary
    with open("sejongWmodern_10_ver02_cfd.pickle", "wb") as f:
        pickle.dump(cfd, f)
    
    print("Training complete!")