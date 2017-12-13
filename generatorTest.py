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

#All posibilities lower case
#DONE : 
    #25 a-z * len (aaaaaaaa,bbbbbbbb)
tempDic = []
word = ""
stop = 0
for l in lc_letters:
    print l
    while stop < lengthWords:
        word = ''.join([word, l])
        stop = stop + 1
    tempDic.append(word)
    word = ""
    stop = 0



#Write in file
for i in tempDic:
    file.writelines(i+'\n')
