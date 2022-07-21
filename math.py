import math

a = float(3.2) 
print(a)
print(math.ceil(a))


# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))

c = [1,1]
loop = (len(c))
i = 0
while i < loop:
    if c[i] == 1:
        c.remove(c[i])
        loop -= 1
        i -= 1

    i+=1

print(c) #prints empty

import functools

#fibonacci recursive with caching
@functools.lru_cache(maxsize=None) #128 by default (Simple lightweight unbounded function cache. Sometimes called “memoize”.)
def fib(num):
    if num < 2:
        return num
    else:
        return fib(num-1) + fib(num-2)
print(fib(20))

#fibonacci tabulation
def fibtab(n):
    list = [int('0')] * (n + 1)
    list[1] = 1
    print(list)
    for i in range(2,len(list)):
        list[i] = list[i-1] + list[i-2]
    return list[n]
print(f"fibtab{fibtab(50)}")        

@functools.lru_cache(maxsize=None) #128 by default (Simple lightweight unbounded function cache. Sometimes called “memoize”.)
def gridtravel(m,n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return gridtravel(m-1,n) + gridtravel(m,n-1)

print(gridtravel(18,18))

#there may be a way to improve this
def allConstruct(target, wordBank):
    if target == '':
        return [[]]

    result = []
    for word in wordBank:
        if target.startswith(word):
            # print(word)
            suffix = target[len(word):]
            # print(f"suffix {suffix}")
            suffixWays = allConstruct(suffix, wordBank)
            targetWays = []
            for way in suffixWays:
                way.insert(0,word)
                if not word in targetWays:
                    targetWays.extend(way)
                else: 
                    result.append(way)
            if targetWays:
                result.append(targetWays)

    return result

print(allConstruct('puuurple',['purp','p','ur','le','purpl','u','uu','pu','e','pl']))

