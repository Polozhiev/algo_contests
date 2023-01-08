import itertools
from random import random
from random import choice

def nextRand24(a, b):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield cur >> 8

def nextRand32(a, b):
    gen = nextRand24(a, b)
    while True:
        c = next(gen); d = next(gen)
        yield (c << 8) ^ d

def partition(arr,l,r):
    j=l-1
    pivot=arr[r]
    for i in range(l,r):
        if arr[i]<=pivot:
            j+=1
            arr[j], arr[i]=arr[i], arr[j]   
      
    arr[j+1], arr[r] = arr[r], arr[j+1]
    return j+1

def findOrderStat(arr, l, r, q):
    pivot_index=partition(arr, l, r)
    if (q-1==pivot_index-l):
        return arr[pivot_index]
    elif (q-1<pivot_index-l):
        return findOrderStat(arr, l, pivot_index-1, q)
    else:
        return findOrderStat(arr, pivot_index+1, r, q-pivot_index+l-1)

    



n, q = map(int, input().split())
a, b = map(int, input().split())
x = list(itertools.islice(nextRand32(a, b), n)) # данный массив
#print(x)
print(findOrderStat(x,0,n-1,q))
