n=int(input("Please enter the size of the storage area: "))
logs=int(input("Please enter the number of logs to be added: "))
piles=[]

for i in range(0, (n*n)):
    ele=int(input("Please enter the number of logs currently in each pile of the storage area: "))

    piles.append(ele)

for i in range(logs):
    piles[piles.index(min(piles))]+=1

for i in range(0, n*n, n):
    print(' '.join(str(p) for p in piles[i:i+n]))