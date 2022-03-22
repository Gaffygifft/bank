
print('Choose your time either in sec,min or hour')
rate = int(input('choose your rate >> '))
hour = int(input('chosose your hour >> '))
pick_time = input('Input time in sec,min or hour :')
if pick_time == 'sec':
    hour = hour/3600
    pay = rate * hour
    
elif(pick_time) == 'min':
        hour = hour/60
        pay = rate * hour
        
else:
    pay = hour * rate
    
print(pay)

class Bank_System:
  
  def __init__(self):
    self.balance = 1000
    self.credit = 0
    self.debit = 0
    
  def take_amount(self):
    self.credit = int(input(">>"))
    self.debit = int(input(">>"))
    
  def deposit(self):
    if self.credit < 1000:
      print("You can only deposit above 1000")
    else:
      self.amount = self.balance + self.credit
      print("Your balance is now :",self.amount)
      
bank = Bank_System()

print(bank.take_amount())
print(bank.deposit())
    
