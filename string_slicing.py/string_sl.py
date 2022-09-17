#s = "techtorial"

#print(s[4:])

#enter a string which lenght is odd and longer than 3
#and print middle letters

print("enter a string ")

text = input()

middle_index = len(text)//2

print(text[middle_index-1:middle_index+2])


