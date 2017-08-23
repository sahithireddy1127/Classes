#Create a wallet class, with the following methods: 
#Note: Don't consider negative numbers, when adding or paying money.
#Note: money can be float (23 rupees 43 paisa = 23.43)
#a. add money // Adding money to the wallet.
#b. pay money // Paying money from the wallet.
#c. check balance. // Return the current amount from the wallet.
# Note: Implement the above three methods in the Wallet class.
#Ex: input wallet.add(9) 
#Ex: output wallet.check() //should return 9
class wallet(object):
    def addmoney(self,newmoney):
        addmoney=0
        self.addmoney=self.admoney+newmoney
    def paymoney(self,newpay):
        self.paymoney=self.addmoney-newpay
    def checkbalence(self):
        return self.paymoney
r=int(input('enter the value'))
l=int(input('enter the value'))
a=wallet()
if r<0:
    print ('not considered')
elif l<0:
    print('not considerd')
else:
    print(a.addmoney(r))
    print(a.paymoney(l))
    print(a.checkbalence())

