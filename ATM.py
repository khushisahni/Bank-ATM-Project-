class Atm(object):

    def __init__(self,card_number,pin):
        self.card_number=card_number
        self.pin=pin
        
    
    def check_balance(self):
        print("your balance is 50000")

    def withdrawl (self,amount):
        new_amount=50000-amount
        print("your withdrawl amount is "+str(amount)+"your remaining balance is "+str(new_amount))

def main():
        card_name=input("insert your card number:-")
        pin_number=input("enter your pin:-")
        new_user=Atm(card_name,pin_number)
        print("choose your activity")
        print("1.balance enquiry 2.Withdrawl")
        activity=int(input("enter activity number:-"))
        if (activity==1):
            new_user.check_balance()
        elif(activity==2):
            amount=int(input("enter the amount:-"))
            new_user.withdrawl(amount)
        else:
            print("enter the valid number")


if __name__ == "__main__":
    main()