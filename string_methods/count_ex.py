# Ask user to give two different string values 
# if the first string contains the second string 
# return true, if not return false

print("Please enter first word")

first_word = input()

print("Please enter second word")

second_word = input()

is_first_and_second_same = bool(first_word.count(second_word))

print(is_first_and_second_same)



