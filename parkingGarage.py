from IPython.display import clear_output

class Garage:
    #attributes
    def __init__(self, tickets, parkingSpaces, currentTickets):
        self.tickets = [*range(1,11)]
        self.parkingSpaces =  [*range(1,11)]
        self.currentTickets = {}
    #Methods
    def takeTicket(self):
        clear_output()
        if len(self.tickets) > 0:
            print(f'You took ticket number {self.tickets[0]}')
            self.currentTickets[self.tickets[0]]='occupied'
            self.tickets.remove(self.tickets[0])
            self.parkingSpaces.remove(self.parkingSpaces[0])
        else:
            print("sorry we're all full. :(")
    def payParking(self):
        clear_output()
        space = input("What's your ticket number?")
        status = self.currentTickets[int(space)] 
        if status =='occupied':
            pay = input('You owe $1. (type "$1" to pay) ')
            if pay == '$1':
                self.currentTickets[int(space)]="paid"
                print("Thanks for paying. You have 15 minutes to leave.")
        elif status == 'paid':
            print(f'ticket {space} has already been paid for')
        else:
            print("Your money seems funny. We don't play that here. Try again.")
          
    def leaveGarage(self):
        clear_output()
        space = input("What's your ticket number?")
        status = self.currentTickets[int(space)]
        if status =='occupied':
            print("You can't leave without paying.")
        elif status =='paid':
            print("Thanks. buh bye!")
            self.tickets.append(int(space))
            self.parkingSpaces.append(int(space))
            self.currentTickets[space]="free"
        else:
            print("that ticket isn't gonna work here. Try again")

garageA = Garage("","","" )

def run():
    while True:
        response = input('Welcome to the Garage. Please choose a command. ENTER, PAY, or LEAVE: ')
        if response.lower() == "enter":
            garageA.takeTicket()
        if response.lower() == "pay":
            garageA.payParking()
        if response.lower() == "leave":
            garageA.leaveGarage()
run()

