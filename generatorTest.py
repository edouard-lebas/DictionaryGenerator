from random import randint
import time
start_time = time.time()
#Lengh of words
lengthWords = 8

#All lower case letters
lc_letters = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

#All upper case letters
uc_letters = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

#All numbers
numbers = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#File dictionary
file = open("dic.txt","w")

#Dictionary tmp LC
tmpDicLC = []

#Dictionary tmp UC
tmpDicUC = []

#Maximum of words to generate
maxWords = 100

#Get random number between min and max
def getRandomNumber(min,max):
    return randint(min,max)

#Generate random lower case word with length
def generateLCRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,25)
        letter = lc_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all lower case words with max words
def loadAllLCRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateLCRandomWord()        
        tmpDicLC.append(word)        
        cursor = cursor+1

#Generate random upper case word with length
def generateUCRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,25)
        letter = uc_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all lower upper words with max words
def loadAllUCRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateUCRandomWord()        
        tmpDicUC.append(word)        
        cursor = cursor+1

#Write in file
loadAllLCRandomWord()
loadAllUCRandomWord()
for i in tmpDicLC:
    file.writelines(i+'\n')
for i in tmpDicUC:
    file.writelines(i+'\n')
file.close()
print("--- %s seconds ---" % (time.time() - start_time))