#ask user to give me string
#Ask user to give order number of the letter print the letter from string

print("Enter a text ")
text = input()

print("Enter the order number of the letter you wan to see")

order_number = int(input())

#We have to consider non-inidex number, number provided would be 1 bigger than provided

index_number = order_number - 1
print (text[index_number])



















