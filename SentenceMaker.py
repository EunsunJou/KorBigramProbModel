#! /usr/bin/python3
# -*- coding: utf-8 -*-

import bisect
import itertools
import random
import codecs
import pickle
import datetime

import nltk
#from konlpy.corpus import kolaw
from konlpy.tag import Mecab # MeCab tends to reserve the original form of morphemes


# save timestamp for naming output file
now = datetime.datetime.now()
nowDatetime = now.strftime('%Y%m%d_%H%M')

# open review file
out = codecs.open('SentenceMaker'+nowDatetime[2:]+'.txt', 'w', 'utf-8')

def generate_sentence(cfdist, word, num=15):
    sentence = []

    # Generate words until we meet a period
    while word!='.':
        sentence.append(word)

        # Generate the next word based on probability
        choices, weights = zip(*cfdist[word].items())
        cumdist = list(itertools.accumulate(weights))
        x = random.random() * cumdist[-1]
        word = choices[bisect.bisect(cumdist, x)]

    return ' '.join(sentence)


def calc_cfd(doc):
    # Calculate conditional frequency distribution of bigrams
    words = [w for w, t in Mecab().pos(doc)]
    bigrams = nltk.bigrams(words)
    return nltk.ConditionalFreqDist(bigrams)


if __name__=='__main__':
    nsents = int(input("How many sentences?")) # Number of sentences
    initwords = [u'저승']

    print("Loading model...")
    f = open("sejongWmodern_10_ver02_cfd.pickle", "rb")
    cfd = pickle.load(f)
    
    for init in initwords:
        print("Generating sentences for "+init+"...")
        out.write('Word: '+init+"\n")
        for i in range(nsents):
            out.write('%d. %s \n' % (i, generate_sentence(cfd, init)))

out.close()
