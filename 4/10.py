s=input()
n=len(s)
dp=[[0]*n for i in range(n)]

for i in range(n):
    dp[i][i]=1

def pair(i,j):
    if (s[i] == '(' and s[j] == ')') or (s[i] == '[' and s[j] == ']') or (s[i] == '{' and s[j] == '}'):
        return(True)
    else:
        return(False)    

for j in range(1,n):
    for i in range(j-1, -1,-1):
        min_del=101
        if pair(i,j)==True:
            min_del=dp[i+1][j-1]
        for k in range(i,j):
            min_del=min(min_del, dp[i][k]+dp[k+1][j])
        dp[i][j]=min_del
        
print(n-dp[0][n-1])
