import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import copy

file = open("estimations.txt", "r")
tonals = file.readlines()
file.close()

tonalities = defaultdict(int)
for t in tonals:
    tonalities[t.split()[0]] = int(t.split()[1])

data = open("prepared_data", "r")
tweets = data.readlines()
data.close()

d = [x[:17] for x in tweets]
dates = pd.to_datetime(d, format='%Y-%m-%d %H:%M')

#res = {'Good': 0, 'Bad': 0, 'Neutral': 0}
res = {}
point = pd.to_datetime('2018-07-07 23:50', format='%Y-%m-%d %H:%M')
brpoint = pd.to_datetime('2018-07-08 11:50', format='%Y-%m-%d %H:%M')
t_low = -1
t_up = 1
numOfTweets = 0

i = len(tweets) -1
local_res = {'Good': 0, 'Bad': 0, 'Neutral': 0}
while i > 10 and brpoint > point:
    while dates[i] < point:
        sum = 0
        for word in tweets[i].split():
            sum += tonalities[word]
        if sum <= t_low:
            local_res['Bad'] += 1
        elif sum >= t_up:
            local_res['Good'] += 1
        else:
            local_res['Neutral'] += 1
        i -= 1

    res[point] = copy.copy(local_res)
    point += pd.Timedelta(60, unit='m')

#[print(x, res[x]) for x in res]

table = pd.DataFrame(res,index=['Good', 'Bad', 'Neutral'])
#print(table)


#print(res.keys())

x = res.keys()
y1 = table.values[0, :]
y2 = table.values[1, :]
y3 = table.values[2, :]
print(x)
print(y1)
print(len(x), len(y1))

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()