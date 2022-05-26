from sys import flags
import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import threading
from turtle import left
from tafc import cquestion



class tkinterApp(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		
		container = tk.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)
		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		for F in (HomePage, PlayPage):
			frame = F(container, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky ="nsew")

		self.show_frame(HomePage)
  
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        bgfrm = tk.Frame(self, width=1000, height=600,bg="black",)
        bgfrm.place(x=0,y=0)
        
        label = tk.Label(self, justify= CENTER, font=("Berlin Sans FB",17), fg="white", bg ="black",
                         text ="TRAIN YOUR BRAIN\nWITH BASIC MATH GAME")   
        label.place(anchor = CENTER, x = 500, y = 80)
        
        def clickb2():
            global listLB
            pnj = len(listLB) - 1
            for i in range(pnj):
                for j in range(pnj):
                    if listLB[j][1] < listLB[j+1][1]:
                        templs = listLB[j]
                        listLB[j] = listLB[j+1]
                        listLB[j+1] = templs 
            frm1 = tk.Frame(self, width = 350, height = 590, bg = "black",)
            frm1.place(x=5,y=5)
            llb = tk.Label(frm1, font=("Berlin Sans FB",15,"bold"), fg="#f5dd9d", bg="black",
                           text = "SCORE LEADERBOARD")
            llb.place(x=175,y=30,anchor=CENTER)
            
            for i in range(pnj+1):
                lpname = listLB[i][0]
                lpscore = listLB[i][1]
                lpcorrect = listLB[i][2]
                lpwrong = listLB[i][3]
                lpspeed = listLB[i][4]
                lptques = lpcorrect+lpwrong
                
                try:   
                    lpacc = 100*(lpcorrect/lptques)
                except ValueError :
                    lpacc = 0
                except ZeroDivisionError :
                    lpacc = 0
                fboard = tk.Frame(frm1, width=330, height=60, bg="#290345")
                fboard.place(anchor=NW,x=10,y=((i+1)*70)-15)
                lbname = tk.Label(fboard,font=("Berlin Sans FB",12),text=f"{i+1}. {lpname}",fg="#f5dd9d",bg="#290345")
                lbname.place(anchor=NW,x=3,y=2)
                lbscore = tk.Label(fboard,font=("Berlin Sans FB",14,"bold"),text=f"{lpscore}",fg="#f5dd9d",bg="#290345" )
                lbscore.place(anchor=NW,x=10,y=30)
                lbavsp = tk.Label(fboard,font=("Berlin Sans FB",10),text=f"speed: {lpspeed:.2f} s",fg="#f5dd9d",bg="#290345" )
                lbavsp.place(anchor=NW,x=90,y=2)
                lbsq = tk.Label(fboard,font=("Berlin Sans FB",10),text=f"total question: {lptques}",fg="#f5dd9d",bg="#290345" )
                lbsq.place(anchor=NW,x=215,y=2)
                lbacc = tk.Label(fboard,font=("Berlin Sans FB",10),text=f"accuracy: {lpacc:.2f}%",fg="#f5dd9d",bg="#290345" )
                lbacc.place(anchor=NW,x=90,y=30)
                lbcrt = tk.Label(fboard,font=("Berlin Sans FB",8),text=f"correct: {lpcorrect}",fg="#f5dd9d",bg="#290345" )
                lbcrt.place(anchor=NW,x=210,y=30)
                lbwrg = tk.Label(fboard,font=("Berlin Sans FB",8),text=f"wrong: {lpwrong}",fg="#f5dd9d",bg="#290345")
                lbwrg.place(anchor=NW,x=270,y=30)
                
            def desfrmr1():
                for widget in frm1.winfo_children():
                    widget.destroy()
                frm1.destroy()
            xbt = tk.Button(frm1, text = " X ", bg = "red", font=("Berlin Sans FB",11,""), relief=FLAT, fg="white",
                            command=desfrmr1)    
            xbt.place(anchor=NE,x=350,y=0)       
            
        def clickb3():
            frm2 = tk.Frame(self, width = 350, height = 590, bg = "black")
            frm2.place(x=645,y=5)
            lhp = tk.Label(frm2, text = "HOW TO PLAY", font=("Berlin Sans FB",17,"bold"),bg="black",fg="#f5dd9d")
            lhp.place(x=175,y=120,anchor=CENTER)
            lhtp = tk.Label(frm2,  font=("",12,"bold"), justify=LEFT, bg="#08024d", fg="#f5dd9d", pady=15, padx= 5,
                            text = "1. Clik button [PLAY]\n\n2. Click buttom [Start Game]\n\n3. Insert your answer beside the question\n\n    then press enter to the next question\n\n4. You have time limit solve the question\n\n5. If time is up, your score will appear above\n\n6. Insert your name then click [OK]",)
            lhtp.place(x=175,y=300,anchor=CENTER)
            xbt = tk.Button(frm2, text = " X ", bg = "red", font=("Berlin Sans FB",11,""), relief=FLAT, fg="white",
                            command=frm2.destroy)
            xbt.place(anchor=NW,x=0,y=0)
            
         
        def clkb1():
            frm3 = tk.Frame(self, width = 200, height = 180, bg = "#fc4103",)
            frm3.place(x=500,y=461,anchor=CENTER)
            lbpt = tk.Label(frm3, text = "PROFILE",font = ("Berlin Sans FB",14,""),justify=CENTER,widt=24,
                            fg = "#f5dd9d",bg="#cc0202")
            lbpt.place(anchor=N,x=100,y=0)
            lbdev = tk.Label(frm3, text = "By:\nLas1705",font = ("Berlin Sans FB",11,""),justify=CENTER
                             ,fg = "#f5dd9d",bg="#fc4103")
            lbdev.place(anchor=N,x=100,y=30)
            lbacd = tk.Label(frm3, text = "Academic:\nUNDIP, FAKULTAS TEKNIK,\nTEKNIK KOMPUTER (2021)",font = ("Berlin Sans FB",11,""),justify=CENTER
                             ,fg = "#f5dd9d",bg="#fc4103")
            lbacd.place(anchor=N,x=100,y=70)
            lbdt = tk.Label(frm3, text = "Date:\n24/05/2022",font = ("Berlin Sans FB",11,""),justify=CENTER
                            ,fg = "#f5dd9d",bg="#fc4103")
            lbdt.place(anchor=N,x=100,y=126)
            lcls = tk.Label(frm3, bg="#cc0202", width=30)
            lcls.place(anchor=S,x=100,y=190)
            lbpt.bind('<Button-1>', lambda event: frm3.destroy() )
            lcls.bind('<Button-1>', lambda event: frm3.destroy() )
                
                
        button1 = tk.Button(self, text ="PLAY",font = ("Berlin Sans FB",30,""), padx=50, pady=0, bg="#80ffff", fg ="#08024d", relief=FLAT,
                            command = lambda : controller.show_frame(PlayPage))
        button1.place(anchor=CENTER,x=500,y=250)

        button2 = tk.Button(self, font = ("Berlin Sans FB",15), fg="#80ffff", bg ="#08024d", relief=FLAT,
                            text ="Leaderboard\nScore", justify=CENTER,
                            command = lambda : [ clickb2()])
        button2.place(anchor=W,x=100,y=250)        
                
        button3 = tk.Button(self,font = ("Berlin Sans FB",15), fg="#80ffff", bg ="#08024d", relief=FLAT,
                            text ="How To\nPlay", justify=CENTER,
                            command =  lambda : clickb3())
        button3.place(anchor=E,x=900,y=250)
        
        lby = tk.Label(self, justify=CENTER,font=("Berlin Sans FB",11),
                       text="by las1705, 2022\nTEKKOM UNDIP (2021)")
        lby.place(anchor=CENTER,x=500,y=570)
        lby.bind('<Button-1>', lambda event: clkb1())
 
 
listAnswer = []
listCoreect = []       
listSpeed = []
sumCoreect = 0 
sumWrong = 0
sumScore = 0
sumQuestion = sumWrong + sumCoreect
listLB = [["Oxob30",4169,8,3,4.23],["Hyun",7054,10,2,6.54]]
        
class PlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        bgfrm1 = tk.Frame(self, width=1000, height=600,bg="black",)
        bgfrm1.place(x=0,y=0)

        ldb1 = tk.Label(self, justify= CENTER, bg="black", fg="#44fcf3", font=("Berlin Sans FB",12),
                         text =f"Click button [start game] to start game")   
        ldb1.place(anchor = CENTER, x = 150, y = 95)
        
        frmr = tk.Frame(self, width = 700, height = 590, bg = "#e4d5f2",)
        frmr.place(x=300,y=110)
        ttlf = tk.Label(self, text = "List Player Answer", font=("Berlin Sans FB",25,""), bg = "black",fg="#e4d5f2")
        ttlf.place(anchor=CENTER, x=650, y = 30)
        
        ffr = tk.Frame(self, width = 298, height = 330, bg = "#80ffff",)
        ffr.place(x=0,y=270)
        
        
        def toptabel(ppx):
            if ppx == 1:
                px = 0
            elif ppx == 2:
                px = 350
            bglbl1 = tk.Label(self, justify=CENTER, font=("Berlin Sans FB",13), height=2, width = 39,bg="#591166",)   
            bglbl1.place(anchor = W, x = 300+px, y = 88)
            lra1 = tk.Label(self, justify=CENTER, font=("Berlin Sans FB",13), height=2, bg="#591166", fg="white",
                             text ="Question")   
            lra1.place(anchor = CENTER, x = 350+px, y = 88)
            lra2 = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13), height=2,bg="#591166",fg="white",
                             text ="Player\nanswer")   
            lra2.place(anchor = CENTER, x = 420+px, y = 88)
            lra3 = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13), height=2,bg="#591166",fg="white",
                             text ="Correct\nanswer")   
            lra3.place(anchor = CENTER, x = 490+px, y = 88)
            lra4 = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13), height=2,bg="#591166",fg="white",
                             text ="Time")   
            lra4.place(anchor = CENTER, x = 560+px, y = 88)
            lra5 = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13), height=2,bg="#591166",fg="white",
                             text ="Score")   
            lra5.place(anchor = CENTER, x = 610+px, y = 88)
            
        toptabel(1)
        toptabel(2)
        
        def timelimit():
            time.sleep(60)
            
            global eans,sumCoreect,sumWrong,sumScore,sumQuestion,listSpeed
            eans.config(state="disabled")
            app.bind('<Return>', lambda event : ())
            ltes = tk.Label(ffr, font=("Berlin Sans FB",17), bg="#f51d3e", width = 27,
                            text = "Time is up")
            ltes.place(x=150,y= 0,anchor=N)
            tspeed = 0
            for i in listSpeed:
                tspeed += i
            try:   
                avspeed = tspeed/(sumCoreect+sumWrong)
            except ValueError :
                avspeed = 0
            except ZeroDivisionError :
                avspeed = 0
            
            lfr1 = tk.Label(ffr, text = "Final Score", font=("Berlin Sans FB",13),fg="black",bg = "#80ffff")
            lfr1.place(anchor=SE,x=90,y=70)
            lfr2 = tk.Label(ffr, text = "Total Quest", font=("Berlin Sans FB",13),fg="black",bg = "#80ffff")
            lfr2.place(anchor=SE,x=90,y=110)
            lfr3 = tk.Label(ffr, text = "Total Correct", font=("Berlin Sans FB",12),fg="black",bg = "#80ffff")
            lfr3.place(anchor=SE,x=255,y=65)
            lfr4 = tk.Label(ffr, text = "Total Wrong", font=("Berlin Sans FB",12),fg="black",bg = "#80ffff")
            lfr4.place(anchor=SE,x=255,y=105)
            lfr5 = tk.Label(ffr, text = "avarege Time", font=("Berlin Sans FB",12),fg="black",bg = "#80ffff")
            lfr5.place(anchor=SE,x=235,y=145)
            
            lvfr1 = tk.Label(ffr, text = sumScore, font=("Berlin Sans FB",16),fg="black",bg = "#80ffff")
            lvfr1.place(anchor=SW,x=90,y=70)
            lvfr2 = tk.Label(ffr, text = (sumCoreect+sumWrong), font=("Berlin Sans FB",16),fg="black",bg = "#80ffff")
            lvfr2.place(anchor=SW,x=90,y=110)
            lvfr3 = tk.Label(ffr, text = sumCoreect, font=("Berlin Sans FB",13),fg="black",bg = "#80ffff")
            lvfr3.place(anchor=SW,x=255,y=65)
            lvfr4 = tk.Label(ffr, text = sumWrong, font=("Berlin Sans FB",13),fg="black",bg = "#80ffff")
            lvfr4.place(anchor=SW,x=255,y=105)
            lvfr5 = tk.Label(ffr, text = f"{avspeed:.2f} s", font=("Berlin Sans FB",13),fg="black",bg = "#80ffff")
            lvfr5.place(anchor=SW,x=235,y=145)
        
            strname = StringVar(self)
            ename = tk.Entry(ffr, font=("Berlin Sans FB",17), width=8, textvariable=strname,fg="#591166")
            ename.place(anchor=CENTER,x=150,y=225)
            btok = tk.Button(ffr, text = "OK ", font=("Berlin Sans FB",15), width =10, state = "disabled",bg="#591166",fg="white",
                             command= lambda : addLB(ename.get(),avspeed))
            btok.place(anchor=CENTER,x=150,y=270) 
            lname = tk.Label(ffr, text = "Input Your Name ", font=("Berlin Sans FB",12),fg="black",bg = "#80ffff")
            lname.place(anchor=CENTER,x=150,y=190)
            def cksch (*args):
                if len(strname.get()) > 7 and len(strname.get()) < 0:
                    btok.config(state="disabled")
                else:
                    btok.config(state="normal")
            
            strname.trace('w',cksch)
            
        def addLB(name,avsp):
            global sumScore,sumCoreect,sumWrong,listSpeed,listLB
            listLB.append([name,sumScore,sumCoreect,sumWrong,avsp])
            sumScore = 0
            sumCoreect = 0
            sumWrong = 0
            listSpeed = []
            btstart.config(state = "normal")
            btback.config(state = "normal")
            lqn.config(text = "")
            lsc.config(text = "000000")
            lsq.config(text = "00")
            for widget in ffr.winfo_children():
                widget.destroy()
            for widget in frmr.winfo_children():
                widget.destroy()      
        
        def clkStart():
            threading.Thread(target=timelimit).start()
            global sumCoreect,sumWrong,sumScore,sumQuestion
            inplay(sumScore,sumQuestion)
        
        
        def inplay(sc,sq):
            global sumCoreect,sumWrong,sumScore,sumQuestion,lq,lqn,eans
            btstart.config(state = 'disabled')
            btback.config(state = 'disabled')
            clsq = cquestion()
            lsc.config(text = sc)
            lsq.config(text = sq)
            
            spwnq = clsq.printQustion()
            
            lq = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",12),fg="white",bg="black",
                          text ="Solve This!!!")   
            lq.place(anchor = SE, x = 150, y = 220)
            lqn = tk.Label(self, justify= CENTER, bg = "#591166", fg="white", width = 9,
                           text= f" {spwnq} = ", font = ("Berlin Sans FB",16,))   
            lqn.place(anchor = E, x = 150, y = 240)

            tstart = time.time()
            eans = tk.Entry(self, justify=CENTER, bg = "#e4d5f2", state = "normal", 
                            width=4, relief=SUNKEN,font = ("Berlin Sans FB",17))
            eans.place(anchor = W, x = 160, y = 240)
            
            correctAns = clsq.printResult()
            eans.focus()

            app.bind('<Return>', lambda event :indResult(eans.get(), correctAns, tstart, spwnq))
              
        
        def indResult(pans,cans,tb,ques ):
            global sumCoreect,sumWrong,sumScore,listAnswer,listCoreect
            listAnswer.append(pans)
            listCoreect.append(cans)
            tfinish = time.time()
            tans = tfinish-tb
            try:
                cvpans = int(pans)
            except ValueError:
                ancrtr = False
                sumWrong += 1
                pmscore = -1000
            else:
                if cvpans == cans:
                    ancrtr = True
                    sumCoreect += 1
                    if tans <= 10:
                        bscore = int((10-tans)*100)
                    else:
                        bscore = 0
                    pmscore = 1000 + bscore
                else:
                    ancrtr = False
                    pmscore = -1000
                    sumWrong += 1
            sumScore += pmscore
            sumQuestion = sumCoreect + sumWrong
            listSpeed.append(tans)
            showResult(sumQuestion,ques,pans,cans,tans,pmscore)
            inplay(sumScore,sumQuestion)
            
            
        def showResult(no,ques,pa,ca,sp,sc):
            global bglbl1,lra1,lra2,lra3,lra4,lra5
            if sc >0:
                bgcolor = "#11f568"
            elif sc <0:
                bgcolor = "red" 
            if no <= 19:
                px = 0
            elif no > 19:
                no = no - 19
                px = 350
            
            bglbl1 = tk.Label(frmr, justify=CENTER, font=("Berlin Sans FB",11), width = 41,bg = bgcolor)   
            bglbl1.place(anchor = W, x = 5+px, y = 15+((no-1)*25))
            lra1 = tk.Label(frmr, justify=CENTER, font=("Berlin Sans FB",11),
                            text =ques, bg = bgcolor)   
            lra1.place(anchor = CENTER, x = 50+px, y = 15+((no-1)*25))
            lra2 = tk.Label(frmr, justify= CENTER, font = ("Berlin Sans FB",11),
                            text =pa, bg = bgcolor)
            lra2.place(anchor = CENTER, x = 120+px, y = 15+((no-1)*25))
            lra3 = tk.Label(frmr, justify= CENTER, font = ("Berlin Sans FB",11),
                            text =ca, bg = bgcolor)   
            lra3.place(anchor = CENTER, x = 190+px, y = 15+((no-1)*25))
            lra4 = tk.Label(frmr, justify= CENTER, font = ("Berlin Sans FB",11),
                             text =f"{sp:.3f}", bg = bgcolor)   
            lra4.place(anchor = CENTER, x = 260+px, y = 15+((no-1)*25))
            lra5 = tk.Label(frmr, justify= CENTER, font = ("Berlin Sans FB",11),
                             text =sc, bg = bgcolor)   
            lra5.place(anchor = CENTER, x = 310+px, y = 15+((no-1)*25))
                          
        btstart = tk.Button(self,  relief=FLAT, fg="#80ffff", bg ="#08024d",
                            text ="Start Game",font = ("Berlin Sans FB",15,"bold"), padx=15, pady=5, command = clkStart)
        btstart.place(anchor=CENTER,x=150,y=60)
        
        ltm = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",14),fg="white",bg="black",
                         text ="Timer")   
        ltm.place(anchor = SE, x = 60, y = 145)
        ltimer = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",14),fg="white",bg="black",
                         text ="30 second")   
        ltimer.place(anchor = SE, x = 142, y = 145)
        
        lscore = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13),fg="white",bg="black",
                         text ="Score")   
        lscore.place(anchor = SE, x = 210, y = 165)
        lsc = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",16),fg="white",bg="black",
                         text ="000000")   
        lsc.place(anchor = SW, x = 210, y = 165)
        
        lsque = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",13),fg="white",bg="black",
                         text ="Total Qustion")   
        lsque.place(anchor = SE, x = 250, y = 200)
        lsq = tk.Label(self, justify= CENTER, font = ("Berlin Sans FB",16),fg="white",bg="black",
                         text ="00")   
        lsq.place(anchor = SW, x = 250, y = 200)
        
        btback = tk.Button(self, text ="back",font = ("Berlin Sans FB",11,""), padx=2,bg="#591166",fg="white",relief=FLAT,
                           command = lambda : controller.show_frame(HomePage))
        btback.place(anchor=NW,x=2,y=2)
    


# Driver Code
app = tkinterApp()
app.geometry("1000x600")
app.resizable(width=0,height=0)
app.mainloop()
