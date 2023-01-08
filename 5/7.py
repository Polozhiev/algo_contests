import sys
import threading

def main():
    def distanceSquare(x1,y1,x2,y2):
        return ((x2-x1)**2+(y2-y1)**2)

    def getCnf(m, coords):
        cnf=[]
        for i in range(n):
            for j in range (i+1, n):
                if distanceSquare(coords[i][0],coords[i][1],coords[j][0],coords[j][1])<m:
                    cnf.append([2*i+1, 2*j+1])
                if distanceSquare(coords[i][0],coords[i][1],coords[j][2],coords[j][3])<m:
                    cnf.append([2*i+1, 2*j])
                if distanceSquare(coords[i][2],coords[i][3],coords[j][0],coords[j][1])<m:
                    cnf.append([2*i, 2*j+1])
                if distanceSquare(coords[i][2],coords[i][3],coords[j][2],coords[j][3])<m:
                    cnf.append([2*i, 2*j])
        return cnf

    def makeGraph(cnf):
        adj=[[] for i in range(2*n)]
        rev_adj=[[] for i in range(2*n)]
        for i in range(len(cnf)):
            a=cnf[i][0]
            b=cnf[i][1]
            neg_a=a^1
            neg_b=b^1
            adj[neg_a].append(b)
            adj[neg_b].append(a)
            rev_adj[b].append(neg_a)
            rev_adj[a].append(neg_b)        
        return(adj, rev_adj)

    def findScc(adj, rev_adj):
        def dfs(v, order):
            used[v]=True
            for u in adj[v]:
                if not used[u]:
                    dfs(u, order)
            order.append(v)

        def dfs2(v,c):
            used[v]=True
            colors[v]=c
            for u in rev_adj[v]:
                if not used[u]:
                    if colors[u]==0:
                        dfs2(u, c)
        
        used=[False]*(2*n)
        order=[]
        for i in range(2*n):
            if not used[i]:
                dfs(i, order)

        colors=[0]*(2*n)
        used=[False]*(2*n)
        c=1

        order.reverse()
        for v in order:
            if not used[v]:
                dfs2(v,c)
                c+=1 
        return(colors)

    def findSolution(scc):
        for i in range(0,2*n,2):
            if scc[i]==scc[i+1]:
                return(False)
        return(True)

    def checkAnswer(m, coords):
        cnf=getCnf(m, coords)
        adj, rev_adj=makeGraph(cnf)
        scc=findScc(adj, rev_adj)
        if findSolution(scc):
            return True
        else:
            return False
        
    def binarySearch(coords):
        left=0
        right=8*10**18
        mid=left+(right-left)//2
        while right-left>1:
            if checkAnswer(mid, coords):
                left=mid
            else:
                right=mid
            mid=left+(right-left)//2
        return left**0.5

    n=int(input())
    coords=[]
    for i in range(n):
        c=[int(_) for _ in input().split()]
        coords.append(c)
    print(binarySearch(coords))

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()


# 3
# -1 1 0 0
# 0 1 1 1 
# 1 0 2 1

# 4
# -2 -2 -2 2
# 0 0 0 2
# 0 -2 2 0
# 2 1 3 0

# 2
# 0 0 1000000000 1000000000
# 0 0 -1000000000 -1000000000