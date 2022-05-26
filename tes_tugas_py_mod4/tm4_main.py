

pilA =["dfd","fdfb","sd","rg","frfe"]
pilB = ["gre","ngf"]
pilC = ["ferfg","rsfd"]

        
def imenu1(md, inama):
    if md == 1:
        pilA.insert(len(pilA), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 2:
        pilB.insert(len(pilB), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam data survey")
    elif md == 3:
        pilC.insert(len(pilC), inama)
        return print(" <<berhasil menambahkan peserta <"+inama+"> ke dalam survey")
    else:
        return print(" <<Pilihan ini tidak tersedia")

def imenu2(n):
    print(" >Memilih pro Rusia ("+str(len(pilA))+" pendukung)")
    for n in range (len(pilA)):
        print("  "+str(n+1), pilA[n])
    print(" >Memilih pro Ukraina ("+str(len(pilB))+" pendukung)")
    for n in range (len(pilB)):
        print(f"  "+str(n+1), pilB[n])
    print(" >Netral ("+str(len(pilC))+" pendukung)")
    for n in range (len(pilC)):
        print("  "+str(n+1), pilC[n])
    

def imenu3():
    t = len(pilA) + len(pilB) + len(pilC)
    pa = 100 * len(pilA) / t 
    pb = 100 * len(pilB) / t 
    pc = 100 * len(pilC) / t 
    ipa = int(pa)
    ipb = int(pb)
    ipc = int(pc)
    return print("   Terdata perserta survey adalah "+str(t)+" orang\n   1. Pendukung Rusia "+str(ipa)+"%\n   2. pendukung Ukraina "+str(ipb)+"%\n   3. Netral "+str(ipc)+"%")
    

from tm4_c2 import *

while True:
    lp = 0
    print("\n\n=========Survey=========")
    mkr = mthd("DIDID BAYU FARIZQI","LUTHFI ANIS SYAFAR","ADDELLIA DEVIANTI","RIZAL AGATHA ERDIN AGESYAH")
    print("Survey by: Shift 1, Kelompok 3: \n<> "+mkr.n1+"\n<> "+mkr.n2+"\n<> "+mkr.n3+"\n<> "+mkr.n4)
    print(">menu:")
    print("a. menambah data survey\nb. menampilkan data\nc. melihat persentase")
    imenu = input(">pilih huruf angka dari pilihan menu: ")
    print("")

    if imenu == 'a':
        print("--Menambah Data Survey--")
        inama = input(" masukkan nama anda: ")
        print(" pilihan untuk didukung:")
        print(" 1. dukung Rusia\n 2. dukung Ukaraina\n 3. Netral")
        md = int(input(" pilih kelompok yang akan anda dukkung: "))
        imenu1(md, inama)
    elif imenu == 'b':
        print("--List Data Survey--")
        imenu2(0)
        
    elif imenu == 'c':
        print("--Persentase Data Survey--")
        imenu3()
        
    else:
        print("--pilihan tidak ada dalam menu--")

    if imenu == 'a' or imenu == 'A' or imenu == 'b' or imenu == 'B' or imenu == 'c' or imenu == 'C':
        lp += 1
    
    print("")
    mkr.selesai(lp)
 





