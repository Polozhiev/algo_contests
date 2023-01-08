import sys
import threading

def main():
    def goodDegrees(counter):
        global start
        start=-1
        end=-1
        for i in range(len(counter)):
            if counter[i]>1:
                return False
            if counter[i]==1:
                if start!=-1:
                    return False
                start=i
            if counter[i]==-1:
                if end!=-1:
                    return False
                end=i
        if start*end<0:
            return False
        return True

    def findEuler(v, ans_ind):
        while adj[v]!=[]:
            u=adj[v].pop()
            findEuler(u, ans_ind)
            ans_ind.append(u)   
        return ans_ind

    alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    n = int(input())
    adj=[[] for _ in range(62*62)]
    counter=[0]*(62*62)
    for i in range(n):
        a, b, c=map(alphabet.index, input())
        adj[a*62+b].append(b*62+c)
        counter[a*62+b]+=1
        counter[b*62+c]-=1

    if goodDegrees(counter):
        ans_ind=[]
        if start!=-1:
            ans_ind=(findEuler(start, ans_ind))
        else:   
            ans_ind=(findEuler(a*62+b, ans_ind))
        if start!=-1:
            ans_ind.append(start)
        else:   
            ans_ind.append(a*62+b)
        ans_ind.reverse()
        ans=[]
        ans.append(alphabet[ans_ind[0]//62])
        ans.append(alphabet[ans_ind[0]%62])
        for i in range(1, len(ans_ind)):
            ans.append(alphabet[ans_ind[i]%62])
        if len(ans)==n+2:    
            print("YES")
            for i in range(len(ans)):
                print (ans[i], end="")
        else:
            print("NO")
    else:
        print("NO")


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()

