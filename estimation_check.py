from collections import defaultdict

file = open("estimations.txt", "r")
tonals = file.readlines()
file.close()

inform = defaultdict(dict)
for t in tonals:
    inform[t.split()[0]] = {'Est' : int(t.split()[1]), 'Sum' : 0, 'Num' : 0}

data = open("prepared_data", "r")
tweets = data.readlines()
num = 0
for tweet in tweets:

    t_low, t_up = -1, 1
    sum = 0
    for word in tweet.split()[16:]:
        if inform[word]:
            sum += (inform[word])['Est']
    if sum < t_low: local_res = -1
    elif sum > t_up: local_res = 1
    else: local_res = 0
    for word in tweet.split()[16:]:
        if inform[word]:
            (inform[word])['Sum'] += local_res
            (inform[word])['Num'] += 1

res = defaultdict(dict)
numOfWords = 0
numOfCurrWords = 0
for word in inform.keys():
    if inform[word] and (inform[word])['Num'] != 0:
        numOfWords += 1
        est = (inform[word])['Est']
        check = (inform[word])['Sum'] / (inform[word])['Num']
        acc = abs((1-abs(est - check))*100)
        if 80 <= acc <= 100: numOfCurrWords += 1
        res[word] = {'Est': est, 'Check_Est': round(check, 2), 'Acc': round(acc, 2)}

estimation_accuracy = numOfCurrWords / numOfWords * 100
print(estimation_accuracy)

nums = list(res.items())
nums.sort(key=lambda i:(i[1])['Acc'], reverse=True)
closest = []
for word in nums:
    if (word[1])['Acc'] < 100 and (word[1])['Est'] != 0:
        closest.append(word[0])
    if len(closest) == 5:
        break
nums.sort(key=lambda i:(i[1])['Acc'])
furthest = []
for word in nums:
    if (word[1])['Acc'] != 0 and (word[1])['Est'] != 0:
        furthest.append(word[0])
    if len(furthest) == 5:
        break
file = open('estimation_check.txt', 'w')
file.write('Top-5 Closest:\n')
[file.write(word+' '+str((inform[word])['Est'])+' '+str((res[word])['Check_Est'])+'\n') for word in closest]
file.write('\nTop-5 Furthest:\n')
[file.write(word+' '+str((inform[word])['Est'])+' '+str((res[word])['Check_Est'])+'\n') for word in furthest]
file.write('\nEstimation accuracy: ' + str(round(estimation_accuracy, 2)) + '%')
file.close()


nums.sort(key=lambda i:(i[1])['Check_Est'], reverse=True)
words = [x[0] for x in nums]
n = len(words)
most_positive = []
i = 0
while len(most_positive) < 5:
    if (inform[words[i]])['Num']>2:
        most_positive.append(words[i])
    i += 1

print(most_positive)
file = open('best_worst.txt', 'w')
file.write('Top-5 Most Positive:\n')
[file.write(word + ' ' + str((res[word])['Check_Est'])+'\n') for word in most_positive]
file.write('\nTop-5 Most Negative:\n')
[file.write(words[n-i-1] + ' ' + str((res[words[n-i-1]])['Check_Est'])+'\n') for i in range(5)]
file.close()