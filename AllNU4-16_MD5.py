import time
import hashlib
#All num
num = ["0","1","2","3","4","5","6","7","8","9"]


lenght = raw_input("Lenght : ")

start_time = time.time()
if lenght == "4":
    file = open("DIC_num_4.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        word = a+b+c+d
                        md5 = hashlib.md5(word).hexdigest()
                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "5":
    file = open("DIC_num_5.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            word = a+b+c+d+e
                            md5 = hashlib.md5(word).hexdigest()
                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "6":
    file = open("DIC_num_6.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                word = a+b+c+d+e+f
                                md5 = hashlib.md5(word).hexdigest()
                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "7":
    file = open("DIC_num_7.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    word = a+b+c+d+e+f+g
                                    md5 = hashlib.md5(word).hexdigest()
                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "8":
    file = open("DIC_num_8.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        word = a+b+c+d+e+f+g+h
                                        md5 = hashlib.md5(word).hexdigest()
                                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "9":
    file = open("DIC_num_9.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            word = a+b+c+d+e+f+g+h+i
                                            md5 = hashlib.md5(word).hexdigest()
                                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "10":
    file = open("DIC_num_10.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                word = a+b+c+d+e+f+g+h+i+j
                                                md5 = hashlib.md5(word).hexdigest()
                                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "11":
    file = open("DIC_num_11.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    word = a+b+c+d+e+f+g+h+i+j+k
                                                    md5 = hashlib.md5(word).hexdigest()
                                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "12":
    file = open("DIC_num_12.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    for l in num:
                                                        word = a+b+c+d+e+f+g+h+i+j+k+l
                                                        md5 = hashlib.md5(word).hexdigest()
                                                        file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "13":
    file = open("DIC_num_13.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    for l in num:
                                                        for m in num:
                                                            word = a+b+c+d+e+f+g+h+i+j+k+l+m
                                                            md5 = hashlib.md5(word).hexdigest()
                                                            file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "14":
    file = open("DIC_num_14.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    for l in num:
                                                        for m in num:
                                                            for n in num:
                                                                word = a+b+c+d+e+f+g+h+i+j+k+l+m+n
                                                                md5 = hashlib.md5(word).hexdigest()
                                                                file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "15":
    file = open("DIC_num_15.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    for l in num:
                                                        for m in num:
                                                            for n in num:
                                                                for o in num:
                                                                    word = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o
                                                                    md5 = hashlib.md5(word).hexdigest()
                                                                    file.write(word+":"+md5+"\n")
        print "DONE"
        file.close()
    except KeyboardInterrupt:
        print "KeyboardInterrupt"
elif lenght == "16":
    file = open("DIC_num_16.txt.txt","w")
    try:
        for a in num:
            print a
            for b in num:
                for c in num:
                    for d in num:
                        for e in num:
                            for f in num:
                                for g in num:
                                    for h in num:
                                        for i in num:
                                            for j in num:
                                                for k in num:
                                                    for l in num:
                                                        for m in num:
                                                            for n in num:
                                                                for o in num:
                                                                    for p in num:
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