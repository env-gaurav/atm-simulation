total_balance = 0.0

def addBalance(amt):
    global total_balance
    total_balance = total_balance + amt
    return total_balance

def withdrawBalance(amt):
    global total_balance
    if total_balance <= 0:
        return print("Insufficient Balance")
    total_balance -= amt
    return total_balance

def balanceEnquiry(amt):
    global total_balance
    return total_balance

atm=f'''
{"-"*30}        
             ATM
{"-"*30}             
1. PIN GEN      2. CASH DEPOSIT
3. WITHDRAWL    4. BAL ENQUIRY
5. EXIT

{"-"*30}
'''
print(atm)
while True:
    user_choice=int(input("enter your choice: "))
    if user_choice== 5:
        print("Thank You for using ATM")
        break
    if user_choice == 1:
        print("PIN GEN")
    elif user_choice == 2:
        cd = float(input("ENTER AMOUNT: "))
        addBalance(cd)
        print(f"NEW BALANCE: {total_balance}")
    elif user_choice == 3:
        cw = float(input("ENTER AMOUNT: "))
        withdrawBalance(cw)
        print(f"NEW BALANCE: {total_balance}")
    elif user_choice == 4:
        print("Total Balance: ", total_balance )
    else:
        print("Acceptable Inputs are 1-5 " )
        break