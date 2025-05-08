class ATM:
    Bank_Name="SBI"
    Branch="velachery"
    IFSE_Code="SBI000126"

    def __init__(self,Name,Account,phone,bal,pin):
        self.Name=Name
        self.Account_no=Account
        self.Phone_no=phone
        self.Balance=bal
        self.PIN=pin

    def Insert_card(self):
        pin=int(input("Enter the PIN Number :"))
        if pin==self.PIN:
            print("1. Withdraw")
            print("2. Deposite")
            print("3. Balance Enquiry")
            print("4. PIN change")
            print("5. Account detials")
            cho=int(input("Choose your choice :"))
            if cho==1:
                self.withdraw(int(input("Enter the withdraw amount :")))
            elif cho==2:
                self.deposite(int(input("Enter the deposite amount :")))
            elif cho==3:
                self.Balance_Enquiry()
            elif cho==4:
                self.check_phone_no(int(input("Enter the phone no :")))
            elif cho==5:
                self.account_details()
            else:
                print("Enter the Correct number")
        else:
            print("Incorrect pin")
            print("Pls Take your card")



    def In_card(self):
        print("1. Withdraw")
        print("2. Deposite")
        print("3. Balance Enquiry")
        print("4. PIN change")
        print("5. Account detials")
        cho=int(input("Choose your choice :"))
        if cho==1:
            self.withdraw(int(input("Enter the withdraw amount :")))
        elif cho==2:
            self.deposite(int(input("Enter the deposite amount :")))
        elif cho==3:
            self.Balance_Enquiry()
        elif cho==4:
            self.check_phone_no(int(input("Enter the phone no :")))
        elif cho==5:
            self.account_details()
        else:
            print("Enter the Correct number")
    
#balance
    
    def Balance_Enquiry(self):
        print("Current Balance :",self.Balance)
        print("Thank you")


#withdraw
                
    def withdraw(self,amount):
        if amount<=self.Balance:
            self.Balance=self.sub(self.Balance,amount)
            self.Balance_Enquiry()
        else:
            print("Insufficient Balance")
        print("1.Continue")
        print("2.Exit")
        sel=int(input("Choose your choice :"))
        if sel==1:
            self.In_card()
        else:
            print("Thank you")
            print(" Visit Again")

    @staticmethod
    def sub(num1,num2):
        result=num1-num2
        return result

#deposite
    
    def deposite(self,amount):
        self.Balance=self.add(self.Balance,amount)
        self.Balance_Enquiry()
        print("1.Continue")
        print("2.Exit")
        sel=int(input("Choose your choice :"))
        if sel==1:
            self.In_card()
        else:
            print("Thank you")
            print(" Visit Again")


    @staticmethod
    def add(num1,num2):
        result=num1+num2
        return result

#pin change
    
    def check_phone_no(self,phone):
        if phone==self.Phone_no:
            n=(int(input("Enter the new pin :")))
            self.PIN=n
            print("Successfully new pin was changed")
            print("check new pin Enter : 1")
            print("exit Enter the : 0")
            a=int(input("Enter the num :"))
            if a==0:
                self.Balance_Enquiry()
            elif a==1:
                print()
                user.Insert_card()
            else:
                print("Enter the correct number")
        else:
            print("worng phone number")
            
#account details
    def account_details(self):
        print("-"*24)
        print(" "*5,ATM.Bank_Name,ATM.Branch)
        print("-"*24)
        print("Name :",self.Name)
        print("IFSE CODE :",ATM.IFSE_Code)
        hi=str(self.Account_no)
        h=hi[:4]+'x'*5+hi[-2:]
        print("Account No :",h)
        li=str(self.Phone_no)
        l=li[:3]+'x'*4+li[-1]
        print("Phone No :",l)
        print("Balance :",self.Balance)
        print("1.Continue")
        print("2.Exit")
        sel=int(input("Choose your choice :"))
        if sel==1:
            self.In_card()
        else:
            print("Thank you")
            print(" Visit Again")




user=ATM("Mani",63598245276,9944457363,6000,3563)
user.Insert_card()




