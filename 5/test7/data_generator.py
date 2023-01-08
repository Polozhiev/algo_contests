import random
def main():
    with open('/home/roman/edu/Algo/Contests/test7/data.txt', 'w') as f:
        n=100
        inp=str(n)+"\n"
        for i in range(n):
            x1=random.randint(-10**9,10**9)
            y1=random.randint(-10**9,10**9)
            x2=random.randint(-10**9,10**9)
            y2=random.randint(-10**9,10**9)
            inp+=str(x1)+" "+str(y1)+" "+str(x2)+" "+str(y2)+"\n"
        f.write(inp)

if __name__=="__main__":
    main()