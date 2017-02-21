''' Given an integer n, find total possible bit strings(0,1) of length n
    which dont have two contiguous zeroes in them. '''

def permutations(n):
    for i in range(1, 2**n-1):
        yield '{:0{n}b}'.format(i, n=n)

def calculate_bytes(m):
    
    samp = list(permutations(m))

    # filter out results which have repeated 0s

    new_samp = []

    for i in range(0, len(samp)):

        temp = 0

        for j in range(0, m-1):
            if (samp[i][j]=='0')and(samp[i][j+1]=='0')and(j!=m-1):
                temp = 1

        if temp == 0:
            new_samp.append(samp[i])

    # print(new_samp)

    # count number of elements in list. display them.

    print(len(new_samp)+1)

n = list()

size = int(input())

if size<1 or size>1000: # Constraint 1
    print("Error.")
    quit()

for i in range(0,size):
    temp = int(input())

    if temp<1 or temp>10**15:   # Constraint 2
        print("Error.")
        quit()
    
    n.append(temp)

for i in range(0,len(n)):
    calculate_bytes(n[i])

