from random import randint
#Lengh of words
lengthWords = 8

#All lower case letters
lc_letters = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}

#All upper case letters
uc_letters = {0:"A",1:"B",2:"C",3:"D",4:"E",5:"F",6:"G",7:"H",8:"I",9:"J",10:"K",11:"L",12:"M",13:"N",14:"O",15:"P",16:"Q",17:"R",18:"S",19:"T",20:"U",21:"V",22:"W",23:"X",24:"Y",25:"Z"}

#All numbers
numbers = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}

#All lower case and upper case letters mixed
uclc_letters = {0:"a",1:"A",2:"b",3:"B",4:"c",5:"C",6:"d",7:"D",8:"e",9:"E",10:"f",11:"F",12:"g",13:"G",14:"h",15:"H",16:"i",17:"I",18:"j",19:"J",20:"k",21:"K",22:"l",23:"L",24:"m",25:"M",26:"n",27:"N",28:"o",29:"O",30:"p",31:"P",32:"q",33:"Q",34:"r",35:"R",36:"s",37:"S",38:"t",39:"T",40:"u",41:"U",42:"v",43:"V",44:"w",45:"W",46:"x",47:"X",48:"y",49:"y",50:"z",51:"Z"}

#All lower case and num letters
lcnum_letters = {0:"a",1:"b",2:"0",3:"c",4:"d",5:"1",6:"e",7:"f",8:"2",9:"g",10:"h",11:"3",12:"i",13:"j",14:"4",15:"k",16:"l",17:"5",18:"m",19:"n",20:"6",21:"o",22:"p",23:"7",24:"q",25:"r",26:"8",27:"s",28:"t",29:"9",30:"u",31:"v",32:"w",33:"x",34:"y",35:"z"}

#All upper case and num letters
ucnum_letters = {0:"A",1:"B",2:"0",3:"C",4:"D",5:"1",6:"E",7:"F",8:"2",9:"G",10:"H",11:"3",12:"I",13:"J",14:"4",15:"K",16:"L",17:"5",18:"M",19:"N",20:"6",21:"O",22:"P",23:"7",24:"Q",25:"R",26:"8",27:"S",28:"T",29:"9",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z"}

#All upper case and num letters
allmixed_letters = {0:"A",1:"B",2:"0",3:"C",4:"D",5:"1",6:"E",7:"F",8:"2",9:"G",10:"H",11:"3",12:"I",13:"J",14:"4",15:"K",16:"L",17:"5",18:"M",19:"N",20:"6",21:"O",22:"P",23:"7",24:"Q",25:"R",26:"8",27:"S",28:"T",29:"9",30:"U",31:"V",32:"W",33:"X",34:"Y",35:"Z",36:"a",37:"b",38:"0",39:"c",40:"d",41:"1",42:"e",43:"f",44:"2",45:"g",46:"h",47:"3",48:"i",49:"j",50:"4",51:"k",52:"l",53:"5",54:"m",55:"n",56:"6",57:"o",58:"p",59:"7",60:"q",61:"r",62:"8",63:"s",64:"t",65:"9",66:"u",67:"v",68:"w",69:"x",70:"y",71:"z"}

#Dictionary tmp
tmpDic = []

#Maximum of words to generate
maxWords = 100

#Type of char in word in int(
# 1 = lc_letters, 2 = uc_letters, 3 = numbers,
# 4 = lc_letters+uc_letters Mixed, 5 = lc_letters+numbers Mixed, 6 = uc_letters+numbers Mixed,
# 7 = lc_letters+uc_letters, 8 = lc_letters+numbers, 9 = uc_letters+numbers,
# 10 = All Mixed, 11= All
# )
typeCharNumber = 7

#Type of char in word in string
typeCharString = "lc_letters+uc_letters";

#exploit = 1 == RUN
exploit = 0

##MENU

#Convert number enter by user to string
def typeCharNumberToString():
    global typeCharNumber
    global typeCharString
    if typeCharNumber == 1:
        typeCharString = "lc_letters"
    elif typeCharNumber == 2:        
        typeCharString = "uc_letters"
    elif typeCharNumber == 3:        
        typeCharString = "numbers"
    elif typeCharNumber == 4:        
        typeCharString = "lc_letters+uc_letters MIXED"
    elif typeCharNumber == 5:        
        typeCharString = "lc_letters+numbers MIXED"
    elif typeCharNumber == 6:        
        typeCharString = "uc_letters+numbers MIXED"
    elif typeCharNumber == 7:        
        typeCharString = "lc_letters+uc_letters"
    elif typeCharNumber == 8:        
        typeCharString = "lc_letters+numbers"
    elif typeCharNumber == 9:        
        typeCharString = "uc_letters+numbers"
    elif typeCharNumber == 10:        
        typeCharString = "All MIXED"
    elif typeCharNumber == 11:        
        typeCharString = "All"
    else:
        print "Error"

#Display principal menu
def displayMenu():
    global lengthWords
    global typeCharString
    global maxWords
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print "* 1 > Chose word length : ",lengthWords
    print "* 2 > Chose type of char in word: ",typeCharString
    print "* 3 > Chose number of words : ",maxWords
    print "* 4 > RUN"
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    displayChoices()

#Display menu for type of dictionary
def displayAllCaseMenu():
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"
    print "* 1 > lc_letters"
    print "* 2 > uc_letters"
    print "* 3 > numbers"
    print "* 4 > lc_letters+uc_letters Mixed"
    print "* 5 > lc_letters+numbers Mixed"
    print "* 6 > uc_letters+numbers Mixed"
    print "* 7 > lc_letters+uc_letters"
    print "* 8 > lc_letters+numbers"
    print "* 9 > uc_letters+numbers"
    print "* 10 > All Mixed"
    print "* 11 > All"
    print "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*"

#Display all choices to user
def displayChoices():
    global lengthWords
    global typeCharNumber
    global maxWords
    global exploit
    response = int(raw_input("Choice : "))
    if response == 1:
        lengthWords = int(raw_input("Word length : "))
    elif response == 2:
        displayAllCaseMenu()
        typeCharNumber = int(raw_input("Choice : "))
        typeCharNumberToString()
    elif response == 3:
        maxWords = int(raw_input("Number of words : "))
    elif response == 4:
        exploit = 1
    else:
        print "Error"

##./MENU

#Get random number between min and max
def getRandomNumber(min,max):
    return randint(min,max)

##LC

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
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./LC

##UC

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
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

#./UC

##NUM

#Generate random number word with length
def generateNUMRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,9)
        letter = numbers[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all number words with max words
def loadAllNUMRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateNUMRandomWord()        
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./NUM

##LCUC

#Generate random number word with length
def generateLCUCRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,51)
        letter = uclc_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all number words with max words
def loadAllLCUCRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateLCUCRandomWord()        
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./LCUC

##LCNUM

#Generate random number word with length
def generateLCNUMRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,35)
        letter = lcnum_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all number words with max words
def loadAllLCNUMRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateLCNUMRandomWord()        
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./LCNUM

##UCNUM

#Generate random number word with length
def generateUCNUMRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,35)
        letter = ucnum_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all number words with max words
def loadAllUCNUMRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateUCNUMRandomWord()        
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./UCNUM

##ALLMIXED

#Generate random number word with length
def generateAllMixedRandomWord():
    cursor = 0
    word = ""
    while cursor < lengthWords:
        rnd = getRandomNumber(0,71)
        letter = allmixed_letters[rnd]
        word = ''.join([word, letter])
        cursor = cursor+1
    return word

#Generate all number words with max words
def loadAllAllMixedRandomWord():
    cursor = 0
    while cursor < maxWords:
        word = generateAllMixedRandomWord()        
        if word not in tmpDic:     
            tmpDic.append(word) 
            cursor = cursor+1
        else:
            print "IN > ",word

##./ALLMIXED

def run():
    global typeCharNumber
    global exploit
    try:
        while exploit == 0:
            displayMenu()
        #LC
        if typeCharNumber == 1:
            loadAllLCRandomWord()
        #UC
        elif typeCharNumber == 2:
            loadAllUCRandomWord()
        #NUM
        elif typeCharNumber == 3:
            loadAllNUMRandomWord()
        #UCLCMIXED
        elif typeCharNumber == 4:
            loadAllLCUCRandomWord()
        #LCNUMMIXED
        elif typeCharNumber == 5:
            loadAllLCNUMRandomWord()
        #UCNUMMIXED
        elif typeCharNumber == 6:
            loadAllUCNUMRandomWord()
        #UCLC
        elif typeCharNumber == 7:
            loadAllLCRandomWord()
            loadAllUCRandomWord()
        #LCNUM
        elif typeCharNumber == 8:
            loadAllLCRandomWord()
            loadAllNUMRandomWord()
        #UCNUM
        elif typeCharNumber == 9:
            loadAllUCRandomWord()
            loadAllNUMRandomWord()
        #UCNUM
        elif typeCharNumber == 10:
            loadAllAllMixedRandomWord()
        #ALL
        elif typeCharNumber == 11:
            loadAllUCRandomWord()
            loadAllLCRandomWord()
            loadAllNUMRandomWord()
        else:
            print "Error"
    except KeyboardInterrupt, e:
        print "KeyboardInterrupt > ", e
    
run()
#File dictionary
filename = "dic-"+typeCharString+"-"+str(lengthWords)+".txt"
file = open(filename,"w")

#Write in file
for i in tmpDic:
    file.writelines(i+'\n')
file.close()