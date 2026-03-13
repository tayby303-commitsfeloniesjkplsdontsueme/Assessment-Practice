mb=10
length=3
month=[4,6,2]
def internet(mb,length,month):
    remaining=0
    for i in range(length):
        remaining+=mb
        remaining-=month[i]
    print(remaining+mb)
internet(mb,length,month)