#User wants to deposit his money into his bank account, 
#He already has $200 in his account, he has 3 different paycehcks 
# $400, $600 and $350. He can only deposit one paycheck at a time. 
# After he dpesits all the money in the account, he bought a phone 599, headphone 299,
# create a python program to calculate his final money in his account.
# use input the 

Bank_account = 200

print("Please input your paycheck")

Paycheck1 = int(input("first paycheck deposinting"))
Paycheck2 = int(input("Second paycheck deposinting"))
Paycheck3 = int(input("Third paycheck deposinting"))

Bank_account = Paycheck1 + Paycheck2 + Paycheck3
print(Bank_account)

print ( "Please enter what you want to buy")
phone = 599
headphone= 299

if(phone == input(phone)):
Bank_account2 = Bank_account - phone




