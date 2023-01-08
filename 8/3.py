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

S=input()
doubleS=S+S
z=z_function(S+S)
ans=0
for i in range(1,len(S)):
    if z[i]<len(S):
        if doubleS[z[i]]>doubleS[i+z[i]]:
            ans+=1
print(ans+1)

