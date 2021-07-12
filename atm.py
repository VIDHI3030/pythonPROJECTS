class atm:
    def __init__(self, cno, pno):
        self.money = 500
        self.cno = cno
        self.pno = pno
    def withdraw(self):
        amount = int( input("How much do you want to take? "))
        if(amount>self.money):
            print("You have too little money")
        else:
            left = self.money - amount
            print("You have withdrawn ", amount, ". You have " , left, " left.")
    def checkBalance(self):
        print("Your balance is: ", self.money)
    def suprise(self):
        print("Be suprised.")

pincode = input("Enter pin code: ")
cardno = input("ENter card number: ")
user = atm(cardno, pincode)
function = int(input("Press 1 to withdraw, 2 to check balance, 3 for a suprise "))
if function == 1:
    user.withdraw()
elif function == 2:
    user.checkBalance()
elif function == 3:
    user.suprise()
