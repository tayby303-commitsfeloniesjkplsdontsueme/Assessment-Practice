word=input("Enter a word: ")
wrd=word.lower
def honi(wrd):
    letters=["h","o","n","i"] #letters in honi
    current=0 #tracks current index in letters
    search=letters[current] #sets the letter in letters[] that is searched
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
    elif count==0:
        print("That is not a honi")
honi(wrd)