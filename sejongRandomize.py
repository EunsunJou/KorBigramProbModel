import codecs
import random


f = codecs.open("Path\\to\\corpus\\...sejong\\01\\sejongWmodern_compiled\\sejongWmodern_lines.txt", 'r', 'utf-8')
o = codecs.open("Path\\to\\corpus\\...\\sejong\\01\\sejongWmodern_compiled\\sejongWmodern_10.txt", 'w', 'utf-8')

sentences = f.readlines()

# The total number of sentences from original.
whole = len(sentences)
# The target size. Here it's 10% of the whole.
part = round(whole*0.10)

# "targets" is a list of unique integers within the range of 'whole'.
# The number of integers equals 'part.'
# E.g. If there are 100 sentences and I opted for 10%, 
# "targets" will consist of ten unique integers within the range of 0-99.
# I will use this list as the index of sentences to be picked up.
targets = random.sample(range(whole), part)

for i in targets:
    o.write(sentences[i])


f.close()
o.close()