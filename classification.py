from collections import defaultdict

file = open("estimations.txt", "r")
tonals = file.readlines()
file.close()

tonalities = defaultdict(int)
for t in tonals:
    tonalities[t.split()[0]] = int(t.split()[1])
#print(tonalities)

data = open("prepared_data", "r")
tweets = data.readlines()

# /----- TEST 1 -----/
res1 = {'Good': 0, 'Bad': 0, 'Neutral': 0}

t_low = -1
t_up = 1
numOfTweets = 0

for tweet in tweets:
    numOfTweets += 1
    sum = 0
    for word in tweet.split():
        sum += tonalities[word]
    if sum < t_low: res1['Bad'] += 1
    elif sum > t_up: res1['Good'] += 1
    else: res1['Neutral'] += 1

# /----- TEST 2 -----/
res2 = {'Good': 0, 'Bad': 0, 'Neutral': 0}

for tweet in tweets:
    sum = 0
    for word in tweet.split():
        sum += tonalities[word]
    if sum <= t_low: res2['Bad'] += 1
    elif sum >= t_up: res2['Good'] += 1
    else: res2['Neutral'] += 1

# /----- TEST 3 -----/
res3 = {'Good': 0, 'Bad': 0, 'Neutral': 0}

for tweet in tweets:
    temp = {'Good': 0, 'Bad': 0, 'Neutral': 0}
    for word in tweet.split():
        t = tonalities[word]
        if t == -1: temp['Bad'] += 1
        elif t == 1: temp['Good'] += 1
        else: temp['Neutral'] += 1
    res3[max(temp.items(), key=lambda k_v: k_v[1])[0]] += 1

# /----- TEST 4 -----/
res4 = {'Good': 0, 'Bad': 0, 'Neutral': 0}

for tweet in tweets:
    temp = {'Good': 0, 'Bad': 0, 'Neutral': 0}
    for word in tweet.split():
        t = tonalities[word]
        if t == -1: temp['Bad'] += 1
        elif t == 1: temp['Good'] += 1
        else: temp['Neutral'] += 1
    if temp['Good'] != 0 and temp['Bad'] == 0: res4['Good'] += 1
    elif temp['Good'] == 0 and temp['Bad'] != 0: res4['Bad'] += 1
    else: res4['Neutral'] += 1

file = open("classifications.txt", "w")
file.write('Sum rule ( -1 <= Neutral <=1 ):\n')
for x in res1:
    file.write(x+' - '+str(res1[x])+' - '+str(round(res1[x]*100/numOfTweets, 4))+'% \n')

file.write('\nSum rule ( -1 < Neutral < 1 ):\n')
for x in res2:
    file.write(x+' - '+str(res2[x])+' - '+str(round(res2[x]*100/numOfTweets, 4))+'% \n')

file.write('\nPercent rule:\n')
for x in res3:
    file.write(x+' - '+str(res3[x])+' - '+str(round(res3[x]*100/numOfTweets, 4))+'% \n')

file.write('\nStrange rule:\n')
for x in res4:
    file.write(x+' - '+str(res4[x])+' - '+str(round(res4[x]*100/numOfTweets, 4))+'% \n')