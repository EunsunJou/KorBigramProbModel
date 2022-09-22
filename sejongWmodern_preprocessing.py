# Code for preprocessing extracted test
import re
import codecs

input = codecs.open("inputFile", "r", "utf-8")
output = codecs.open("outputFile", "w", "utf-8")

raw = input.read()

print("Pattern 1 ...")
raw = re.sub("^\n", "", raw)

print("Pattern 2 ...")
raw = re.sub("\.", "", raw)

print("Pattern 3 ...")
raw = re.sub('\"', "", raw)

print("Pattern 4 ...")
raw = re.sub("\?[^\n]", "\?\n", raw)

print("Pattern 5 ...")
raw = re.sub("!", "!\n", raw)

output.write(raw)

input.close()
output.close()