n = input('').split(' ')
k = int(n[1])
advancers = 0
 
scores = input('').split(' ')
cutoff = int(scores[k - 1])
for score in scores:
    if int(score) >= cutoff and int(score) != 0:
        advancers += 1
    
print(advancers)