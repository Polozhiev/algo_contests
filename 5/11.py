import sys
import threading

def main():
    def ConvFromDecimal(num):
        digits=[]
        for i in range(1,k):
            dig=num//(d**(k-1-i))
            digits.append(dig)
            num=num-dig*(d**(k-1-i))
        return digits

    def ConvToDecimal(digits):
        digits.reverse()
        dec=0
        for i in range(1,k-1):
            dec+=digits[i-1]*d**i
        return dec

    def makeGraph(d, k):
        global last_digit
        last_digit=[]
        adj=[[] for _ in range (d**(k-1))]
        for num in range (d**(k-1)):
            digits=ConvFromDecimal(num)
            last_digit.append(digits[-1])
            new_digits=digits[1:]
            null_adj_index=ConvToDecimal(new_digits)
            for i in range(d):
                adj[num].append(null_adj_index+i)
        return adj

    def euler(v):
        global ans
        ans=[]
        while adj[v]!=[]:
            u=adj[v].pop()
            euler(u)
            ans.append(last_digit[u])   
        return ans

    d, k =(int(_) for _ in input().split())

    if k==1:
        for i in range(d):
            print(i, end="")
    else:
        adj=makeGraph(d, k)
        ans=euler(0)
        ans.extend([0 for i in range(k-1)])
        for i in range(len(ans)):
            print(ans[i],end="")

if __name__=="__main__":
    sys.setrecursionlimit(10**7)
    threading.stack_size(10**8)
    thread = threading.Thread(target=main)
    thread.start()    