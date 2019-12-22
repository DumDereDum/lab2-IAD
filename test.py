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
    'нахуй',
    ' ',
    'fgh',
    'dfghjk',
    'tyu'

]
i=0
while i < len(messages):
    results = model.predict(messages[0:2], k=1)

    for message, sentiment in zip(messages[0:2], results):
        #print(message, '->', list(sentiment.keys())[0])
        print(message, '->', sentiment)
    i+=2

print("11  ", len('\n'))