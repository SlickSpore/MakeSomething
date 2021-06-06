import tkinter as tk
#from # import #
from tkinter import Label, Message, filedialog
import sys
import socket
import threading
from time import sleep
from tkinter.constants import TRUE
font = "Calibri "
connectionh = None
message = None  
starter = True
name = "Tris! Host"
sended = [None,0,0,0,0,0,0,0,0,0]
used = [None,0,0,0,0,0,0,0,0,0]
rounds = [0,0,0,0,0,0,0,0,0]
gameplayer= 0
indexuse = 1
wait = False
class triss1():
    
    def recve(self):
        global message
        global used
        global wait
        a = connectionh.recv(1024)
        message = a
        print(message)
        if message != None:
            wait = False
        if gameplayer == 0:
            if message==b'1':
                if used[1]==0:
                    self.but1.config(text="X")
                    used[1]=1
                else:
                    pass

        if gameplayer == 1:
            if message==b'1':
                if used[1]==0:
                    self.but1.config(text="O")
                    used[1]=1
                else:
                    pass
        sys.exit()
        
    def __init__(self):
        global starter
        global name
        
        #index = 2
        self.start = False
        self.uno = 0
        self.game = [0,0,0,0,0,0,0,0,0]
        #
        self.root = tk.Tk()
        self.root.geometry("240x350")
        self.root.title(name)
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
 
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
        self.res = tk.Button(self.root,text="RESTART",height = 5, width = 10,command = self.reset)
        self.res.grid(column=1,row=4) 
        self.player = tk.Button(self.root,text="PLAYER",height = 5, width = 10,command = self.player)
        self.player.grid(column=3,row=4) 
        self.player1 = tk.Label(self.root,text="X",height = 5, width = 10)
        self.player1.grid(column=2,row=4) 
        if starter == False:
            global message
            global wait
            x = threading.Thread(target=self.recve)
            x.start()
            wait = True
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

        round[0]=0
        round[1]=0
        round[2]=0
        round[3]=0
        round[4]=0
        round[5]=0
        round[6]=0
        round[7]=0
        round[8]=0


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
        
        
        if round[2]==1 and round[5]==1 and round[8]==1:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[0]==1 and round[3]==1 and round[6]==1:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if round[1]==1 and round[4]==1 and round[7]==1:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if round[0]==1 and round[1]==1 and round[2]==1:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if round[3]==1 and round[4]==1 and round[5]==1:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if round[6]==1 and round[7]==1 and round[8]==1:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if round[0]==1 and round[4]==1 and round[8]==1:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[2]==1 and round[4]==1 and round[6]==1:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 

        if round[2]==2 and round[5]==2 and round[8]==2:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[0]==2 and round[3]==2 and round[6]==2:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if round[1]==2 and round[4]==2 and round[7]==2:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if round[0]==2 and round[1]==2 and round[2]==2:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if round[3]==2 and round[4]==2 and round[5]==2:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if round[6]==2 and round[7]==2 and round[8]==2:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if round[0]==2 and round[4]==2 and round[8]==2:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[2]==2 and round[4]==2 and round[6]==2:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 
    def uno1(self):
        
        global message
        global sended
        global indexuse
        if sended[1] ==0:
        
        
            #print(connectionh)
            if wait == False:

                connectionh.send(b'1')
            x = threading.Thread(target=self.recve)
            x.start()
            sended[1]=1
            indexuse = 1
            if wait == False:
                

                if used[1] !=1:
                    if gameplayer == 0:
                        self.but1.config(text="O")
                    if gameplayer == 1:
                        self.but1.config(text="X")
                else:
                    pass
        else:
            pass
        #a = self.recve()
       # print(message)
    def uno2(self):
        global message
        global sended
        global indexuse
        if sended[1] ==0:
        
        
            #print(connectionh)
            if wait == False:

                connectionh.send(b'1')
            x = threading.Thread(target=self.recve)
            x.start()
            sended[1]=1
            indexuse = 1
            if wait == False:
                

                if used[1] !=1:
                    if gameplayer == 0:
                        self.but1.config(text="O")
                    if gameplayer == 1:
                        self.but1.config(text="X")
                else:
                    pass
        else:
            pass        
    def uno3(self):
        pass
    def uno4(self):
        pass
    def uno5(self):
        pass
    def uno6(self):
        pass
    def uno7(self):
        pass
    def uno8(self):
        pass 
    def uno9(self):
        pass
class start():
    def __init__(self):
        #240x350
        x = threading.Thread(target=self.lconnect)#, args=triss1())
        x.start()
        a = socket.gethostname()
        self.b = socket.gethostbyname(a)
        self.root1 = tk.Tk()
        self.root1.geometry("200x150")
        self.root1.title("Starting")
        
        self.root1.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
        self.label= tk.Label(text=self.b,font=font)
        self.label.grid()




        self.root1.mainloop()
    def lconnect(self):
        global connectionh
        global gameplayer
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a = socket.gethostname()
        b = socket.gethostbyname(a)
        
        
        s.bind((b,1234))
        s.listen(1)

        conn, addr = s.accept()
        connectionh = conn
        #self.root1.destroy()
        #conn.setblocking(0)

        a = conn.recv(1024)
        
        if a == b'Hello':
            print("Hosting")
            connectionh.send(b'Hello')
            gameplayer = 1
            #self.label1=tk.Label(text=addr)
            #self.label1.grid()
            #self.labe1=tk.Button(text="QUIT",command=self.quit)
            #self.labe1.grid()
            triss1()
            #print("something")
            #sys.exit()


class connect():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x190")
        self.root.title("Select GameMode")
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
        self.label = tk.Label(text="Specify The Host")
        self.label.grid()
        self.But = tk.Entry()
        self.But.grid()
        self.But1 = tk.Button(text="CONNECT",command=self.startc,height = 3, width=18)
        self.But1.grid()
        self.root.mainloop()
    def startc(self):
        x = threading.Thread(target=self.connection)
        x.start()
    def connection(self):
        global connectionh
        global starter
        global name
        global gameplayer
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
                
                name = "Tris! Client"
                x = threading.Thread(target=triss1)
                x.start()

                    
                
                
        except Exception as e:
            print(e)
            self.label.config(text="Host Is Down")
            #x.start()

class bind():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x190")
        self.root.title("Select GameMode")
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')

        self.But1 = tk.Button(text="START",command=self.strat,font=font,height = 8, width=20,fg="GREEN")
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
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
        self.But = tk.Button(text="CONNECT",fg = "Red",bg="WHite",font="Calibri 16",command = self.con,height = 3, width=18)
        self.But.grid()
        self.But1 = tk.Button(text="BIND",fg = "Blue",bg="WHite",font="Calibri 16",command = self.bind,height = 3, width=18)
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
        round = [0,0,0,0,0,0,0,0,0]
        self.root = tk.Tk()
        self.root.geometry("240x350")
        self.root.title("Tris")
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
 
        self.but1 = tk.Button(text="",height = 5, width = 10,command = self.uno1,bg = "White")
        self.but1.grid(column=1,row=1)
        self.but2 = tk.Button(text="",height = 5, width = 10,command = self.uno2,bg = "White")
        self.but2.grid(column=2,row=1)
        self.but3 = tk.Button(text="",height = 5, width = 10,command = self.uno3,bg = "White")
        self.but3.grid(column=3,row=1)
        self.but4 = tk.Button(text="",height = 5, width = 10,command = self.uno4,bg = "White")
        self.but4.grid(column=1,row=2)        
        self.but5 = tk.Button(text="",height = 5, width = 10,command = self.uno5,bg = "White")
        self.but5.grid(column=2,row=2)            
        self.but6 = tk.Button(text="",height = 5, width = 10,command = self.uno6,bg = "White")
        self.but6.grid(column=3,row=2)            
        self.but7 = tk.Button(text="",height = 5, width = 10,command = self.uno7,bg = "White")
        self.but7.grid(column=1,row=3)        
        self.but8 = tk.Button(text="",height = 5, width = 10,command = self.uno8,bg = "White")
        self.but8.grid(column=2,row=3)            
        self.but9 = tk.Button(text="",height = 5, width = 10,command = self.uno9,bg = "White")
        self.but9.grid(column=3,row=3)  
        self.res = tk.Button(text="RESTART",fg = "red",height = 5, width = 10,command = self.reset)
        self.res.grid(column=1,row=4) 
        self.player = tk.Button(text="PLAYER",fg = "Green",height = 5, width = 10,command = self.player)
        self.player.grid(column=3,row=4) 
        self.player1 = tk.Label(text="X",height = 5, width = 10)
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

        round[0]=0
        round[1]=0
        round[2]=0
        round[3]=0
        round[4]=0
        round[5]=0
        round[6]=0
        round[7]=0
        round[8]=0


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
        
        
        if round[2]==1 and round[5]==1 and round[8]==1:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[0]==1 and round[3]==1 and round[6]==1:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if round[1]==1 and round[4]==1 and round[7]==1:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if round[0]==1 and round[1]==1 and round[2]==1:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if round[3]==1 and round[4]==1 and round[5]==1:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if round[6]==1 and round[7]==1 and round[8]==1:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if round[0]==1 and round[4]==1 and round[8]==1:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[2]==1 and round[4]==1 and round[6]==1:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 

        if round[2]==2 and round[5]==2 and round[8]==2:
            self.but3.config(bg = "light green")
            self.but6.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[0]==2 and round[3]==2 and round[6]==2:
            self.but4.config(bg = "light green")
            self.but7.config(bg = "light green")
            self.but1.config(bg = "light green")  
        if round[1]==2 and round[4]==2 and round[7]==2:
            self.but2.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but8.config(bg = "light green") 

        if round[0]==2 and round[1]==2 and round[2]==2:
            self.but1.config(bg = "light green")
            self.but2.config(bg = "light green")
            self.but3.config(bg = "light green")  
        if round[3]==2 and round[4]==2 and round[5]==2:
            self.but4.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but6.config(bg = "light green")  
        if round[6]==2 and round[7]==2 and round[8]==2:
            self.but7.config(bg = "light green")
            self.but8.config(bg = "light green")
            self.but9.config(bg = "light green") 

        if round[0]==2 and round[4]==2 and round[8]==2:
            self.but1.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but9.config(bg = "light green")  
        if round[2]==2 and round[4]==2 and round[6]==2:
            self.but3.config(bg = "light green")
            self.but5.config(bg = "light green")
            self.but7.config(bg = "light green") 
    def uno1(self):
        self.start = True
        if self.game[0]==0:

            if (self.uno % 2) == 0:
                self.but1.config(text="X")
                self.uno += 1
                round[0]=1
            else:
                self.but1.config(text="O")
                self.uno += 1  
                round[0]=2   
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
                round[1]=1
            else:
                self.but2.config(text="O")
                self.uno += 1 
                round[1]=2
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
                round[2]=1
            else:
                self.but3.config(text="O")
                self.uno += 1  
                round[2]=2
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
                round[3]=1
            else:
                self.but4.config(text="O")
                self.uno += 1  
                round[3]=2
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
                round[4]=1
            else:
                self.but5.config(text="O")
                self.uno += 1  
                round[4]=2
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
                round[5]=1
            else:
                self.but6.config(text="O")
                self.uno += 1  
                round[5]=2
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
                round[6]=1
            else:
                self.but7.config(text="O")
                self.uno += 1  
                round[6]=2
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
                round[7]=1
            else:
                self.but8.config(text="O")
                self.uno += 1  
                round[7]=2
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
                round[8]=1
            else:
                self.but9.config(text="O")
                self.uno += 1  
                round[8]=2
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
        self.root.iconbitmap('C:\\Users\\Ettore\\OneDrive\\Documenti\\tris.ico')
        self.But = tk.Button(text="1vs1!",fg = "RED",bg = "WHITE",font="Calibri 16",command = self.triss,height = 3, width=18)
        self.But.grid()
        self.But1 = tk.Button(text="LAN!",fg = "Blue",bg = "White",font="Calibri 16",command = self.online,height = 3, width=18)
        self.But1.grid()
        self.root.mainloop()
    def triss(self):
        self.root.destroy()
        triss()
    def online(self):
        self.root.destroy()
        online()

menu()
#triss1()