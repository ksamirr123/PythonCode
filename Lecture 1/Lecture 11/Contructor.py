#questions********
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks  = marks

    def _getavg(self):
        sum =0
        for val in self.marks:
            sum+=val
            print("hi",self.name,"your marks is:",sum/3)

    @staticmethod
    def hello():
        print("hello dunia")        



s1 = student("sameer khan",[98,97,91])
s1._getavg()    
s1.hello()    