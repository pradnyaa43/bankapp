bal = 0

def check_bal():
    print('Current Bal=', bal)
    
def deposit(amt):
    global bal
    bal = bal + amt
    print(bal,'Rs. deposited!')

def withdraw(amt):
    global bal
    if bal>amt:
        bal = bal - amt
        print(bal,'Rs. Withdrawn!')
        
    else:
        print('Insufficient Balance!')


while True:
    ch = int(input('\n*Options* \n1. Check Balance \n2. Deposit \n3. Withdraw \n4. Exit \nEnter your choice: '))
    if ch==1:
        check_bal()
        
    elif ch==2:
        d_amt = int(input('Enter amount to deposit: '))
        deposit(d_amt)
        
    elif ch==3:
        w_amt = int(input('Enter amount to Withdraw: '))
        withdraw(w_amt)
        
    elif ch==4:
        print('You Chose to Exit!')
        break
    
    else:
        print('Invalid Choice')
