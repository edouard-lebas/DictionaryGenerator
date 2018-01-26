import time
import hashlib
#All lower case letters
lc_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


lenght = raw_input("Lenght : ")

start_time = time.time()
if lenght == "4":
    file = open("DIC_lcletters_4.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        word = a+b+c+d
                        md5 = hashlib.md5(word).hexdigest()
                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "5":
    file = open("DIC_lcletters_5.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            word = a+b+c+d+e
                            md5 = hashlib.md5(word).hexdigest()
                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "6":
    file = open("DIC_lcletters_6.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                word = a+b+c+d+e+f
                                md5 = hashlib.md5(word).hexdigest()
                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "7":
    file = open("DIC_lcletters_7.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    word = a+b+c+d+e+f+g
                                    md5 = hashlib.md5(word).hexdigest()
                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "8":
    file = open("DIC_lcletters_8.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        word = a+b+c+d+e+f+g+h
                                        md5 = hashlib.md5(word).hexdigest()
                                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "9":
    file = open("DIC_lcletters_9.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            word = a+b+c+d+e+f+g+h+i
                                            md5 = hashlib.md5(word).hexdigest()
                                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "10":
    file = open("DIC_lcletters_10.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                word = a+b+c+d+e+f+g+h+i+j
                                                md5 = hashlib.md5(word).hexdigest()
                                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "11":
    file = open("DIC_lcletters_11.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    word = a+b+c+d+e+f+g+h+i+j+k
                                                    md5 = hashlib.md5(word).hexdigest()
                                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "12":
    file = open("DIC_lcletters_12.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    for l in lc_letters:
                                                        word = a+b+c+d+e+f+g+h+i+j+k+l
                                                        md5 = hashlib.md5(word).hexdigest()
                                                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "13":
    file = open("DIC_lcletters_13.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    for l in lc_letters:
                                                        for m in lc_letters:
                                                            word = a+b+c+d+e+f+g+h+i+j+k+l+m
                                                            md5 = hashlib.md5(word).hexdigest()
                                                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "14":
    file = open("DIC_lcletters_14.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    for l in lc_letters:
                                                        for m in lc_letters:
                                                            for n in lc_letters:
                                                                word = a+b+c+d+e+f+g+h+i+j+k+l+m+n
                                                                md5 = hashlib.md5(word).hexdigest()
                                                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "15":
    file = open("DIC_lcletters_15.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    for l in lc_letters:
                                                        for m in lc_letters:
                                                            for n in lc_letters:
                                                                for o in lc_letters:
                                                                    word = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o
                                                                    md5 = hashlib.md5(word).hexdigest()
                                                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "16":
    file = open("DIC_lcletters_16.txt.txt","w")
    try:
        for a in lc_letters:
            print a
            for b in lc_letters:
                for c in lc_letters:
                    for d in lc_letters:
                        for e in lc_letters:
                            for f in lc_letters:
                                for g in lc_letters:
                                    for h in lc_letters:
                                        for i in lc_letters:
                                            for j in lc_letters:
                                                for k in lc_letters:
                                                    for l in lc_letters:
                                                        for m in lc_letters:
                                                            for n in lc_letters:
                                                                for o in lc_letters:
                                                                    for p in lc_letters:
                                                                        word = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p
                                                                        md5 = hashlib.md5(word).hexdigest()
                                                                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
else:
    print "Erreur"

totalTime = time.time() - start_time
print totalTime