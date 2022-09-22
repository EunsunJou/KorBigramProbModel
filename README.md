# Bigram modeling from the Sejong Corpus of Korean

A collection of Python scripts that achieve three things:

1) Sample random sentences from the Sejong corpus of written Korean (sejongExtract.py, sejongRandomize.py, sejongWmodern_preprocessing.py)

   The entire corpus is 400MB of text, so it was practical to sample at the time I wrote this code. 

2) Build a bigram probability model and save the model for later use (cfdLearner.py)

   I used the MeCab morphological tagger by KoNLPy, and NLTK for building the model. The resultant model is saved as a Python pickle object using Python's native package "pickle".

3) Given a word, generate a sentence that begins with that word (SentenceMaker.py)

   Basically, if you give SentenceMaker.py a word that it knows, it will generate a sequence of bigrams based on the bigram model from Step 2 until it reaches an end-of-sentence marker. The results are not great but they are entertaining -- goes on to show that you need more than linear adjacency information at the syntax level I guess...


***About the Sejong Corpus***

The Sejong Corpus is a corpus compiled by the National Institute of Korean Language (NIKL) from 1998 to 2007; the 2nd edition version of its digital publication is dated 2011. This project used the "raw" sub-corpus, which is a corpus of written text that contains minimal markup (i.e., no part of speech tagging). It is publically available for non-commercial use, and I requested (and received) a DVD hard copy in 2016. The more up-to-date version seems to be available online here: https://corpus.korean.go.kr/ (Interface seems to be only in Korean, unfortunately).
