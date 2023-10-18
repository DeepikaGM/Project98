class atm(object):
    def __init__(self,Atmcardnumber,pinnumber):
        self.Atmcardnumber=Atmcardnumber
        self.pinnumber=pinnumber

    def CashWithdrawal(self,amount):
        new_amount=50000-amount
        print("The amount withdrawn is ",amount,"the remaining amount is ", new_amount)

    def BalanceEnquiry(self):
        print("Your current balance is 50000")

def main():
    Atmcardnumber=input("Enter your card number")
    pinnumber=input("Enter your pin number")

    user=atm(Atmcardnumber,pinnumber)

    print("select any activity")
    print("1. Balance enquiry 2.cash withdrawal")

    activity=int(input("Enter activity number: "))

    if(activity==1):
        user.BalanceEnquiry()
    elif (activity==2):
        amount=int(input("Enter the amount to withdraw"))
        user.CashWithdrawal(amount)
    else:
        print("PLease enter valid number")

main()



    
