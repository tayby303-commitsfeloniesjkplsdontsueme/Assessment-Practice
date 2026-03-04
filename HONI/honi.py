word=input("Enter a word: ")
wrd=word.lower
def honi(wrd):
    letters=["h","o","n","i"] #letters in honi
    current=0 #tracks current index in letters
    search=letters[current] #
    count=0
    for i in wrd:
        if wrd[i]==search:
            current+=1
        elif search==letters[3]:
            current=0
            count+=1
            break
    if count==1:
        print("That is a honi")
print(honi(wrd))