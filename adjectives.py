import pymorphy2

data = open("frequency.txt", "r")
frequency = data.readlines()
data.close()

data = open("estimations.txt", "r")
estimations = data.readlines()
data.close()

morph = pymorphy2.MorphAnalyzer()

numOfWords = len(estimations)
positive = []
negative = []
i = 0
while (i < numOfWords) and (len(positive) < 5 or len(negative) < 5):
    est = estimations[i].split()
    #print(est)
    if (est[1] != '0') and ('ADJF' in morph.parse(est[0])[0].tag):
        if est[1] == '1' and len(positive) < 5:
            positive.append(frequency[i])
        elif est[1] == '-1' and len(negative) < 5:
            negative.append(frequency[i])
    i += 1

file = open("adjectives.txt", "w")
file.write("Top-5 Positive:\n")
[file.write(x) for x in positive]
file.write("\nTop-5 Negative:\n")
[file.write(x) for x in negative]


print("Top-5 Positive:")
[print(x, end='') for x in positive]

print("\nTop-5 Negative:")
[print(x, end='') for x in negative]
