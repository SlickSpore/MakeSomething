import tkinter as tk
#from # import #
#from tkinter import Label, Message, filedialog
import sys
import socket
import threading
from time import sleep
#from tkinter.constants import TRUE
import os
path = os.getcwd()
#print(path)
font = "Calibri "
connectionh = None
message = None  
starter = True
name = "Tris! Host"
sended = [None,0,0,0,0,0,0,0,0,0]
used = [None,0,0,0,0,0,0,0,0,0]
gameplayer= 0
indexuse = 1
wait = False
delay= False
gamer = 1
class triss1():
    
    def recve(self):
        global message
        global used
        global wait
        global delay
        global starter
        global sended
        global name
        global indexuse
        global gamer
        delay = True
        a = connectionh.recv(1024)
        message = a

        if message != None:
            wait = False
            #print(used)
        if gameplayer == 0:
            if message==b'1':
                if used[1]==0:
                    self.but1.config(text="X")
                    used[1]=1
                    sended[1] = 1
                    self.round[1] = 2
                    #print(used)
                    self.check(0) 
                else:
                    pass
            if message==b'2':
                if used[2]==0:
                    self.but2.config(text="X")
                    used[2]=1
                    sended[2] = 1
                    self.round[2] = 2
                    
                    self.check(0) #print(self.round)                
                else:
                    pass
            if message==b'3':
                if used[3]==0:
                    self.but3.config(text="X")
                    used[3]=1
                    sended[3] = 1
                    self.round[3] = 2
                    #print(self.round)   
                    
                    self.check(0)             
                else:
                    pass
            if message==b'4':
                if used[4]==0:
                    self.but4.config(text="X")
                    used[4]=1
                    self.round[4] = 2
                    self.check(0) 
                    sended[4] = 1
                else:
                    pass
            if message==b'5':
                if used[5]==0:
                    self.but5.config(text="X")
                    used[5]=1
                    sended[5] = 1
                    self.round[5] = 2
                    #print(self.round)                
                    self.check(0) 
                else:
                    pass
            if message==b'6':
                if used[6]==0:
                    self.but6.config(text="X")
                    used[6]=1
                    sended[6] = 1
                    self.round[6] = 2
                    #print(self.round)                
                    self.check(0) 
                else:
                    pass
            if message==b'7':
                if used[7]==0:
                    self.but7.config(text="X")
                    used[7]=1
                    sended[7] = 1
                    self.round[7] = 2
                    #print(self.round)                
                    self.check(0) 
                else:
                    pass
            if message==b'8':
                if used[8]==0:
                    self.but8.config(text="X")
                    used[8]=1
                    sended[8] = 1
                    self.round[8] = 2
                    #print(self.round)                
                    self.check(0) 
                else:
                    pass
            if message==b'9':
                if used[9]==0:
                    self.but9.config(text="X")
                    used[9]=1
                    sended[9] = 1
                    self.round[9] = 2
                    #print(self.round)                
                    self.check(0) 
                    #font = "Calibri "

                else:
                    pass
            if message==b'bye':
                x = threading.Thread(target=menu)
                x.start()
                self.root.destroy()
                connectionh.close()

        if gameplayer == 1:
            if message==b'1':
                if used[1]==0:
                    self.but1.config(text="O")
                    used[1]=1
                    self.round[1] = 2
                    sended[1] = 1
                    self.check(0) 
                else:
                    pass
            if message==b'2':
                if used[2]==0:
                    self.but2.config(text="O")
                    used[2]=1
                    self.round[2] = 2
                    sended[2] = 1
                    self.check(0) 
                else:
                    pass   
            if message==b'3':
                if used[3]==0:
                    self.but3.config(text="O")
                    used[3]=1
                    self.round[3] = 2
                    self.check(0) 
                    sended[3] = 1
                else:
                    pass 
            if message==b'4':
                if used[4]==0:
                    self.but4.config(text="O")
                    used[4]=1
                    self.round[4] = 2
                    self.check(0) 
                    sended[4] = 1
                else:
                    pass 
            if message==b'5':
                if used[5]==0:
                    self.but5.config(text="O")
                    used[5]=1
                    self.round[5] = 2
                    self.check(0) 
                    sended[5] = 1
                else:
                    pass   
            if message==b'6':
                if used[6]==0:
                    self.but6.config(text="O")
                    used[6]=1
                    self.round[6] = 2
                    self.check(0) 
                    sended[6] = 1
                else:
                    pass  
            if message==b'7':
                if used[7]==0:
                    self.but7.config(text="O")
                    used[7]=1
                    self.round[7] = 2
                    self.check(0) 
                    sended[7] = 1
                else:
                    pass
            if message==b'8':
                if used[8]==0:
                    self.but8.config(text="O")
                    used[8]=1
                    self.round[8] = 2
                    sended[8] = 1
                    self.check(0) 
                else:
                    pass
            if message==b'9':
                if used[9]==0:
                    self.but9.config(text="O")
                    used[9]=1
                    self.round[9] = 2
                    self.check(0) 
                    sended[9] = 1
                else:
                    pass
            if message==b'bye':
                x = threading.Thread(target=menu)
                connectionh.close()
                x.start()
                self.root.destroy()
                #menu()
        print("rouns",self.round)
        print("used",used)        
        delay = False
        sys.exit()
        
    def __init__(self):
        global starter
        global name
        
        index = 2
        self.start = False
        self.uno = 0
        self.game = [0,0,0,0,0,0,0,0,0]
        self.round = [None,0,0,0,0,0,0,0,0,0]
        self.root = tk.Tk()
        self.root.geometry("240x350")
        self.root.title(name)
        #
 
        self.but1 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno1,bg = "White")
        self.but1.grid(column=1,row=1)
        self.but2 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno2,bg = "White")
        self.but2.grid(column=2,row=1)
        self.but3 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno3,bg = "White")
        self.but3.grid(column=3,row=1)
        self.but4 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno4,bg = "White")
        self.but4.grid(column=1,row=2)        
        self.but5 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno5,bg = "White")
        self.but5.grid(column=2,row=2)            
        self.but6 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno6,bg = "White")
        self.but6.grid(column=3,row=2)            
        self.but7 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno7,bg = "White")
        self.but7.grid(column=1,row=3)        
        self.but8 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno8,bg = "White")
        self.but8.grid(column=2,row=3)            
        self.but9 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno9,bg = "White")
        self.but9.grid(column=3,row=3)  

        self.bye = tk.Button(self.root,text="LEAVE",height = 5,bg="red", width = 10,command = self.leave)
        self.bye.grid(column=1,row=4)
        #self.player = tk.Button(self.root,text="PLAYER",height = 5, width = 10,command = self.player)
        #self.player.grid(column=3,row=4) 
        if name == "Tris! Host":
            self.player1 = tk.Label(self.root,text="X",height = 5, width = 10)
            self.player1.grid(column=2,row=4) 
        else:
            self.player1 = tk.Label(self.root,text="O",height = 5, width = 10)
            self.player1.grid(column=2,row=4) 
            
        if starter == False:
            global message
            global wait
            x = threading.Thread(target=self.recve)
            x.start()
            wait = True
        self.root.mainloop()

    def leave(self):
        print(self.root)
        #connectionh.send(b'bye')
        connectionh.close()
        # self.root.destroy()
        #t = threading.Thread(target=menu)
        #t.setDaemon(True)
       # t.start()
       # menu()
        self.root.destroy()
        exit()
    def player(self):
        if self.start == False:
            self.uno +=1
            if (self.uno%2)==0:
                self.player1.config(text="X")
            else:
                self.player1.config(text="O")
        else:
            pass
    def reset(self):
        
        self.start = False
        self.game[0]=0
        self.game[1]=0
        self.game[2]=0
        self.game[3]=0
        self.game[4]=0
        self.game[5]=0
        self.game[6]=0
        self.game[7]=0
        self.game[8]=0

        self.round[0]=0
        self.round[1]=0
        self.round[2]=0
        self.round[3]=0
        self.round[4]=0
        self.round[5]=0
        self.round[6]=0
        self.round[7]=0
        self.round[8]=0


        self.uno=2
        self.but1.config(text="")
        self.but2.config(text="")
        self.but3.config(text="")       
        self.but4.config(text="")       
        self.but5.config(text="")      
        self.but6.config(text="")      
        self.but7.config(text="")      
        self.but8.config(text="")      
        self.but9.config(text="")

        self.but1.config(bg = "White")
        self.but2.config(bg = "White")
        self.but3.config(bg = "White")       
        self.but4.config(bg = "White")       
        self.but5.config(bg = "White")      
        self.but6.config(bg = "White")      
        self.but7.config(bg = "White")      
        self.but8.config(bg = "White")      
        self.but9.config(bg = "White")
        
    def check(self,game):
        #print(self.round)
        print("rouns",self.round)
        print("used",used) 
        if game == 2:
            if self.round[3]==1 and self.round[6]==1 and self.round[9]==1:
                self.but3.config(bg = "light green")
                self.but6.config(bg = "light green")
                self.but9.config(bg = "light green")  
            if self.round[1]==1 and self.round[4]==1 and self.round[7]==1:
                self.but4.config(bg = "light green")
                self.but7.config(bg = "light green")
                self.but1.config(bg = "light green")  
            if self.round[2]==1 and self.round[5]==1 and self.round[8]==1:
                self.but2.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but8.config(bg = "light green") 

            if self.round[1]==1 and self.round[2]==1 and self.round[3]==1:
                self.but1.config(bg = "light green")
                self.but2.config(bg = "light green")
                self.but3.config(bg = "light green")  
            if self.round[4]==1 and self.round[5]==1 and self.round[6]==1:
                self.but4.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but6.config(bg = "light green")  
            if self.round[7]==1 and self.round[8]==1 and self.round[9]==1:
                self.but7.config(bg = "light green")
                self.but8.config(bg = "light green")
                self.but9.config(bg = "light green") 

            if self.round[1]==1 and self.round[5]==1 and self.round[9]==1:
                self.but1.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but9.config(bg = "light green")  
            if self.round[3]==1 and self.round[5]==1 and self.round[7]==1:
                self.but3.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but7.config(bg = "light green") 

            if self.round[3]==2 and self.round[6]==2 and self.round[9]==2:
                self.but3.config(bg = "light green")
                self.but6.config(bg = "light green")
                self.but9.config(bg = "light green")  
            if self.round[1]==2 and self.round[4]==2 and self.round[7]==2:
                self.but4.config(bg = "light green")
                self.but7.config(bg = "light green")
                self.but1.config(bg = "light green")  
            if self.round[2]==2 and self.round[5]==2 and self.round[8]==2:
                self.but2.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but8.config(bg = "light green") 

            if self.round[1]==2 and self.round[2]==2 and self.round[3]==2:
                self.but1.config(bg = "light green")
                self.but2.config(bg = "light green")
                self.but3.config(bg = "light green")  
            if self.round[4]==2 and self.round[5]==2 and self.round[6]==2:
                self.but4.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but6.config(bg = "light green")  
            if self.round[7]==2 and self.round[8]==2 and self.round[9]==2:
                self.but7.config(bg = "light green")
                self.but8.config(bg = "light green")
                self.but9.config(bg = "light green") 

            if self.round[1]==2 and self.round[5]==2 and self.round[9]==2:
                self.but1.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but9.config(bg = "light green")  
            if self.round[3]==2 and self.round[5]==2 and self.round[7]==2:
                self.but3.config(bg = "light green")
                self.but5.config(bg = "light green")
                self.but7.config(bg = "light green") 
        if game == 0:
            if self.round[3]==1 and self.round[6]==1 and self.round[9]==1:
                self.but3.config(bg = "red") 
                self.but6.config(bg = "red") 
                self.but9.config(bg = "red") 
            if self.round[1]==1 and self.round[4]==1 and self.round[7]==1:
                self.but4.config(bg = "red") 
                self.but7.config(bg = "red") 
                self.but1.config(bg = "red")  
            if self.round[2]==1 and self.round[5]==1 and self.round[8]==1:
                self.but2.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but8.config(bg = "red") 

            if self.round[1]==1 and self.round[2]==1 and self.round[3]==1:
                self.but1.config(bg = "red") 
                self.but2.config(bg = "red") 
                self.but3.config(bg = "red")  
            if self.round[4]==1 and self.round[5]==1 and self.round[6]==1:
                self.but4.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but6.config(bg = "red")  
            if self.round[7]==1 and self.round[8]==1 and self.round[9]==1:
                self.but7.config(bg = "red") 
                self.but8.config(bg = "red") 
                self.but9.config(bg = "red") 

            if self.round[1]==1 and self.round[5]==1 and self.round[9]==1:
                self.but1.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but9.config(bg = "red")  
            if self.round[3]==1 and self.round[5]==1 and self.round[7]==1:
                self.but3.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but7.config(bg = "red") 

            if self.round[3]==2 and self.round[6]==2 and self.round[9]==2:
                self.but3.config(bg = "red") 
                self.but6.config(bg = "red") 
                self.but9.config(bg = "red")  
            if self.round[1]==2 and self.round[4]==2 and self.round[7]==2:
                self.but4.config(bg = "red") 
                self.but7.config(bg = "red") 
                self.but1.config(bg = "red")  
            if self.round[2]==2 and self.round[5]==2 and self.round[8]==2:
                self.but2.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but8.config(bg = "red") 

            if self.round[1]==2 and self.round[2]==2 and self.round[3]==2:
                self.but1.config(bg = "red") 
                self.but2.config(bg = "red") 
                self.but3.config(bg = "red")  
            if self.round[4]==2 and self.round[5]==2 and self.round[6]==2:
                self.but4.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but6.config(bg = "red")  
            if self.round[7]==2 and self.round[8]==2 and self.round[9]==2:
                self.but7.config(bg = "red") 
                self.but8.config(bg = "red") 
                self.but9.config(bg = "red") 

            if self.round[1]==2 and self.round[5]==2 and self.round[9]==2:
                self.but1.config(bg = "red") 
                self.but5.config(bg = "red") 
                self.but9.config(bg = "red")  
            if self.round[3]==2 and self.round[5]==2 and self.round[7]==2:
                self.but3.config(bg = "red")
                self.but5.config(bg = "red")
                self.but7.config(bg = "red") 
    def uno1(self):
        
        global message
        global sended
        global indexuse
        if delay == False:
            if sended[1] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'1')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[1]=1
                
                indexuse = 1
                self.round[1] = 1
                if wait == False:
                    

                    if used[1] !=1:
                        if gameplayer == 0:
                            self.but1.config(text="O")
                            used[1]=1
                        if gameplayer == 1:
                            self.but1.config(text="X")
                            used[1]=1
                    else:
                        pass
            self.check(2)
        else:
            print("SETTED")
        #a = self.recve()
       # print(message)
    def uno2(self):
        global message
        global sended
        global indexuse
        self.check(2)
        if delay == False:

            if sended[2] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'2')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[2]=1
                
                indexuse = 1
                self.round[2] = 1
                if wait == False:
                    

                    if used[2] !=1:
                        if gameplayer == 0:
                            self.but2.config(text="O")
                            used[2]=1
                        if gameplayer == 1:
                            self.but2.config(text="X")
                            used[2]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")        
    def uno3(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[3] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'3')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[3]=1
                self.round[3] = 1
                indexuse = 1
                if wait == False:
                    

                    if used[3] !=1:
                        if gameplayer == 0:
                            self.but3.config(text="O")
                            used[3]=1
                        if gameplayer == 1:
                            self.but3.config(text="X")
                            used[3]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")    
    def uno4(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[4] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'4')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[4]=1
                
                indexuse = 1
                self.round[4] = 1
                if wait == False:
                    

                    if used[4] !=1:
                        if gameplayer == 0:
                            self.but4.config(text="O")
                            used[4]=1
                        if gameplayer == 1:
                            self.but4.config(text="X")
                            used[4]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")
    def uno5(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[5] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'5')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[5]=1
                
                indexuse = 1
                self.round[5] = 1
                if wait == False:
                    

                    if used[5] !=1:
                        if gameplayer == 0:
                            self.but5.config(text="O")
                            used[5]=1
                        if gameplayer == 1:
                            self.but5.config(text="X")
                            used[5]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")
    def uno6(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[6] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'6')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[6]=1
                
                indexuse = 1
                self.round[6] = 1
                if wait == False:
                    

                    if used[6] !=1:
                        if gameplayer == 0:
                            self.but6.config(text="O")
                            used[6]=1
                        if gameplayer == 1:
                            self.but6.config(text="X")
                            used[6]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")
    def uno7(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[7] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'7')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[7]=1
                
                indexuse = 1
                self.round[7] = 1
                if wait == False:
                    

                    if used[7] !=1:
                        if gameplayer == 0:
                            self.but7.config(text="O")
                            used[7]=1
                        if gameplayer == 1:
                            self.but7.config(text="X")
                            used[7]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED") 
    def uno8(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[8] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'8')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[8]=1
                
                indexuse = 1
                self.round[8] = 1
                if wait == False:
                    

                    if used[8] !=1:
                        if gameplayer == 0:
                            self.but8.config(text="O")
                            used[8]=1
                        if gameplayer == 1:
                            self.but8.config(text="X")
                            used[8]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED")
    def uno9(self):
        global message
        global sended
        global indexuse
        if delay == False:

            if sended[9] ==0:
            
            
                #print(connectionh)
                if wait == False:

                    connectionh.send(b'9')
                x = threading.Thread(target=self.recve)
                x.start()
                sended[9]=1
                
                indexuse = 1
                self.round[9] = 1
                if wait == False:
                    

                    if used[9] !=1:
                        if gameplayer == 0:
                            self.but9.config(text="O")
                            used[9]=1
                        if gameplayer == 1:
                            self.but9.config(text="X")
                            used[9]=1
                    else:
                        pass
                self.check(2)
        else:
            print("SETTED") 
class start():
    def __init__(self):
        #240x350
        x = threading.Thread(target=self.lconnect)#, args=triss1())
        x.start()
        a = socket.gethostname()
        self.b = socket.gethostbyname(a)
        self.root1 = tk.Tk()
        self.root1.geometry("370x100")
        self.root1.title("Starting")
        self.label = tk.Label(self.root1,text="         ")
        self.label.grid(column=1,row=1)
        self.root1.iconbitmap(path+'\\tris.ico')
        self.label= tk.Label(self.root1,text="Game hosted on: "+self.b,font=font)
        self.label.grid(column=2,row=2)




        self.root1.mainloop()
    def lconnect(self):
        global connectionh
        global gameplayer
        global message
        global used
        global wait
        global delay
        global starter
        global sended
        global name
        global indexuse
        global gamer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a = socket.gethostname()
        b = socket.gethostbyname(a)
        
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((b,1234))
        s.listen(1)

        conn, addr = s.accept()
        connectionh = conn
        #self.root1.destroy()
        #conn.setblocking(0)
                #connectionh = None
        message = None  
        starter = True
        name = "Tris! Host"
        sended = [None,0,0,0,0,0,0,0,0,0]
        used = [None,0,0,0,0,0,0,0,0,0]
        #gameplayer= 0
        indexuse = 1
        wait = False
        delay= False
        gamer = 1
        a = conn.recv(1024)
        
        if a == b'Hello':
            print("Hosting")
            connectionh.send(b'Hello')
            gameplayer = 1
            #self.label1=tk.Label(text=addr)
            #self.label1.grid()
            #self.labe1=tk.Button(text="QUIT",command=self.quit)
            #self.labe1.grid()
            x = threading.Thread(target=triss1)
            x.start()

            self.root1.destroy()
            #print("something")
            #sys.exit()


class connect():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("265x190")
        self.root.title("Select GameMode")
        #
        self.label = tk.Label(self.root,text="       ")
        self.label.grid(column=1,row=1)
        self.label = tk.Label(self.root,text="Specify The Host",height = 2, width=13,font = font)
        self.label.grid(column=2,row=1)
        self.But = tk.Entry(self.root,font=font)#,height = 2, width=18)
        self.But.grid(column=2,row=2)
        self.But1 = tk.Button(self.root,text="CONNECT",command=self.startc,height = 3, width=13,font = font,fg = "red")
        self.But1.grid(column=2,row=3)
        self.root.mainloop()
    def startc(self):
        x = threading.Thread(target=self.connection)
        x.start()
    def connection(self):
        global connectionh
        global starter
        global name
        global gameplayer
        global gamer
        global sended
        global used
        s = socket.socket()
        a = self.But.get()
        ip=a.split(":")
        port = 1234
        host = ip[0]
        try:
            s.connect((host,port))
            
            s.send(b'Hello')

            a = s.recv(1024)
            if a!='':
                self.label.config(text=host)
                starter = False
                print("Connecting")
                connectionh = s
                gamer = 0
                sended = [None,0,0,0,0,0,0,0,0,0]
                used = [None,0,0,0,0,0,0,0,0,0]
                name = "Tris! Client"
                
                """
                print("ciao")
                triss1()
                """
                
                x = threading.Thread(target=triss1)
                x.start()
                
                self.root.destroy()
                    
                
                
        except Exception as e:
            print(e)
            self.label.config(text="Host Is Down")
            #x.start()

class bind():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x190")
        self.root.title("Select GameMode")
        #

        self.But1 = tk.Button(self.root,text="START",command=self.strat,font=font,height = 8, width=20,fg="GREEN")
        self.But1.grid()
        self.root.mainloop()
    def strat(self):
        self.root.destroy()
        start()
class online():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x190")
        self.root.title("Select GameMode")
        #
        self.But = tk.Button(self.root,text="CONNECT",fg = "Red",bg="WHite",font="Calibri 16",command = self.con,height = 3, width=18)
        self.But.grid()
        self.But1 = tk.Button(self.root,text="BIND",fg = "Blue",bg="WHite",font="Calibri 16",command = self.bind,height = 3, width=18)
        self.But1.grid()
        self.root.mainloop()

    def con(self):
        self.root.destroy()
        connect()
    def bind(self):
        self.root.destroy()
        bind()

class triss:
    
    def __init__(self):
        index = 2
        self.start = False
        self.uno = 0
        self.game = [0,0,0,0,0,0,0,0,0]
        self.round = [0,0,0,0,0,0,0,0,0]
        self.root = tk.Tk()
        self.root.geometry("240x350")
        self.root.title("Tris")
        #
 
        self.but1 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno1,bg = "White")
        self.but1.grid(column=1,row=1)
        self.but2 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno2,bg = "White")
        self.but2.grid(column=2,row=1)
        self.but3 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno3,bg = "White")
        self.but3.grid(column=3,row=1)
        self.but4 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno4,bg = "White")
        self.but4.grid(column=1,row=2)        
        self.but5 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno5,bg = "White")
        self.but5.grid(column=2,row=2)            
        self.but6 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno6,bg = "White")
        self.but6.grid(column=3,row=2)            
        self.but7 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno7,bg = "White")
        self.but7.grid(column=1,row=3)        
        self.but8 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno8,bg = "White")
        self.but8.grid(column=2,row=3)            
        self.but9 = tk.Button(self.root,text="",height = 5, width = 10,command = self.uno9,bg = "White")
        self.but9.grid(column=3,row=3)  
        self.res = tk.Button(self.root,text="RESTART",fg = "red",height = 5, width = 10,command = self.reset)
        self.res.grid(column=1,row=4) 
        self.player = tk.Button(self.root,text="PLAYER",fg = "Green",height = 5, width = 10,command = self.player)
        self.player.grid(column=3,row=4) 
        self.player1 = tk.Label(self.root,text="X",height = 5, width = 10)
        self.player1.grid(column=2,row=4) 
        self.root.mainloop()


    def player(self):
        if self.start == False:
            self.uno +=1
            if (self.uno%2)==0:
                self.player1.config(text="X")
            else:
                self.player1.config(text="O")
        else:
            pass
    def reset(self):
        self.start = False
        self.game[0]=0
        self.game[1]=0
        self.game[2]=0
        self.game[3]=0
        self.game[4]=0
        self.game[5]=0
        self.game[6]=0
        self.game[7]=0
        self.game[8]=0

        self.round[0]=0
        self.round[1]=0
        self.round[2]=0
        self.round[3]=0
        self.round[4]=0
        self.round[5]=0
        self.round[6]=0
        self.round[7]=0
        self.round[8]=0


        self.uno=2
        self.but1.config(text="")
        self.but2.config(text="")
        self.but3.config(text="")       
        self.but4.config(text="")       
        self.but5.config(text="")      
        self.but6.config(text="")      
        self.but7.config(text="")      
        self.but8.config(text="")      
        self.but9.config(text="")

        self.but1.config(bg = "White")
        self.but2.config(bg = "White")
        self.but3.config(bg = "White")       
        self.but4.config(bg = "White")       
        self.but5.config(bg = "White")      
        self.but6.config(bg = "White")      
        self.but7.config(bg = "White")      
        self.but8.config(bg = "White")      
        self.but9.config(bg = "White")
        
    def check(self):
        
        
        if self.round[2]==1 and self.round[5]==1 and self.round[8]==1:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if self.round[0]==1 and self.round[3]==1 and self.round[6]==1:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if self.round[1]==1 and self.round[4]==1 and self.round[7]==1:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if self.round[0]==1 and self.round[1]==1 and self.round[2]==1:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if self.round[3]==1 and self.round[4]==1 and self.round[5]==1:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if self.round[6]==1 and self.round[7]==1 and self.round[8]==1:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if self.round[0]==1 and self.round[4]==1 and self.round[8]==1:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if self.round[2]==1 and self.round[4]==1 and self.round[6]==1:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 

        if self.round[2]==2 and self.round[5]==2 and self.round[8]==2:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if self.round[0]==2 and self.round[3]==2 and self.round[6]==2:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if self.round[1]==2 and self.round[4]==2 and self.round[7]==2:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if self.round[0]==2 and self.round[1]==2 and self.round[2]==2:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if self.round[3]==2 and self.round[4]==2 and self.round[5]==2:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if self.round[6]==2 and self.round[7]==2 and self.round[8]==2:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if self.round[0]==2 and self.round[4]==2 and self.round[8]==2:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if self.round[2]==2 and self.round[4]==2 and self.round[6]==2:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 
    def uno1(self):
        self.start = True
        if self.game[0]==0:

            if (self.uno % 2) == 0:
                self.but1.config(text="X")
                self.uno += 1
                self.round[0]=1
            else:
                self.but1.config(text="O")
                self.uno += 1  
                self.round[0]=2   
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[0]=1      
        self.check()
    def uno2(self):
        self.start = True
        if self.game[1]==0:
            if (self.uno % 2) == 0:
                self.but2.config(text="X")
                self.uno += 1
                self.round[1]=1
            else:
                self.but2.config(text="O")
                self.uno += 1 
                self.round[1]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[1]=1
        self.check()                   
    def uno3(self):
        self.start = True
        if self.game[2]==0:
            if (self.uno % 2) == 0:
                self.but3.config(text="X")
                self.uno += 1
                self.round[2]=1
            else:
                self.but3.config(text="O")
                self.uno += 1  
                self.round[2]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[2]=1                 
        self.check()
    def uno4(self):
        self.start = True
        if self.game[3]==0:
            if (self.uno % 2) == 0:
                self.but4.config(text="X")
                self.uno += 1
                self.round[3]=1
            else:
                self.but4.config(text="O")
                self.uno += 1  
                self.round[3]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[3]=1 
        self.check()
    def uno5(self):
        self.start = True
        if self.game[4]==0:
            if (self.uno % 2) == 0:
                self.but5.config(text="X")
                self.uno += 1
                self.round[4]=1
            else:
                self.but5.config(text="O")
                self.uno += 1  
                self.round[4]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[4]=1
        self.check() 
    def uno6(self):
        self.start = True
        if self.game[5]==0:
            if (self.uno % 2) == 0:
                self.but6.config(text="X")
                self.uno += 1
                self.round[5]=1
            else:
                self.but6.config(text="O")
                self.uno += 1  
                self.round[5]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[5]=1
        self.check() 
    def uno7(self):
        self.start = True
        if self.game[6]==0:
            if (self.uno % 2) == 0:
                self.but7.config(text="X")
                self.uno += 1
                self.round[6]=1
            else:
                self.but7.config(text="O")
                self.uno += 1  
                self.round[6]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[6]=1
        self.check() 
    def uno8(self):
        self.start = True
        if self.game[7]==0:
            if (self.uno % 2) == 0:
                self.but8.config(text="X")
                self.uno += 1
                self.round[7]=1
            else:
                self.but8.config(text="O")
                self.uno += 1  
                self.round[7]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[7]=1
        self.check() 
    def uno9(self):
        self.start = True
        if self.game[8]==0:
            if (self.uno % 2) == 0:
                self.but9.config(text="X")
                self.uno += 1
                self.round[8]=1
            else:
                self.but9.config(text="O")
                self.uno += 1  
                self.round[8]=2
        else:
            pass
        #('c:/Users/Ettore/OneDrive/Documenti/sound.wav')
        self.game[8]=1
        self.check() 

class menu():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x190")
        self.root.title("Select GameMode")
        #
        self.But = tk.Button(self.root,text="1vs1!",fg = "RED",bg = "WHITE",font="Calibri 16",command = self.triss,height = 3, width=18)
        self.But.grid()
        self.But1 = tk.Button(self.root,text="LAN!",fg = "Blue",bg = "White",font="Calibri 16",command = self.online,height = 3, width=18)
        self.But1.grid()
        self.root.mainloop()
    def triss(self):
        self.root.destroy()
        triss()
    def online(self):
        self.root.destroy()
        #t = threading.Thread(target=online)
        #t.start()
        online()

menu()
#triss1()