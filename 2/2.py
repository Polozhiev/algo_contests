import itertools

def nextRand24(a, b, m):
    AND = (1 << 32) - 1
    cur = 0
    while True:
        cur = (cur * a + b) & AND
        yield (cur >> 8) % m
 

def mergeSort(x):
    count=0
    if len(x)<=1:
        return 0
    med=len(x)//2
    L=x[:med]
    R=x[med:]
    count+=mergeSort(L)
    count+=mergeSort(R)
    
    i,j,k=0,0,0

    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            x[k]=L[i]
            i+=1
            k+=1
        else:
            x[k]=R[j]
            j+=1
            k+=1
            count+=med-i
    while i<len(L):
        x[k]=L[i]
        i+=1
        k+=1
    while j<len(R):
        x[k]=R[j]
        j+=1
        k+=1  
    return (count)

# x=[0,6,4,2,1,3,8,9,12,0]
# print(mergeSort(x))
# print(x)


n, m = map(int, input().split())
a, b = map(int, input().split())

x = list(itertools.islice(nextRand24(a, b, m), n)) # x - данный массив
#print(x)
print(mergeSort(x))
