import random
import json
import random
import urllib.request

url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())
final = []
num = input("Specify the quantity of ideas to generate: ")

def genStem():
        stem = open("sentence_src\\stem.txt", "r")
        stemList = [line.strip() for line in stem]
        finalStem = stemList[random.randint(0, len(stemList) - 1)]
        
        for i in finalStem:
                finalStem = finalStem.replace("&", random.choice(words), 1)
                finalStem = finalStem.replace("%", random.choice(words), 1)
        
        if int(num) >= 100:
                pass
        else:
                print(finalStem)
        final.append(finalStem)

for i in range(int(num)):
        genStem()

f = open("out/" + num + ".txt", 'w')
for element in final:
        f.write(element + "\n")
f.close()