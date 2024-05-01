class student:
    @staticmethod
    def start():
        print("car started")

class car(student):

s1 = student()
s2 = car()
print(s2.start)            