txt=input().split()
l=[]
for i in txt:
    if i.isdigit():
        l.append(int(i))
    else:
        a=l.pop()
        b=l.pop()
        if i=="+":
            l.append(b+a)
        elif i=="*":
            l.append(b*a)
        elif i=="-":
            l.append(b-a)
print(l[0])
