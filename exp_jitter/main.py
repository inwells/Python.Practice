import random

base = 1000
cap = 3000

def backoff(attempt):
    return min(cap, base * 2 ** attempt)

def backoff_with_jitter(attempt):
    return random.randrange(1000, min(cap, base * 2 ** attempt))
    


for i in range(1,10):
	sleep = backoff(i)
	jsleep = backoff_with_jitter(i)
	sleepstr = str(sleep)
	sleeplen = len(sleepstr)
	alltogether = len(str(sleep))
    
	#print(str(sleep) + '    ' + str(alltogether) + '    *' + (' '*alltogether)+'*')
	print(str(i) + '    ' + str(sleep) + ' ' + str(jsleep/1000))
    
print('\nEND') 