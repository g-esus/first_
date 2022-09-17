#you start from end of the word with from  -1 to -m
#3s = "python"
# text = input()
#print(s[-2:])

#Slice from the start 
#print(s[:7])

# enter a string and print rotated 
# hello --> lloha
#java --> vaja

s = input()

first_two = s[:2]
rest_string = s[2:]

s = rest_string + first_two
print(s)