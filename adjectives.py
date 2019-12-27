import pymorphy2
import numpy as np

import matplotlib.pyplot as plt

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

bars1 = [x.split()[0] for x in positive]
height1 = [int(x.split()[2]) for x in positive]
numOfBars1 = np.arange(len(bars1))

bars2 = [x.split()[0] for x in negative]
height2 = [int(x.split()[2]) for x in negative]
numOfBars2 = np.arange(len(bars2))

fig = plt.figure(figsize=(32, 16))
ax1 = fig.add_subplot(121)
ax1.grid(True)
ax1 = plt.bar(numOfBars1, height1)
ax1 = plt.yticks(fontsize=25)
ax1 = plt.xticks(numOfBars1, bars1, fontsize=25)
ax1 = plt.title('Top-5 Positive:', fontsize=46)

ax2 = fig.add_subplot(122)
ax2.grid(True)
ax2 = plt.bar(numOfBars2, height2)
ax2 = plt.yticks(fontsize=25)
ax2 = plt.xticks(numOfBars2, bars2, fontsize=25)
ax2 = plt.title('Top-5 Negative:', fontsize=46)

fig.savefig('plot')