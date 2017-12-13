#Lengh of words
lengthWords = 8

#All lower case letters
lc_letters = ["a","b","c","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#All upper case letters
uc_letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

#All numbers
numbers = ["1","2","3","4","5","6","7","8","9"]

#File dictionary
file = open("dictest.txt","w")

#Dictionary tmp
tmpDic = []

#All posibilities lower case
#DONE : 
    #26 a-z * len (aaaaaaaa,bbbbbbbb)
    #26 A-Z * len (aaaaaaaa,bbbbbbbb)


#26 a-z * len (aaaaaaaa,bbbbbbbb)
def lc26az():
    word = ""
    stop = 0
    for l in lc_letters:
        while stop < lengthWords:
            word = ''.join([word, l])
            stop = stop + 1
        print word
        tmpDic.append(word)
        word = ""
        stop = 0

#26 A-Z * len (AAAAAAAA,BBBBBBBB)
def uc26AZ():
    word = ""
    stop = 0
    for l in uc_letters:
        while stop < lengthWords:
            word = ''.join([word, l])
            stop = stop + 1
        print word
        tmpDic.append(word)
        word = ""
        stop = 0

#Load all def
def loadAll():
    lc26az()
    uc26AZ()

#Write in file
loadAll()
for i in tmpDic:
    file.writelines(i+'\n')
file.close()