# Date:16/08/2021
#Booking of seat of a train.   This is a very conceptual problem for me 
class Train():
    def __init__(self,name,seats,fair):
        self.name=name
        self.seats=seats
        self.fair=fair
    
    def getinfo(self):
        print(f"The name of the train is {self.name}\nSeats avilable in the train is {self.seats}\nThe fair of the train is {self.fair}")
    
    def seatbook(self):
        if self.seats>0:
            print(f"Your seat is booked and your seat number is {self.seats}")
            self.seats=self.seats-1
            print(f"Seats avilable now {self.seats}")
        else:
            print("Sorry seats are full")
    
    def seatcancelled(self):
        print("Your seat is cancelled")
        self.seats=self.seats+1
        print(f"Seats avilable now {self.seats}")

Rail=Train("Rajdhani Express", 2,"Rs400/")
Rail.getinfo()
Rail.seatbook()   #Now show the seat no. is 2
Rail.seatbook()   #Now show the seat no. is 1
Rail.seatbook()   #Now show you cant book seat as seats are full.
Rail.seatcancelled()  #Cancelling a seat and a seat inc.
Rail.seatbook()       #Now you can book a seat