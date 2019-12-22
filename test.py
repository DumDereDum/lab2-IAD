import dostoevsky
#dostoevsky download fasttext-social-network-model

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)

messages = [
    'но',
    'я люблю тебя!!',
    'fuck',
    'спасибо'

]

results = model.predict(list(messages), k=2)

for message, sentiment in zip(messages, results):
    #print(message, '->', list(sentiment.keys())[0])
    print(message, '->', sentiment)