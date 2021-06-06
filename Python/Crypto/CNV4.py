import time, random, os
def load(prefisso,iterazione,totale):

    try:
        percentuale=(('{0:.'+str(1)+'f}').format(100*(iterazione/float(totale))))  
        lunghezza=int(100*iterazione//totale)
        barra= '#'*lunghezza+'-'*(100-lunghezza)
        print(f'\r{prefisso}: <{barra}> | {percentuale}%',end='\r')
        if iterazione==totale:
            print()
    except Exception as e:
        print(e)
def NewFile(text,name1,a,b):
    
    
    name = b +".cn"
    
    try:
        if text != "":
            with open( name1, "w+")as f:
                #os.rename(name1,name1+".cn")
                print("[+] i'm opening file")
                i=0
                l=len(text)
                for symbols in text:
                    i+=1
                    load("Encoding",i,l)
                    car = ord(symbols)
                    spazio = ""
                    carattere = str(bin(int(car)))
                    fi = carattere [2:]
                    time.sleep(0.01)
                    if "1" in fi:
                        fi = fi.replace("1","e")
                    if "0" in fi:
                        fi = fi.replace("0","c")
                    if "ee" in fi:
                        fi = fi.replace("ee", "E")
                    if "cc" in fi:
                        fi = fi.replace("cc", "C")
                    if "ec" in fi:
                        fi = fi.replace("ec", "I")

                    if "ce" in fi:
                        fi = fi.replace("ce", "i")
                        
                    if "cE" in fi:
                        fi = fi.replace("cE", "D")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "d")
                        
                    if "Ce" in fi:
                        fi = fi.replace("Ce", "F")
                        
                    if "eC" in fi:
                        fi = fi.replace("eC", "f")
                        
                    if "CC" in fi:
                        fi = fi.replace("CC", "G")
                        
                    if "EE" in fi:
                        fi = fi.replace("EE", "g")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "H")
                        
                    if "CE" in fi:
                        fi = fi.replace("Ce", "H")
                    num = random.randint(1,8)
                    if num == 1:
                        spazio = "U"
                    if num == 2: 
                        spazio = "W"  
                    if num == 3:
                        spazio = "K"
                    if num == 4:
                        spazio = "J"
                    if num == 5:
                        spazio = "Y"
                    if num == 6:
                        spazio = "R"
                    if num == 7:
                        spazio = "A"
                    if num == 8:
                        spazio = "O"           
                    #time.sleep(0.1)
                    f.write(fi+spazio)
                    #print(f"[+] i'm writing {symbols} in file")
                f.close()
                #print ("---Progress: 0%---")
                #time.sleep(1)
            #    print ("---Progress: 50%---")
           #     #
           #     print ("---Progress: 75%---")
           #     #time.sleep(1)
           #     print ("---Progress: 100%---")
           #     time.sleep(1)
           #     print ("[!] PROCESS COMPLETE")
                try:
                    my_file = name1
                    base = os.path.splitext(my_file)[0]
                    os.rename(my_file, name1 + '.cn')
                    c = input ("Press Any Key To Continue...")
                except Exception as e:
                    #print(e)
                    pass
        else:
            with open( name, "w+")as f:
                i=0
                print("[+] i'm opening file")
                l=len(a)
                for symbols in a:
                    i+=1
                    load("Encrypting",i,l)
                    car = ord(symbols)
                    spazio = ""
                    carattere = str(bin(int(car)))
                    fi = carattere [2:]
                    #time.sleep(0.5)
                    if "1" in fi:
                        fi = fi.replace("1","e")
                    if "0" in fi:
                        fi = fi.replace("0","c")
                    if "ee" in fi:
                        fi = fi.replace("ee", "E")
                    if "cc" in fi:
                        fi = fi.replace("cc", "C")
                    if "ec" in fi:
                        fi = fi.replace("ec", "I")

                    if "ce" in fi:
                        fi = fi.replace("ce", "i")
                        
                    if "cE" in fi:
                        fi = fi.replace("cE", "D")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "d")
                        
                    if "Ce" in fi:
                        fi = fi.replace("Ce", "F")
                        
                    if "eC" in fi:
                        fi = fi.replace("eC", "f")
                        
                    if "CC" in fi:
                        fi = fi.replace("CC", "G")
                        
                    if "EE" in fi:
                        fi = fi.replace("EE", "g")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "H")
                        
                    if "CE" in fi:
                        fi = fi.replace("Ce", "H")
                    num = random.randint(1,8)
                    if num == 1:
                        spazio = "U"
                    if num == 2: 
                        spazio = "W"  
                    if num == 3:
                        spazio = "K"
                    if num == 4:
                        spazio = "J"
                    if num == 5:
                        spazio = "Y"
                    if num == 6:
                        spazio = "R"
                    if num == 7:
                        spazio = "A"
                    if num == 8:
                        spazio = "O"           
                    
                    f.write(fi+spazio)
                    time.sleep(0.01)
                    #print(f"[+] i'm writing {symbols} in file")
                f.close()
                try:
                    my_file = name1
                    base = os.path.splitext(my_file)[0]
                    os.rename(my_file, my_file + '.cn')
                    c = input ("Press Any Key To Continue...")
                except Exception as e:
                    print(e)
                
#                print ("---Progress: 0%---")
#                #time.sleep(1)
#                print ("---Progress: 50%---")
                 
#                print ("---Progress: 75%---")
#                #time.sleep(1)
#                print ("---Progress: 100%---")
#                time.sleep(1)
                #print ("[!] PROCESS COMPLETE")
                c = input ("Press Any Key To Continue...")
    except:
        print("ERROR! You Must Respond Yes!")
        with open( name1, "w+")as f:
            f.write(text)
"""            with open( name, "w+")as f:
                print("[+] i'm opening file")
                for symbols in a:
                    car = ord(symbols)
                    spazio = ""
                    carattere = str(bin(int(car)))
                    fi = carattere [2:]
                    #time.sleep(0.5)
                    if "1" in fi:
                        fi = fi.replace("1","e")
                    if "0" in fi:
                        fi = fi.replace("0","c")
                    if "ee" in fi:
                        fi = fi.replace("ee", "E")
                    if "cc" in fi:
                        fi = fi.replace("cc", "C")
                    if "ec" in fi:
                        fi = fi.replace("ec", "I")

                    if "ce" in fi:
                        fi = fi.replace("ce", "i")
                        
                    if "cE" in fi:
                        fi = fi.replace("cE", "D")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "d")
                        
                    if "Ce" in fi:
                        fi = fi.replace("Ce", "F")
                        
                    if "eC" in fi:
                        fi = fi.replace("eC", "f")
                        
                    if "CC" in fi:
                        fi = fi.replace("CC", "G")
                        
                    if "EE" in fi:
                        fi = fi.replace("EE", "g")
                        
                    if "Ec" in fi:
                        fi = fi.replace("Ec", "H")
                        
                    if "CE" in fi:
                        fi = fi.replace("Ce", "H")
                    num = random.randint(1,8)
                    if num == 1:
                        spazio = "U"
                    if num == 2: 
                        spazio = "W"  
                    if num == 3:
                        spazio = "K"
                    if num == 4:
                        spazio = "J"
                    if num == 5:
                        spazio = "Y"
                    if num == 6:
                        spazio = "R"
                    if num == 7:
                        spazio = "A"
                    if num == 8:
                        spazio = "O"           
                    
                    f.write(fi+spazio)
                    print(f"[+] i'm writing {symbols} in file")
                f.close()
                print ("---Progress: 0%---")
                #time.sleep(1)
                print ("---Progress: 50%---")
                #time.sleep(0.5)
                print ("---Progress: 75%---")
                #time.sleep(1)
                print ("---Progress: 100%---")
                time.sleep(1)
                print ("[!] PROCESS COMPLETE")
                c = input ("Press Any Key To Continue...")"""
def ReadFile( name,a,b):
    testo = ""

    try:
        try:
            if name != "":
                with open(name , "r+") as f:
                    print("[+] I'm opening file")
                    #time.sleep(1)
                    print(f"[+] I'm reading ")
                    Text = f.read()
                    array = 0
                    a = Text.replace("U","-")
                    a1 = a.replace("W" ,"-")
                    a2 = a1.replace("K" ,"-")
                    a3 = a2.replace("J" ,"-")
                    a4 = a3.replace( "Y","-")
                    a5 = a4.replace("R" ,"-")
                    a6 = a5.replace( "A","-")
                    a7 = a6.replace( "O","-")
                    a8 = a7.replace (" ","")
                    c = a8.split("-")
                    array = len(c)
                    array -= 1
                    del  c[array]
                    print(c)    
                    i=0       
                    l=len(c)
                    for line in c:
                        i+=1
                        load("Decoding",i,l)
                        
                        fi = line
                        while True:

                            #time.sleep(0.01)
                            if "E" in fi:
                                fi = fi.replace("E", "ee")
                            if "C" in fi:
                                fi = fi.replace("C", "cc")
                            if "I" in fi:
                                fi = fi.replace("I", "ec")

                            if "i" in fi:
                                fi = fi.replace("i", "ce")
                                
                            if "D" in fi:
                                fi = fi.replace("D", "cE")
                                
                            if "d" in fi:
                                fi = fi.replace("d", "Ec")
                                
                            if "F" in fi:
                                fi = fi.replace("F", "Ce")
                                
                            if "f" in fi:
                                fi = fi.replace("f", "eC")
                                
                            if "G" in fi:
                                fi = fi.replace("G", "CC")
                                
                            if "g" in fi:
                                fi = fi.replace("g", "EE")
                                
                            if "H" in fi:
                                fi = fi.replace("H", "EC")
                                
                            if "h" in fi:
                                fi = fi.replace("h", "CE")
                            if "e" in fi:
                                fi = fi.replace("e", "1")
                            if "c" in fi:
                                fi = fi.replace("c", "0")

                            #print(f"LETTER --> {fi}")
                            try:
                                a = int(fi)
                                break
                            except:
                                pass
                                #print("###Another Run###")

                        d = int(fi , 2)
                        k = chr(d)
                        testo = testo + k
                    #time.sleep(1)
                    print("[+] I'm translating file")
                    #time.sleep(1)
                    print("[!] PROCESS COMPLETE")
                    print("##########################")
                    print("-->\n"+testo)
                    print("##########################")
                    f.close()
                    with open(name,"w+") as f:
                        f.write(testo)
                        
                    try:
                        my_file = name
                        base = os.path.splitext(my_file)[0]
                        os.rename(my_file, base)
                        c = input ("Press Any Key To Continue...")
                    except Exception as e:
                        print(e)
                #c = input ("Press Any Key To Continue...")
            else:
                with open(b , "r") as f:
                    
                    print("[+] I'm opening file")
                    time.sleep(1)
                    print(f"[+] I'm reading ")
                    Text = f.read()
                    array = 0
                    a = Text.replace("U","-")
                    a1 = a.replace("W" ,"-")
                    a2 = a1.replace("K" ,"-")
                    a3 = a2.replace("J" ,"-")
                    a4 = a3.replace( "Y","-")
                    a5 = a4.replace("R" ,"-")
                    a6 = a5.replace( "A","-")
                    a7 = a6.replace( "O","-")
                    a8 = a7.replace (" ","")
                    c = a8.split("-")
                    array = len(c)
                    array -= 1
                    del  c[array]
                    print(c)    
                    i=0
                    l=len(c)       
                    for line in c:
                        i+=1
                        load("Decoding",i,l)
                        fi = line
                        while True:

                            time.sleep(0.01)
                            if "E" in fi:
                                fi = fi.replace("E", "ee")
                            if "C" in fi:
                                fi = fi.replace("C", "cc")
                            if "I" in fi:
                                fi = fi.replace("I", "ec")

                            if "i" in fi:
                                fi = fi.replace("i", "ce")
                                
                            if "D" in fi:
                                fi = fi.replace("D", "cE")
                                
                            if "d" in fi:
                                fi = fi.replace("d", "Ec")
                                
                            if "F" in fi:
                                fi = fi.replace("F", "Ce")
                                
                            if "f" in fi:
                                fi = fi.replace("f", "eC")
                                
                            if "G" in fi:
                                fi = fi.replace("G", "CC")
                                
                            if "g" in fi:
                                fi = fi.replace("g", "EE")
                                
                            if "H" in fi:
                                fi = fi.replace("H", "EC")
                                
                            if "h" in fi:
                                fi = fi.replace("h", "CE")
                            if "e" in fi:
                                fi = fi.replace("e", "1")
                            if "c" in fi:
                                fi = fi.replace("c", "0")

                            #print(f"LETTER --> {fi}")
                            try:
                                a = int(fi)
                                break
                            except:
                                pass
                                #print("###Another Run###")

                        d = int(fi , 2)
                        k = chr(d)
                        testo = testo + k
                    #time.sleep(1)
                    print("[+] I'm translating file")
                    #time.sleep(1)
                    print("[!] PROCESS COMPLETE")
                    print("##########################")
                    print("-->"+testo)
                    print("##########################")
                c = input ("Press Any Key To Continue...")            

        except Exception as e:
            print(f"Uff... => {e}")
    except:
        print(f"""
        ERROR!:
            -I COULD NOT FIND {b} FILE
            -AN ERROR WAS OCCURRED
        """)
        c = input ("Press Any Key To Continue...")
def AutoFile():
    file = input("[?] Insert File Path + Name >>> ")
    if not file.endswith('.cn'):
        choice=input("""[!] This File is Not Encrypted,
                Are you shure that you want to 
                encrypt that?                
                This Action Could Be unreversable.

                Choice =$ """) 
        if choice == 'y' or "yes" or "Yes" or "Y":
            with open (file, "r") as f:
                text = f.read()
                f.close()
                NewFile(text,file,"","")
        
        
    else:
        choice=input("""[!] This File is Alredy Encrypted,
                would you like to decrypt that?  
                 
                for info read -help

                Choice =$ """)
        ReadFile(file,"","")
def help ():
    print("""
    type:
    ==============================
    "1" for Encrypt a Text In File 
    "2" for Decrypt a Text In File
    "3" for Auto Encrypt od Decrypt
    a file.
    "-H" for manual
    "Leak" for a Next Version Leak
    ##############################
              ATTENTION!
    If you are tring to encrypt a 
    video or a file that needs a 
    checksum, the file could be
    corrupted in the future.
    ##############################
              DISCLAIMER!
    Even If the encryption was fine,
    the file could be corrupted.
    It is raccomanded to do a 
    BackUp of the file in question.
    ==============================
    """)
def Leak():
    print("""
    ==============================
    In The Future Version I Would 
    Like To Add GUI

    --Ettore
    ==============================
    """)
def ls():
    a = os.getcwd()
    b = os.listdir(a)
    print(b)
def main():
    while True:
        a1 = input("CNV1@CNV1~$ ")  
        try:     
            if a1 == "1":
                a = input("[?] Insert Text >>> ")
                b = input("[?] Insert File Name >>> ")
                NewFile("","",a,b)
            if a1 == "2":
                
                b = input("[?] Insert File Name >>> ")
                ReadFile("","",b)
            if a1 == "3":
                AutoFile()
            if a1 == "-H":
                help()
            if a1 == "leak":
                Leak()

            if a1 != "1":
                
                if a1 != "2":
                    
                    if a1 != "3":
                        
                        if a1 != "-H":
                            print(f"Syntax Error at --> {a1}")
        except Exception as e:
            print(f"Uff...{e}")
def Identificazione():
    print("""
    #####################################
    #<<<SlickSpore's Cryptatron.>>>#
    #<<<         Version 4           >>>#
    #####################################

    for help type -H
    ======================================================================================================================
    This Program Encrypts Text Bit To Bit Following the innovative extension: ".cn".
    It is impossible to decrypt a file with your bare hands, because a very complex method of hand-shake crypting is used.

    All credits to Ettore Caccioli.
    ======================================================================================================================
    
    USE THIS PROGRAM FOR LEGAL PURPOSES ONLY

    the staff.
    
    """)
    main()
Identificazione()
