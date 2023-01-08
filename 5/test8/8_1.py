import sys
import threading
import time

def main():
    def make_graph(conditions, n):
        adj=[[] for i in range(2*n+2)]
        rev_adj=[[] for i in range(2*n+2)]
        for i in range(len(conditions)):
            a=conditions[i][0]
            b=conditions[i][1]
            neg_a=a+1*((a+1)%2)-1*(a%2)
            neg_b=b+1*((b+1)%2)-1*(b%2)
            adj[a].append(neg_b)
            adj[b].append(neg_a)
            rev_adj[neg_b].append(a)
            rev_adj[neg_a].append(b)
        return(adj, rev_adj)

    def find_scc(adj, rev_adj,n):
        def dfs(v, order):
            used[v]=True
            for u in adj[v]:
                if not used[u]:
                    dfs(u, order)
            order.append(v)

        def dfs2(v,c):
            used[v]=True
            scc[v]=c
            for u in rev_adj[v]:
                if not used[u]:
                    if scc[u]==0:
                        dfs2(u, c)
        
        used=[False]*(n)
        order=[]
        for i in range(n):
            if not used[i]:
                dfs(i, order)

        scc=[0]*(n)
        used=[False]*(n)
        c=1

        order.reverse()
        for v in order:
            if not used[v]:
                dfs2(v,c)
                c+=1 
        return scc

    def find_solution(scc):
        ans=[]
        for i in range(2,len(scc),2):
            if scc[i]==scc[i+1]:
                return False
            if scc[i]<scc[i+1]:
                ans.append(0)
            else:
                ans.append(1)
        return(ans)

    # n=int(input())
    # colors=[-1]
    # colors.extend([int(_) for _ in input().split()])
    # sockets=[int(_) for _ in input().split()]

    with open('/home/roman/edu/Algo/Contests/test8/data.txt') as f:
        n=int(f.readline())
        colors=[-1]
        colors.extend([int (_) for _ in (f.readline().strip('\n')).split()])
        sockets=[int (_) for _ in (f.readline().strip('\n')).split()] 


    wires_sockets=[[] for _ in range(n+1)]
    for i in range(2*n):
        wires_sockets[sockets[i]].append(i+1)

    help=[0]*(2*n)
    sockets_pairs=[]
    for i in range(2*n):
        sockets_pairs.append(sockets[i]*2+help[sockets[i]])
        help[sockets[i]]=1
        # if sockets[i]*2 not in sockets_pairs:
        #     sockets_pairs.append(sockets[i]*2)
        # else:
        #     sockets_pairs.append(sockets[i]*2+1)



    conditions=[]
    for i in range(2*n-1):
        if colors[sockets[i]]==colors[sockets[i+1]]:
            conditions.append([sockets_pairs[i], sockets_pairs[i+1]])
    if colors[sockets[2*n-1]]==colors[sockets[0]]:
        conditions.append([sockets_pairs[2*n-1], sockets_pairs[0]])

    adj, rev_adj=make_graph(conditions,n)
    scc=find_scc(adj, rev_adj, 2*n+2)
    ans=find_solution(scc)

    if (not ans):
        print("NO")
    else:
        print("YES")
        # for i in range(1,n+1):
        #     print(wires_sockets[i][ans[i-1]-1], end=" ")

if __name__=="__main__":
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()        
