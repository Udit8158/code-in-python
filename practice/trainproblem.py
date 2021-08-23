# Date:19\08\2021

class Train():
    def __init__(self,name,seat):
        self.name = name
        self.seat = seat

    def getinfo(self):
        print(f"The {self.name} has {self.seat} seats ")
    
    def ticketbook(self):
        if self.seat>0:
            print("Your ticket is successfully booked\nThank You for booking")
            self.seat-=1
        else:
            print("Sorry seats are full so you can't book your seat right now\nPlease try again later")
           
    def ticketcancell(self):
        print("Your ticket is succesfully cancelled") 
        self.seat+=1

Rail = Train("Rajdhani Express",3)
Rail.getinfo()
Rail.ticketbook()
Rail.getinfo()
Rail.ticketbook()
Rail.ticketbook()
Rail.getinfo()
Rail.ticketbook()
ail.ticketcancell()



