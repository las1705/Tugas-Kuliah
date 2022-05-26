from abc import  ABC, abstractmethod

class datauser(ABC):
    def __init__(self, nameac, passwordac):
        self.__nameac = nameac
        self.__passwordac = passwordac
        self.__dataac = [
            ["las","123","Classic"],
            ["sal","321","Premium"]
            ]
        self.dsa = None

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
            print ("> Status account : "+dt[2])
        else:
            print(">> Failed Login << ")
            print("< Check again your username and password >")

    def checkst(self):
        dt = self.checkac()
        status = dt[2]
        return status

    @abstractmethod
    def profile(self):
        pass
    
    @abstractmethod
    def material(self):
        pass
    

class classic(datauser):
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
        print("A[Basic]. Front End Language\n 1. HTML -> \n 2. CSS -> \n 3. JavaScript ->")
        print("B[Basic]. Back End Language\n 1. Dasar PHP -> \n 2. C++ -> \n 3. Python -> \n 4. Java ->")
        print("C. Other\n Git/Github ->")
        print("--- {About Classic status} \n ~ There's time limit every you take sub-material to finish the that sub-material ")
        print(">< Can't access next material in Front End Language \n>< Cant access OOP material in Back End Language \n>< Can't access API material")
        print("~~~~~~~~~~~ [--------] ~~~~~~~~~~~")
    
class premium(datauser):  
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
        print("A.[Basic] Front End Language\n 1. HTML -> \n 2. CSS -> \n 3. JavaScript ->")
        print("A.[Next]  Front End Language\n 1. HTMl -> \n 2. CSS -> \n 3. JavaScript ->")
        print("B.[Basic] Back End Language\n 1. PHP -> \n 2. C++ -> \n 3. Python -> \n 4. Java ->")
        print("B.[OOP]   Back End Language\n 1. PHP -> \n 2. C++ -> \n 3. Python -> \n 4. Java ->")
        print("C. Other\n 1. Git/Github -> \n 2. API -> ")
        print("--- {About Premium status} \n ~ There's no limit every you take sub-material to finish the that sub-material ")
        print("<> Next material in Front End Language is avaible \n<> OOP material in Back End Language is avaible \n<> API material is avaible")
        print("~~~~~~~~~~~ [--------] ~~~~~~~~~~~")
    
