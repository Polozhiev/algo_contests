def z_function(string):
    z=[0]*len(string)
    z[0]=len(string)
    L=0
    R=0
    for i in range(1, len(string)):
        k=0
        if i<=R:
            k=min(z[i-L],R-i+1)
        while i+k<len(string) and string[k]==string[i+k]:
            k+=1
        z[i]=k
        if i+z[i]-1>R:
            L=i
            R=i+z[i]-1
    return z

pattern=input()
text=input()
z=z_function(pattern+text)
rev_pattern=pattern[::-1]
rev_text=text[::-1]
rev_z=z_function(rev_pattern+rev_text)
ans_count=0
sum_len=len(pattern+text)
ans=[]
for i in range(len(pattern),sum_len-len(pattern)+1):
    if z[i]+rev_z[sum_len-i]>=len(pattern)-1:
        ans_count+=1
        ans.append(i-len(pattern)+1)
print(ans_count)
print(*ans)