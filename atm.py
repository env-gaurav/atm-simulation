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
user_choice=int(input("enter your choice: "))
if user_choice == 1:
    print("PIN GEN")
elif user_choice == 2:
    print("CASH DEPOSIT")
elif user_choice == 3:
    print("WITHDRAWL")
elif user_choice == 4:
    print("BAL ENQUIRY")
else:
    print("EXIT")
    
