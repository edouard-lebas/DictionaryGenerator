#Lengh of words
lengthWords = 8

#All lower case letters
lc_letters = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

#All upper case letters
uc_letters = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",20:"V",22:"W",23:"X",24:"Y",25:"Z"}

#All numbers
numbers = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#File dictionary
file = open("dictest.txt","w")

#Dictionary tmp
tmpDic = []

#All posibilities lower case
#DONE : 
    #26 a-z * len (aaaaaaaa,bbbbbbbb)
    #26 A-Z * len (aaaaaaaa,bbbbbbbb)


#Basic generation of 25 words lower case between a-z
#Ex : aaaaaaaa, bbbbbbbb
def lcBasicaz():
    word = ""
    stop = 0
    for l in lc_letters:
        while stop < lengthWords:
            word = ''.join([word, lc_letters[l]])
            stop = stop + 1
        tmpDic.append(word)
        word = ""
        stop = 0

#Basic generation of 25 words upper case between A-Z
#Ex : AAAAAAAA, BBBBBBBB
def ucBasicAZ():
    word = ""
    stop = 0
    for l in uc_letters:
        while stop < lengthWords:
            word = ''.join([word, uc_letters[l]])
            stop = stop + 1
        tmpDic.append(word)
        word = ""
        stop = 0

#Load all def
def loadAll():
    lcBasicaz()
    ucBasicAZ()

#Write in file
loadAll()
for i in tmpDic:
    file.writelines(i+'\n')
file.close()