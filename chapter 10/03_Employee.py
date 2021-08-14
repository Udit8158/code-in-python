# Date:14/08/2021
class Employee:
    compamy="Google"
    slary="40LPA"
    location="India"   #This all are class atributes

Udit=Employee()        #Here Udit and Harry are two objects
Harry=Employee()
print(Udit.compamy)
print(Harry.compamy)

# Changing class atributes

Harry.compamy="Microsoft"   
print(Harry.compamy)
Udit.slary="50LPA"
print(Udit.slary)

Udit.Adress="west bengal"  #This is actually creating a instance atributes
print(Udit.Adress)