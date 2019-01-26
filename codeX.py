###################################################################
#                        Import Module
import json , sys , hashlib , os , time , marshal
###################################################################
'''
     Jangan Direcode ya bosku , tinggal make apa susahnya sih
'''
###################################################################
#                             COLOR
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
###################################################################
#                      Exception
try:
	import requests
except ImportError:
	print R + '_     _'.center(44)
	print "o' \.=./ `o".center(44)
	print '(o o)'.center(44)
	print 'ooO--(_)--Ooo'.center(44)
	print W + ' '
	print ('Jony . Shark's ').center(44)
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()
####################################################################
#                    Set Default encoding
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################################################################
#       	        I don't know
jml = []
jmlgetdata = []
n = []
####################################################################
#                        BANNER
def baliho():
	try:
		token = open('cookie/token.log','r').read()
		r = requests.get('https://graph.facebook.com/me?access_token=' + token)
		a = json.loads(r.text)
		name = a['name']
		n.append(a['name'])

		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('[] ' + name + ' []').center(44)
		print ' '

	except (KeyError,IOError):
		print R + '_     _'.center(44)
		print "o' \.=./ `o".center(44)
		print '(o o)'.center(44)
		print 'ooO--(_)--Ooo'.center(44)
		print ' ' + W
		print ('Shark's').center(44)
		print (W + '     [' + G +'Open Source Information Facebook'+ W + ']')
		print ' '
####################################################################
#		    Print In terminal
def show_program():

	print '''
                    %sINFORMATION%s
 ------------------------------------------------------

    Author     Debby Anggraini 'CiKu370'
    Name       Shark's 'Open Source Information Facebook'
    CodeName   Jony
    version    full version
    Date       25/01/2019 09:35:12
    Team       Blackhole Security
    Email      jony6sex@gmail.com
    Telegram   @Jony6sex

* if you find any errors or problems , please contact
  author
'''%(G,W)
def info_ga():

	print '''
     %sCOMMAND                      DESCRIPTION%s
  -------------       -------------------------------------

   get_data           fetching all friends data
   get_info           show information about your friend

   dump_id            fetching all id from friend list
   dump_phone         fetching all phone number from friend list
   dump_mail          fetching all emails from friend list
   dump_<id>_id       fetching all id from your friends <spesific>
		      ex: dump_username_id

   token              Generate access token
   cat_token          show your access token
   rm_token           remove access token

   bot                open bot menu

   clear              clear terminal
   help               show help
   about              Show information about this program
   exit               Exit the program
'''%(G,W)
def menu_bot():
	print '''
   %sNumber                  INFO%s
 ---------   ------------------------------------

   [ 01 ]      auto reactions
   [ 02 ]      auto comment
   [ 03 ]      auto poke
   [ 04 ]      accept all friend requests
   [ 05 ]      delete all posts in your timeline
   [ 06 ]      delete all friends
   [ 07 ]      stop following all friends
   [ 08 ]      delete all photo albums

   [ 00 ]      back to main menu
'''%(G,W)
def menu_reaction():
	print '''
   %sNumber                  INFO%s
 ----------   ------------------------------------

   [ 01 ]      like
   [ 02 ]      reaction 'LOVE'
   [ 03 ]      reaction 'WOW'
   [ 0
