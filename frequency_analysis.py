from collections import defaultdict

data = open("prepared_data", "r")
tweets = data.readlines()
data.close()

file1 = open("frequency.txt", "w")
file2 = open("tweets_length.txt", "w")
file3 = open("words.txt", "w")

numOfTweets = 0
numOfWords = 0
lengths = defaultdict(int)
words = defaultdict(int)

for tweet in tweets:
    num = 0
    for word in tweet[17:].split(' '):
        if word != '\n':
            num += 1
            numOfWords += 1
            words[word] += 1
    numOfTweets += 1
    lengths[num] += 1

nums = list(words.items())
nums.sort(key=lambda i: i[1], reverse=True)

for x in nums:
    res = x[0] + ' - ' + str(x[1]) + ' - ' + str(round(x[1]*100/numOfWords, 4)) + '%'
    file1.write(res + '\n')
    file3.write(x[0] + ' \n')

lens = list(lengths.items())
lens.sort(key=lambda i: i[1], reverse=True)
for x in lens:
    res = str(x[0]) + ' - ' + str(x[1]) + ' - ' + str(round(x[1]*100/numOfTweets, 4)) + '%'
    file2.write(res + '\n')

file1.close()
file2.close()
file3.close()
