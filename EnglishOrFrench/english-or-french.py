x=input("Word: ")
q=x.lower
def language(q,y):
    s=0
    t=0
    for i in q:
        if i=="s":
            s+=1
        elif i=="t":
            t+=1
    if s>=t:
        z="French" 
    elif t>=s:
        z="English"
print(language)