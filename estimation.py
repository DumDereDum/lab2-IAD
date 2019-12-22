import dostoevsky
from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

#dostoevsky download fasttext-social-network-model

data = open("words.txt", "r")
words = data.readlines()
data.close()

file = open("estimations.txt", "w")

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

i = 0
while i < len(words):
    results = model.predict(words[i:i+100], k=1)
    for word, sentiment in zip(words[i:i+100], results):
        estimation = list(sentiment.keys())[0]
        if estimation == 'skip' or estimation == 'speech': estimation = 'neutral'

        if estimation == 'negative': estimation = '-1'
        elif estimation == 'neutral': estimation = '0'
        elif estimation == 'positive': estimation = '1'

        file.write(word.split()[0] + ' ' + estimation + '\n')
    i += 100

file.close()
