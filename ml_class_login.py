import cookielib
import urllib
import urllib2
import re
from sys import argv
from sys import exit

from BeautifulSoup import BeautifulSoup



def get_login (username, password):
    
    ''' log in to what.cd and get a cookie
        opener is returned and should be used to open other pages inside '''
    
    print('logging in as %s',username)

    cj = cookielib.CookieJar() 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
    login_data = urllib.urlencode({'email_address': 'clm2183@columbia.edu',
                                   'password' : 'a54915'})
    opener.addheaders.append(('User-agent', 'Mozilla/4.0'))
    page= 'https://www.ml-class.org/conurse/auth/login'

    #Try to log in and get the result html
    opener.open(page, login_data)
    check=opener.open('http://www.ml-class.org/course/class/index')
    print 'We are in.'
    return opener

def get_vid_ids(page):
    re.search('
    
ml_opener=get_login(argv[1],argv[2])
page=ml_opener.open('http://www.ml-class.org/course/video/list?mode=download')


