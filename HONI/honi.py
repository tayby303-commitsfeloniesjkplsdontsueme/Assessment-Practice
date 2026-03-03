word=input("Enter a word: ")
wrd=word.lower
def honi(wrd):
    letters=["h","o","n","i"]
    search=letters(0)
    for i in wrd:
        if wrd[i]==search:
            search=letters
    if search==letters[3]:
