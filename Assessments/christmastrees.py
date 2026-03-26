trees=int(input("How many trees are there? "))
heights=[1,3,4,2]
up=[]
down=[]
x=0
y=0
for i in heights(trees):
    if heights[i]<heights[i+1]:
        down.append(y)
        x+=1
        y=0
    elif heights[i]<heights[i-1]:
        up.append(x)
        x=0
        y+=1
print(max(up))
print(max(down))