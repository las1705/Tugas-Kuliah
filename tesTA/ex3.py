import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import threading
from tatm import cquestion

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
        tk.Frame
        
        label = tk.Label(self, justify= CENTER, 
                         text ="TRAIN YOUR BRAIN\nWITH BASIC MATH")   
        label.place(anchor = CENTER, x = 500, y = 50)
        
        global listLB
        pnj = len(listLB) - 1
        for i in range(pnj):
            for j in range(pnj):
                if listLB[j][1] < listLB[j+1][1]:
                    templs = listLB[j]
                    listLB[j] = listLB[j+1]
                    listLB[j+1] = templs 
        
        def clickb2():
            global listLB
            pnj = len(listLB) - 1
            for i in range(pnj):
                for j in range(pnj):
                    if listLB[j][1] < listLB[j+1][1]:
                        templs = listLB[j]
                        listLB[j] = listLB[j+1]
                        listLB[j+1] = templs 
            frm1 = tk.Frame(self, width = 350, height = 590, bg = "white",)
            frm1.place(x=5,y=5)
            llb = tk.Label(frm1, font=("",15,"bold"),
                           text = "SCORE LEADER BOARD")
            llb.place(x=175,y=30,anchor=CENTER)
            
            for i in range(pnj+1):
                lpname = listLB[i][0]
                lpscore = listLB[i][1]
                lpcorrect = listLB[i][2]
                lpwrong = listLB[i][3]
                lpspeed = listLB[i][4]
                lptques = lpcorrect+lpwrong
                lpacc = 100*(lpcorrect/lptques)
                fboard = tk.Frame(frm1, width=330, height=60)
                fboard.place(anchor=NW,x=10,y=((i+1)*70)-15)
                lbname = tk.Label(fboard,font=("",12),text=f"{i+1}. {lpname}" )
                lbname.place(anchor=NW,x=3,y=2)
                lbscore = tk.Label(fboard,font=("",14),text=f"{lpscore}" )
                lbscore.place(anchor=NW,x=10,y=30)
                lbavsp = tk.Label(fboard,font=("",10),text=f"speed: {lpspeed:.2f} s" )
                lbavsp.place(anchor=NW,x=90,y=2)
                lbsq = tk.Label(fboard,font=("",10),text=f"total question: {lptques}" )
                lbsq.place(anchor=NW,x=215,y=2)
                lbacc = tk.Label(fboard,font=("",10),text=f"accuracy: {lpacc:.2f}%" )
                lbacc.place(anchor=NW,x=90,y=30)
                lbcrt = tk.Label(fboard,font=("",8),text=f"correct: {lpcorrect}" )
                lbcrt.place(anchor=NW,x=210,y=30)
                lbwrg = tk.Label(fboard,font=("",8),text=f"wrong: {lpwrong}" )
                lbwrg.place(anchor=NW,x=270,y=30)
                
            def desfrmr1():
                for widget in frm1.winfo_children():
                    widget.destroy()
                frm1.destroy()
            xbt = tk.Button(frm1, text = "<---", bg = "red",
                            command=desfrmr1)    
            xbt.place(anchor=NE,x=350,y=0)       
            
        def clickb3():
            frm2 = tk.Frame(self, width = 350, height = 590, bg = "white",)
            frm2.place(x=645,y=5)
            lhp = tk.Label(frm2, text = "tes")
            lhp.place(x=10,y=20)
            xbt = tk.Button(frm2, text = "x", bg = "red",
                            command=frm2.destroy)
            xbt.place(anchor=NE,x=350,y=0)
                
        button1 = tk.Button(self, text ="Play",font = ("",15), padx=15, pady=5, 
                            command = lambda : controller.show_frame(PlayPage))
        button1.place(anchor=CENTER,x=500,y=200)

        button2 = tk.Button(self, font = ("",10),
                            text ="Leaderboard\nScore", justify=CENTER,
                            command = lambda : [ clickb2()])
        button2.place(anchor=W,x=355,y=400)        
                
        button3 = tk.Button(self,
                            text ="How To\nPlay", justify=CENTER,
                            command =  lambda : clickb3())
        button3.place(anchor=E,x=645,y=400)
 
 
listAnswer = []
listCoreect = []       
listSpeed = []
sumCoreect = 0 
sumWrong = 0
sumScore = 0
sumQuestion = sumWrong + sumCoreect
listLB = [["Oxob",4169,8,3,4.23],["Hyun",7054,10,2,6.54]]
        
class PlayPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        ldb1 = tk.Label(self, justify= CENTER, 
                         text ="Click button to start game")   
        ldb1.place(anchor = CENTER, x = 150, y = 20)
        
        frmr = tk.Frame(self, width = 700, height = 590, bg = "white",)
        frmr.place(x=300,y=110)
        ttlf = tk.Label(self, text = "List Player Answer", font=("",17,"bold"), bg = "white")
        ttlf.place(anchor=CENTER, x=650, y = 30)
        
        ffr = tk.Frame(self, width = 298, height = 330, bg = "white",)
        ffr.place(x=0,y=270)
        
        
        def toptabel(ppx):
            if ppx == 1:
                px = 0
            elif ppx == 2:
                px = 345
            bglbl1 = tk.Label(self, justify=CENTER, font=("",13), height=2, width = 37,)   
            bglbl1.place(anchor = W, x = 305+px, y = 80)
            lra1 = tk.Label(self, justify=CENTER, font=("",13), height=2, 
                             text ="Question")   
            lra1.place(anchor = CENTER, x = 350+px, y = 80)
            lra2 = tk.Label(self, justify= CENTER, font = ("",13), height=2,
                             text ="Player\nanswer")   
            lra2.place(anchor = CENTER, x = 420+px, y = 80)
            lra3 = tk.Label(self, justify= CENTER, font = ("",13), height=2,
                             text ="Correct\nanswer")   
            lra3.place(anchor = CENTER, x = 490+px, y = 80)
            lra4 = tk.Label(self, justify= CENTER, font = ("",13), height=2,
                             text ="Time")   
            lra4.place(anchor = CENTER, x = 560+px, y = 80)
            lra5 = tk.Label(self, justify= CENTER, font = ("",13), height=2,
                             text ="Score")   
            lra5.place(anchor = CENTER, x = 610+px, y = 80)
            
        toptabel(1)
        toptabel(2)
        
        def timelimit():
            time.sleep(30)
            
            global eans,sumCoreect,sumWrong,sumScore,sumQuestion,listSpeed
            eans.config(state="disabled")
            app.bind('<Return>', lambda event : ())
            ltes = tk.Label(ffr, font=("",15), bg="orange", width = 26,
                            text = "Time is up")
            ltes.place(x=150,y= 20,anchor=CENTER)
            tspeed = 0
            for i in listSpeed:
                tspeed += i
            avspeed = tspeed/(sumCoreect+sumWrong)
            
            lfr1 = tk.Label(ffr, text = "Final Score", font=("",11))
            lfr1.place(anchor=SE,x=90,y=70)
            lfr2 = tk.Label(ffr, text = "Total Quest", font=("",11))
            lfr2.place(anchor=SE,x=90,y=110)
            lfr3 = tk.Label(ffr, text = "Total Correct", font=("",10))
            lfr3.place(anchor=SE,x=255,y=65)
            lfr4 = tk.Label(ffr, text = "Total Wrong", font=("",10))
            lfr4.place(anchor=SE,x=255,y=105)
            lfr5 = tk.Label(ffr, text = "avarege Time", font=("",10))
            lfr5.place(anchor=SE,x=255,y=145)
            
            lvfr1 = tk.Label(ffr, text = sumScore, font=("",14))
            lvfr1.place(anchor=SW,x=90,y=70)
            lvfr2 = tk.Label(ffr, text = (sumCoreect+sumWrong), font=("",14))
            lvfr2.place(anchor=SW,x=90,y=110)
            lvfr3 = tk.Label(ffr, text = sumCoreect, font=("",12))
            lvfr3.place(anchor=SW,x=260,y=65)
            lvfr4 = tk.Label(ffr, text = sumWrong, font=("",12))
            lvfr4.place(anchor=SW,x=260,y=105)
            lvfr5 = tk.Label(ffr, text = f"{avspeed:.2f}", font=("",12))
            lvfr5.place(anchor=SW,x=260,y=145)
             
            lname = tk.Label(ffr, text = "Input Your Name ", font=("",12))
            lname.place(anchor=CENTER,x=150,y=190)
            ename = tk.Entry(ffr, font=("",17), width=8)
            ename.place(anchor=CENTER,x=150,y=225)
            btok = tk.Button(ffr, text = "OK ", font=("",15), width =10,
                             command= lambda : addLB(ename.get(),avspeed))
            btok.place(anchor=CENTER,x=150,y=270)
            
        def addLB(name,avsp):
            global sumScore,sumCoreect,sumWrong,listSpeed,listLB
            listLB.append([name,sumScore,sumCoreect,sumWrong,avsp])
            sumScore = 0
            sumCoreect = 0
            sumWrong = 0
            listSpeed = []
            btstart.config(state = "normal")
            lqn.config(text = "")
            lsc.config(text = "000000")
            lsq.config(text = "00")
            for widget in ffr.winfo_children():
                widget.destroy()
            for widget in frmr.winfo_children():
                widget.destroy()    
            controller.show_frame(HomePage)         
        
        def clkStart():
            threading.Thread(target=timelimit).start()
            global sumCoreect,sumWrong,sumScore,sumQuestion
            inplay(sumScore,sumQuestion)
        
        
        def inplay(sc,sq):
            global sumCoreect,sumWrong,sumScore,sumQuestion,lq,lqn,eans
            btstart.config(state = 'disabled')
            clsq = cquestion()
            lsc.config(text = sc)
            lsq.config(text = sq)
            
            spwnq = clsq.printQustion()
            
            lq = tk.Label(self, justify= CENTER, font = ("",12),
                          text ="Solve This!!!")   
            lq.place(anchor = SE, x = 150, y = 220)
            lqn = tk.Label(self, justify= CENTER, bg = "gray", width = 9,
                           text= f" {spwnq} = ", font = ("",16,))   
            lqn.place(anchor = E, x = 150, y = 240)

            tstart = time.time()
            eans = tk.Entry(self, justify=CENTER, bg = "gray", state = "normal",
                            width=4, relief=SUNKEN,font = ("",17))
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
                bgcolor = "green"
            elif sc <0:
                bgcolor = "red" 
            if no <= 19:
                px = 0
            elif no > 19:
                no = no - 19
                px = 345
            
            bglbl1 = tk.Label(frmr, justify=CENTER, font=("",11), width = 37,bg = bgcolor)   
            bglbl1.place(anchor = W, x = 5+px, y = 15+((no-1)*25))
            lra1 = tk.Label(frmr, justify=CENTER, font=("",11),
                            text =ques, bg = bgcolor)   
            lra1.place(anchor = CENTER, x = 50+px, y = 15+((no-1)*25))
            lra2 = tk.Label(frmr, justify= CENTER, font = ("",11),
                            text =pa, bg = bgcolor)
            lra2.place(anchor = CENTER, x = 120+px, y = 15+((no-1)*25))
            lra3 = tk.Label(frmr, justify= CENTER, font = ("",11),
                            text =ca, bg = bgcolor)   
            lra3.place(anchor = CENTER, x = 190+px, y = 15+((no-1)*25))
            lra4 = tk.Label(frmr, justify= CENTER, font = ("",11),
                             text =f"{sp:.3f}", bg = bgcolor)   
            lra4.place(anchor = CENTER, x = 260+px, y = 15+((no-1)*25))
            lra5 = tk.Label(frmr, justify= CENTER, font = ("",11),
                             text =sc, bg = bgcolor)   
            lra5.place(anchor = CENTER, x = 310+px, y = 15+((no-1)*25))
                      
            
        btstart = tk.Button(self, text ="Start Game",font = ("",15,"bold"), padx=15, pady=5, command = clkStart)
        btstart.place(anchor=CENTER,x=150,y=60)
        
        
        ltm = tk.Label(self, justify= CENTER, font = ("",13),
                         text ="Timer")   
        ltm.place(anchor = SE, x = 60, y = 145)
        ltimer = tk.Label(self, justify= CENTER, font = ("",13),
                         text ="00:00")   
        ltimer.place(anchor = SE, x = 120, y = 145)
        
        lscore = tk.Label(self, justify= CENTER, font = ("",10),
                         text ="Score")   
        lscore.place(anchor = SE, x = 215, y = 165)
        lsc = tk.Label(self, justify= CENTER, font = ("",15),
                         text ="000000")   
        lsc.place(anchor = SW, x = 220, y = 165)
        
        lsque = tk.Label(self, justify= CENTER, font = ("",10),
                         text ="Total Qustion")   
        lsque.place(anchor = SE, x = 255, y = 200)
        lsq = tk.Label(self, justify= CENTER, font = ("",15),
                         text ="00")   
        lsq.place(anchor = SW, x = 260, y = 200)
    


# Driver Code
app = tkinterApp()
app.geometry("1000x600")
app.mainloop()
