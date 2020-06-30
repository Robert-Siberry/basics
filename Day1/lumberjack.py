n=int(input("Please enter the size of the storage area: "))
logs=int(input("Please enter the number of logs to be added: "))
piles=list(map(int, input("Please input the amount of log in each pile (number of piles to be entered "+(str(n*n))+") of the storage area: ").split()))


for i in range(logs):
    piles[piles.index(min(piles))]+=1

for i in range(0, n*n, n):
    print(' '.join(str(p) for p in piles[i:i+n]))