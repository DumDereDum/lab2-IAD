import nltk
from stop_words import get_stop_words
from nltk.corpus import stopwords
#from nltk.stem import PorterStemmer
import re
import pymorphy2


#nltk.download('stopwords')

stop_words = list(get_stop_words('ru'))
nltk_words = list(stopwords.words('russian'))
stop_words.extend(nltk_words)
rep = re.compile("[^a-zA-Zа-яА-Я ]")
#ps = PorterStemmer()
morph = pymorphy2.MorphAnalyzer()

data = open("data.txt", "r")
file = open("prepared_data", "w")

tweets = data.readlines()
for tweet in tweets:
    res = tweet[:17]
    temp = ""
    flag = 0
    for word in tweet[17:].split(' '):
        if word == "RT": break
        if word == "#" or flag == 1: flag += 1
        if "pic.twitter.com" \
            and"http://" not in word \
            and "https://" not in word \
            and ".com" not in word \
            and flag == 0:
                temp += word + ' '
        if flag == 2: flag = 0

    temp = rep.sub('', temp)

    tokens = nltk.word_tokenize(temp)
    for word in tokens:
        if not word in stop_words:
            p = morph.parse(word)[0]
            res += p.normal_form + ' '

    file.write(res)

data.close()
file.close()
