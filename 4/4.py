n=int(input())
seq1=[int(i) for i in input().split()]
m=int(input())
seq2=[int(i) for i in input().split()]

dp=[[0]*(m+1) for i in range(n+1)]


dp[0][0], dp[1][0], dp[0][1]=0,0,0

for i in range(1,n+1):
    for j in range(1,m+1):
        if seq1[i-1]==seq2[j-1]:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]+1)
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

max_len=0
for i in range(1,n+1):
    for j in range(1,m+1):
        max_len=max(max_len, dp[i][j])
print(max_len)