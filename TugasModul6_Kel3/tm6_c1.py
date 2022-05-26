from abc import  ABC, abstractmethod

class course(ABC):
    def __init__(self, nameac, passwordac):
        self.__nameac = nameac
        self.__passwordac = passwordac
        self.__dataac = [[]]

    @abstractmethod
    def profile(self):
        pass
    
    @abstractmethod
    def material(self):
        pass
    

class datauser(course):
    def __init__(self, nameac, passwordac):
        super().__init__(nameac, passwordac)
        self.__nameac = nameac
        self.__passwordac = passwordac
        self.__dataac = [
            ["las03@dojo.com","123","Classic"],
            ["sal30@dojo.com","321","Premium"]
            ]

    def checkac(self):
        c = 0
        b = 0
        nac = self.__nameac
        pac = self.__passwordac
        d = self.__dataac
        for c in range (len(d)):
            if nac == d[c][0]:
                if pac == d[c][1]:
                    b = 1
                    status = d[c][2]
                    dt = [nac,pac,status]
        if b == 1:
            return dt
        else:
           return False

    def welcome(self):
        dt = self.checkac()
        if dt:
            print ("----- << WELCOME >> -----")
            print ("> Success Login as "+dt[0])
        else:
            print(">> Failed Login << ")
            print("< Check again your username and password >")

    def checkst(self):
        dt = self.checkac()
        status = dt[2]
        return status

    def profile(self):
        pass
    
    def material(self):
        pass


class classic(course):
    def __init__(self, nameac, passwordac, usname):
        super().__init__(nameac, passwordac)
        self.__email = nameac
        self.__username = usname
        self.__status = None

    @property
    def status(self):
        pass
    @status.getter
    def status(self):
        return self.__status
    @status.setter
    def status(self, stts):
        self.__status = stts

    def profile(self):
        print("\n~~~~~~~~~ [Profile] ~~~~~~~~~")
        print(" Email    : "+self.__email+"\n Username : "+self.__username+"\n Status   : "+self.__status)
        print("~~~~~~~~~ [-------] ~~~~~~~~~")

    def material(self):
        print("\n~~~~~~~~~~~ [Material] ~~~~~~~~~~~")
        print("A.[Basic] Front End Language\n 1. HTML -> https://youtube.com/playlist?list=PLFIM0718LjIVuONHysfOK0ZtiqUWvrx4F \n 2. CSS -> https://youtube.com/playlist?list=PLFIM0718LjIUBrbm6Gdh6k7ZUvPIAZm7p \n 3. JavaScript -> https://youtube.com/playlist?list=PLFIM0718LjIWXagluzROrA-iBY9eeUt4w")
        print("B.[Basic] Back End Language\n 1. PHP -> https://youtube.com/playlist?list=PLFIM0718LjIUqXfmEIBE3-uzERZPh3vp6 \n 2. C++ -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo4Ze0bbGB1WKBSNMPzi-eWI \n 3. Python https://www.youtube.com/playlist?list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1 -> \n 4. Java -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo51w0Hmqi0C8h2KWNzDfo6F")
        print("C. Other\n 1. Git/Github -> https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf \n")
        print("--- {About Classic status} \n ~ There's time limit every you take sub-material to finish the that sub-material ")
        print(">< Can't access next material in Front End Language \n>< Cant access OOP material in Back End Language \n>< Can't access API material")
        print("~~~~~~~~~~~ [--------] ~~~~~~~~~~~")
    
    
class premium(course):  
    def __init__(self, nameac, passwordac, usname):
        super().__init__(nameac, passwordac)
        self.__email = nameac
        self.__username = usname
        self.__status = None

    @property
    def status(self):
        pass
    @status.getter
    def status(self):
        return self.__status
    @status.setter
    def status(self, stts):
        self.__status = stts

    def profile(self):
        print("\n~~~~~~~~~ [Profile] ~~~~~~~~~")
        print(" Email    : "+self.__email+"\n Username : "+self.__username+"\n Status   : "+self.__status)
        print("~~~~~~~~~ [-------] ~~~~~~~~~")

    def material(self):
        print("\n~~~~~~~~~~~ [Material] ~~~~~~~~~~~")
        print("A.[Basic] Front End Language\n 1. HTML -> https://youtube.com/playlist?list=PLFIM0718LjIVuONHysfOK0ZtiqUWvrx4F \n 2. CSS -> https://youtube.com/playlist?list=PLFIM0718LjIUBrbm6Gdh6k7ZUvPIAZm7p \n 3. JavaScript -> https://youtube.com/playlist?list=PLFIM0718LjIWXagluzROrA-iBY9eeUt4w")
        print("A.[Next]  Front End Language\n 1. CSS(Layoutinh) -> https://youtube.com/playlist?list=PLFIM0718LjIUu4Ju9GUL5zpLcuq08TKYr \n 2. CSS(Grid) -> https://youtube.com/playlist?list=PLFIM0718LjIXmbwX0dEsoRVX-PC16vmuw \n 3. JavaScript(Next) ->https://youtube.com/playlist?list=PLFIM0718LjIUGpY8wmE41W7rTJo_3Y46-")
        print("B.[Basic] Back End Language\n 1. PHP -> https://youtube.com/playlist?list=PLFIM0718LjIUqXfmEIBE3-uzERZPh3vp6 \n 2. C++ -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo4Ze0bbGB1WKBSNMPzi-eWI \n 3. Python https://www.youtube.com/playlist?list=PLZS-MHyEIRo7cgStrKAMhgnOT66z2qKz1 -> \n 4. Java -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo51w0Hmqi0C8h2KWNzDfo6F")
        print("B.[OOP]   Back End Language\n 1. PHP -> https://youtube.com/playlist?list=PLFIM0718LjIWvxxll-6wLXrC_16h_Bl_p \n 2. C++ -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo7-RC_-hkL9gu0_ofABw862 \n 3. Python -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo7ab0-EveSvf4CLdyOECMm0 \n 4. Java -> https://www.youtube.com/playlist?list=PLZS-MHyEIRo6V4_vk1s1NcM2HoW5KFG7i")
        print("C. Other\n 1. Git/Github -> https://www.youtube.com/playlist?list=PLFIM0718LjIVknj6sgsSceMqlq242-jNf \n 2. API -> https://www.youtube.com/playlist?list=PLFIM0718LjIW7AsIbnhFg15t9yx4H-sQ0 \n")
        print("--- {About Premium status} \n ~ There's no limit every you take sub-material to finish the that sub-material ")
        print("<> Next material in Front End Language is avaible \n<> OOP material in Back End Language is avaible \n<> API material is avaible")
        print("~~~~~~~~~~~ [--------] ~~~~~~~~~~~")
    

       

   
    

            
