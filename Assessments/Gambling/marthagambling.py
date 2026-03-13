quarters=int(input("How many quarters did Martha spend? "))
lastpaidt1=int(input("When was Martha last paid for the first machine? "))
lastpaidt2=int(input("When was Martha last paid for the second machine? "))
lastpaidt3=int(input("When was Martha last paid for the third machine? "))
def gambling(quarters,lastpaidt1,lastpaidt2,lastpaidt3):
    timeplayed=0
    s1=35
    s2=100
    s3=10
    s1-=lastpaidt1
    s2-=lastpaidt2
    s3-=lastpaidt3
    while quarters>0:
        if quarters == 0:
            s1-=1
            quarters-=1
            timeplayed+=1
            if s1==0:
                quarters+=30
                s1+=35
            s2-=1
            quarters-=1
            timeplayed+=1
            if s2==0:
                quarters+=60
                s2+=100
            s3-=1
            quarters-=1
            timeplayed+=1
            if s3==0:
                quarters+=9
                s3+=10
    print(f"Martha played {timeplayed} times before going broke.")  
gambling(quarters,lastpaidt1,lastpaidt2,lastpaidt3)