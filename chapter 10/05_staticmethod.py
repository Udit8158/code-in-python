# Date:15/08/2021
# staticmethod is actually used for get rid of self
class Students:
    division=12
    @ staticmethod
    def greet():
        print("Hellow,\n students")
udit=Students()
udit.greet()         #But for this we dont need of self


class Students:
    division=12
    
    def greet(self):
        print(f"Hellow,\n {self.student}")
udit=Students()
udit.student="Udit"    #Here actually this is the benifit of self
udit.greet()
