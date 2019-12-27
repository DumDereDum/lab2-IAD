import matplotlib.pyplot as plt
import pandas as pd
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

# res = {'Good': 0, 'Bad': 0, 'Neutral': 0}
res = {}
point = pd.to_datetime('2018-07-07 23:55', format='%Y-%m-%d %H:%M')
brpoint = pd.to_datetime('2018-07-08 03:00', format='%Y-%m-%d %H:%M')
t_low = -1
t_up = 1
numOfTweets = 0

i = len(tweets) -1
res_num = 0
while i > 10 and brpoint > point:
    local_res = {'Good': 0, 'Neutral': 0, 'Bad': 0, 'General': 0}
    while dates[i] < point:
        sum = 0
        res_num += 1
        local_res['General'] += 1
        for word in tweets[i].split():
            sum += tonalities[word]
        if sum <= t_low:
            local_res['Bad'] += 1
        elif sum >= t_up:
            local_res['Good'] += 1
        else:
            local_res['Neutral'] += 1
        i -= 1
    print(local_res)
    bad = local_res['Bad'] /local_res['General']
    neutral = local_res['Neutral'] /local_res['General']
    good = local_res['Good'] /local_res['General']
    res[point] = {'Good': round(good,2),'Neutral': round(neutral,2),'Bad': round(bad,2), 'General': res_num}
    point += pd.Timedelta(5, unit='m')

# [print(x, res[x]) for x in res]
file = open("hours.txt", "w")
for k in res.keys():
    file.write('2018-07-07 23:55 - ' + str(k)[11:16] + ' : ' + str(((res)[k])['General'])+' ')
    file.write(str(((res)[k])['Good'])+'/'+str(((res)[k])['Neutral'])+'/'+str(((res)[k])['Bad'])+'\n')


table = pd.DataFrame(res, index=['Good','Neutral', 'Bad'])
print(table)


x = [str(x)[11:16] for x in res.keys()]
y1 = table.values[0, :]
y2 = table.values[1, :]
y3 = table.values[2, :]
y4 = [(res[x])['General'] for x in res.keys()]
print(x)
print(y4)
print(len(x), len(y1))

fig = plt.figure(figsize=(37, 16))
plt.title('Distribution of tweets classes in time', fontsize=42)

ax1 = fig.add_subplot(211)
ax1.grid(True)
ax1 = plt.scatter(x, y1, color='r', s=60, label='Good')
ax1 = plt.plot(x, y1, color='r')
ax1 = plt.scatter(x, y2, color='g', s=60, label='Neutral')
ax1 = plt.plot(x, y2, color='g')
ax1 = plt.scatter(x, y3, color='b', s=60, label='Bad')
ax1 = plt.plot(x, y3, color='b')
ax1 = plt.legend()
ax2 = plt.yticks(fontsize=20)
ax1 = plt.xticks(rotation = 90)
ax1 = plt.ylabel('Fraction', fontsize=30)

ax2 = fig.add_subplot(212)
ax2.grid(True)
ax2.vlines(x,  ymin=0, ymax=max(y4) + 100, color='firebrick', alpha=0.7, linewidth=2)
ax2.scatter(x, y4, s=75, color='firebrick')
ax2 = plt.xlabel('Time window', fontsize=30)
ax2 = plt.ylabel('Number of tweets', fontsize=30)
ax2 = plt.yticks(fontsize=20)
ax2 = plt.xticks(rotation=90, fontsize=30)

plt.show()
fig.savefig('plot1')
