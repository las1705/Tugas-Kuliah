import time
from tkinter import *
from tkinter import messagebox

ls = [[2,4],[5,3],[2,5]]
lss = []
nls = []

print(ls[0])
for a in range(len(ls)):
    print(ls[a][1])

pnj = len(ls) - 1
print(pnj)

for i in range(pnj):
    for j in range(pnj):
        if ls[j][1] > ls[j+1][1]:
            templs = ls[j]
            ls[j] = ls[j+1]
            ls[j+1] = templs 

ls.append([2,3])
            
print(ls)


#for i in range(len(ls)):
 #   lss.append(ls[i][1])
  #  for j in range(len(ls)):
   #     nls.append()
    
    



        