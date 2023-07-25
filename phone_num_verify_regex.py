#Phone number verification.Phone number should consist of 1st character +,next 3 digits between 233,rest 0-9)
import re


num=re.compile("^[\+]+[233]{3}.[0-9]{7}$")
user_input=input('Enter your number to verify :')
if re.search(num,user_input):
    print('Valid number ')
else:
    print('Invalid number,try again')    