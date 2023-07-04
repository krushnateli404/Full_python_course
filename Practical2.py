class Maths:
    def Getinput(self):
     self.n1 = int(input("Enter First number"))
     self.n2 = int(input("Enter Second number"))
class Division(Maths):
    def Div(self):
        try:
            self.div=self.n1/self.n2
        except Exception:
            print("Division by xero", Exception)
        exit()

class Result(Division):
    def Output(self):
        print("Division of %s" % self.n1,"and %s is "%self.n2,self.div)
    Obj=Result()
    Obj.Getinput()
    Obj.Div()
    Obj.Output()
