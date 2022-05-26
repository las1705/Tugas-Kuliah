from tm6_c1 import *

bol = 1
while bol == 1:
    print("_____________________________________________\n")
    email = input("email    : ")
    password = input("password : ")
    lg = datauser(email, password)
    if lg.checkac():
        bol = 0
    else:
        lg.welcome()
        bol = 1
print("_____________________________________________\n")

lg.welcome()
usname = input("\n< Input your name : ")

while bol == 0:
    status = lg.checkst()
    if status == "Classic":
        lgc = classic(email, password,usname)
        lgc.status = "Classic"
        print("\n    [ Menu ]\n 1. Show Profile\n 2. Show Material\n 3. Logout")
        nmenu = int(input("<< Select number menu : "))
        if nmenu == 1:
            lgc.profile()
        elif nmenu == 2:
            lgc.material()
        elif nmenu == 3:
            bol = 1
        else:
            print("This option is doesn't exist in menu")
        
    elif status == "Premium":
        lgp = premium(email, password,usname)
        lgp.status = "Premium"
        print("\n  [ Menu ]\n  1. Show Profile\n  2. Show Material\n  3. Logout")
        nmenu = int(input("<< Select number menu: "))
        if nmenu == 1:
            lgp.profile()
        elif nmenu == 2:
            lgp.material()
        elif nmenu == 3:
            bol = 1
        else:
            print("This option is doesn't exist in menu")    

print("\n----- << LOGOUT >> -----")