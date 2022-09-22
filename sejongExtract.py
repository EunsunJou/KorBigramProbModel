'''
This project compiles a part of 세종 현대문어 원시말뭉치 into one big text file.
(It is roughly the national Korean corpus, or the Sejong corpus)
Of the different types of corpora, what is compiled here is modern written Korean.
The compiled results amount to 390MBs of text, that is 39,811,999 words in 1,399,581 lines(sentences).
The original corpus is marked up under the TEI(?) system, and is (fortunately) parsable with beautifulsoup.
The compiled output file is devoid of any markup.

I compiled corpora in order to train in with nltk.probability (e.g. conditional frequency distributions)
but this approximately 40 million-word corpus is too big to train in its entirety.
So I wrote separate code to randomly pick up certain portions of the corpus line by line.
'''

import os
import codecs
from bs4 import BeautifulSoup

# Directory where original (multiple) corpus text files are located
rawdir = "Path\\to\\corpus\\...\\sejong\\01\\02_말뭉치\\현대\\문어\\현대문어_말뭉치\\원시_말뭉치"
files = os.listdir(rawdir)

# Directory to locate output file:
# one big text file where all text files are compiled, line by line, without markup
output = codecs.open('Path\\to\\corpus\\...\\sejong\\01\\sejongraw\\bin\\collect_lines.txt', 'w', 'utf-8')

counter = 0

# For each original file,
for f in files:
    input = codecs.open(rawdir+"\\"+f, 'r', 'utf-16')  # Open the file
    soup = BeautifulSoup(input, 'html.parser')  # Make a beautifulsoup instance (i.e. parse) of the file 

    for sent in soup.find_all('p'):  # Each sentence is marekd enclosed in <p> ... </p>.
        output.write(sent.text+"\n")
    
    input.close()

    # Show progress
    counter = counter + 1
    print(str(counter)+'/'+str(len(files))) 

output.close()
