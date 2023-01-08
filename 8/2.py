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

s=input()
z=z_function(s)

for i in range(1,len(z)):
    if z[i]==len(s)-i:
        print(i)
        quit()
print(len(s))
