import random

class cquestion():
    def __init__(self):
        self.num1 = random.randint(10,99)
        self.oprt = random.randint(1,5)
        if self.oprt == 1:
            self.num2 = random.randint(10,99)
            rslt = int(self.num1 + self.num2)
            srto = "+"
        elif self.oprt == 2:
            self.num2 = random.randint(10,99)
            rslt = int(self.num1 - self.num2)
            srto = "-"
        elif self.oprt == 3:
            self.num2 = random.randint(1,10)
            rslt = int(self.num1 * self.num2)
            srto = "*"
        elif self.oprt == 4:
            self.num2 = random.randint(1,10)
            rslt = int(self.num1 / self.num2)
            srto = "/"
        elif self.oprt == 5:
            self.num2 = random.randint(1,10)
            rslt = int(self.num1 % self.num2)
            srto = "%"
        self.rque = rslt
        self.sopr = srto

    def printQustion(self):
        return f"{str(self.num1)} {self.sopr} {str(self.num2)} "
    
    def printResult(self):
        return self.rque


    





    
    
