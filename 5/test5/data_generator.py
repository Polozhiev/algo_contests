from random import randint
def main():
    with open('/home/roman/edu/Algo/Contests/test5/data.txt', 'w') as f:
        vertex = set()
        edges = set()
        len_n=10
        for _ in range(len_n):
            a, b = randint(1, len_n), randint(1, len_n)
            vertex.add(a)
            vertex.add(b)
            edges.add((a, b))
        #print(max(vertex), min(vertex))
        f.write(str(len_n) + ' ' + str(len(edges)) + '\n')
        for elem in edges:
            f.write(str(elem[0]) + ' ' + str(elem[1]) + '\n')

if __name__=="__main__":
    main()