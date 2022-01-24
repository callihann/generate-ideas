from base64 import decode
import random
import json
import random
import urllib.request

final = []
words = []
url = urllib.request.urlopen("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")

for line in url:
        words.append(line.strip().decode('utf-8')) # appends stripped and decoded words to word list

num = input("Specify the quantity of ideas to generate: ")

def genStem():
        stem = open("sentence_src\\stem.txt", "r") # imports stems
        stemList = [line.strip() for line in stem]
        finalStem = stemList[random.randint(0, len(stemList) - 1)]
        
        for i in finalStem:
                finalStem = finalStem.replace("&", random.choice(words), 1) # picks random word and replaces % symbol
        if int(num) >= 100: # slight optimization to prevent long wait times
                pass
        else:
                print(finalStem)
        final.append(finalStem)

for i in range(int(num)): # generates sentences in range of num specified
        genStem()

f = open("out/" + num + "-" + random.choice(words) + ".txt", 'w') # opens out file and creates .txt with number of words and a random word
for element in final:
        f.write(element + "\n") # writes to file
f.close()