def credit(balance,value):
    balance=balance+value
    return balance

def debit(balance,value):
    balance=balance-value
    return balance

def show_balance(balance):
    print(balance)
    
    
x=int(input("ENTER THE AMOUNT TO CREDITED:"))
y=int(input("ENTER THE AMOUNT TO DEBITED:")) 
       
balance=0
print("Balance =", end =" ")
balance=credit(balance,x)
balance=debit(balance,y)
show_balance(balance)
    
    
    





