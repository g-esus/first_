s = "          this is python    languaeg  "

print(s)
print(s.strip())

phone_number = "####7774757475448####"

print(phone_number)
print(phone_number.strip("#"))
# Strip is only removing at the begining and end! does not remove in between
#Strip method also works with multiple characters

web_site = "www.techtorial.com"
#Get the domain name from website

print(web_site.strip(".wcmo"))

#given a gmail address from user, print only the user's name
# example@gmail.com

s = "example@gmail.com"

print(s.strip("@gmail.com"))




