n=int(input("How many parking spaces are there? (1≤N≤100) "))
def occupied(n,x,y):
    spaces=0
    for i in range(n):
        if x[i]=="C"  and y[i]=="C":
            spaces+=1
    print(spaces)
occupied(n,"CCC..","C..CC")