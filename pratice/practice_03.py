# Date:17/08/2021
class Train:
    def __init__(self,name,fare,time,seat):
        self.name=name
        self.fare=fare
        self.time=time
        self.seat=seat
    def getinfo(self):
        print(f"The {self.name} train comes at {self.time} and the fare of this train is {self.fare}\nnow the train has {self.seat} seats")
    def ticketbook(self):
        
        if self.seat>0:
            print(f"Your ticket is sucessfully booked \n your seat no. is {self.seat}")
            self.seat=self.seat-1
            print(f" and now seats available is {self.seat}")
        else:
            print("You cant book your seat as seats are fulled")
    def ticketcancelled(self):
        if self.seat<5:
            self.seat=self.seat+1
            print(f"Your ticket is sucessfully cancelled and now the seat available is {self.seat}")
rail=Train("Rajdhane Express", 500, "4:00 pm",5)
rail.getinfo()
rail.ticketbook()
rail.ticketcancelled()
rail.ticketcancelled()