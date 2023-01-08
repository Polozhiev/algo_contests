import sys
import threading

def main():
    n, m = map(int, input().split())
    def findEuler(v, euler_cycle, marked):
        while adj[v]!=[]:
            u, id=adj[v].pop()
            if marked[id]:
                continue
            marked[id]=True
            findEuler(u, euler_cycle, marked)
            euler_cycle.append(v)   
        return euler_cycle

    adj=[[] for i in range(n+1)]
    degrees=[0]*(n+1)
    for i in range(m):
        a, b = map(int, input().split())
        adj[a].append([b,i])
        adj[b].append([a,i])
        degrees[a]+=1
        degrees[b]+=1
    for i in range(n+1):
        if degrees[i]%2==1:
            adj[0].append([i,m])
            adj[i].append([0,m])
            degrees[0]+=1
            degrees[i]+=1
            m+=1

    marked=[False]*m


    euler_cycle=[a]
    euler_cycle=findEuler(a,euler_cycle,marked)
    #print(euler_cycle)

    ans=[]
    count=0
    j=0
    ans_str=[]
    for i in range(len(euler_cycle)-1):
        if euler_cycle[i]!=0:
            ans_str.append(euler_cycle[i])
        elif euler_cycle[i]==0 and len(ans_str)>1:
            ans.append(ans_str)
            count+=1
            ans_str=[]
    if len(ans_str)>1:
        ans.append(ans_str)
        count+=1
    print(count)
    for i in range(count):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()

if __name__=="__main__":
    sys.setrecursionlimit(10**8)
    threading.stack_size(10**8)
    thread = threading.Thread(target=main)
    thread.start()    