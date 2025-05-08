class Bus:
    def __init__(self,bus_id,route):
        self.bus_id=bus_id
        self.route=route

    def display_route(self):
        print("Bus",self.bus_id,"goin to way",self.route)

class User:
    def __init__(self,user_id,user_name):
        self.user_id=user_id
        self.name=user_name
        
    def book_ticket(self,num_tickets):
        print(self.name,"has booked",num_tickets,"tickets on a bus",self.bus_id)

        #or

    """ def book_ticket(self,bus,num_tickets):
        print(self.name,"has booked",num_tickets,"tickets on a bus",bus.bus_id) """   

class ticket:
    def __init__(self,ticket_id):
        self.ticket_id=ticket_id

    def ticket_details(self):
        print("Ticket id :",self.ticket_id)

class Redbus(Bus,User,ticket):
    def __init__(self,bus_id,route,user_id,user_name,ticket_id,num_tickets):
        Bus.__init__(self,bus_id,route)
        User.__init__(self,user_id,user_name)
        ticket.__init__(self,ticket_id)

    def book_ticket(self,num_tickets):
        User.book_ticket(self,num_tickets)
        
    def Booking_details(self):
        print("Passenger :",self.name)
        print("Ticket id :",self.ticket_id)
        print("Bus :",self.bus_id)
        print("Route :",self.route)
        print("Total seat booking :",self.num_tickets)


    def salem(self):
        self.ticket_id=303
        self.bus_id=106
        self.route="chennai-to-salem"
        print()
        self.num_tickets=int(input("Enter the number of tickets :"))
        print("Ticket id :",self.ticket_id)
        print("Bus :",self.bus_id)
        print("Route :",self.route)
        print("Total seat booking :",self.num_tickets)

    def wish(self):
        print("Enter 0 to Home page")
        print("Enter 1 to exit")
        l=int(input("Enter the choose :"))
        if l==0:
            print(self.login)
        elif l==1:
            print("Happy Journey")
        
    def login(self):
        p=eval(input("Enter the user name or id:"))
        
        if p==self.name or p==self.user_id:
             print("choose 1 to book bus ticket")
             print("choose 2 to Bus route")
             print("choose 3 to display user details")
             print("choose 4 to Ticket details")
             print()
             c=int(input("Enter the number :"))

             if c==1:
                 print("Bus : 1")
                 print("Bus_id : 106, Route :chennai-to-salem")
                 print("Bus : 2")
                 print("Bus_id : 104, Route :chennai-to-kovai")
                 print("Bus : 3")
                 print("Bus_id : 105, Route :chennai-to-Madurai")
                 print()
                 o=int(input("Enter the choose :"))

                 if o==1:
                     print(self.salem())
                     print()
                     print(self.wish())
                 else:
                     print("Currently not available")
                     
             elif c==2:
                 print("---------->")
                 print("Bus :",self.bus_id)
                 print("Route :",self.route)
             elif c==3:
                 print("---------->")
                 print("@ User Details")
                 print("Name :",self.name)
                 print("User_ID :",self.user_id)
             elif c==4:
                 print("---------->")
                 print("Booked Ticket detail's")
                 print("Ticket id :",self.ticket_id)
                 print("Bus :",self.bus_id)
                 print("Route :",self.route)
        else:
            print("!!! Enter the correct user name")
            print()
            print(self.login())

        

way1=Redbus(103,"chennai-to-Dpi",36,"Mani",656,2)
way2=Redbus(106,"chennai-to-salem",33,"Hari",303,3)
way1.login()
"""user1.display_route()
print()
user1.book_ticket(2)
print()
user1.Booking_details()"""
