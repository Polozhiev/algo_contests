import random
def main():
    with open('/home/roman/edu/Algo/Contests/test8/data.txt', 'w') as f:
        n=50000
        colors=[]
        sockets=[]
        for i in range(n):
            colors.append(random.randint(1, n))
        for i in range(1,n+1):
            sockets.extend([i,i])
        random.shuffle(sockets)

        f.write(str(n)+"\n")
        f.write(" ".join(map(str,colors))+"\n")
        f.write(" ".join(map(str,sockets)))

if __name__=="__main__":
    main()