#!/usr/bin/python2

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
    
    print 'logging in as %s' % username

    cj = cookielib.CookieJar() 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj)) 
    login_data = urllib.urlencode({'email_address': username,
                                   'password' : password })
    opener.addheaders.append(('User-agent', 'Mozilla/4.0'))
    page= 'https://www.ml-class.org/course/auth/login'

    #Try to log in and get the result html
    opener.open(page, login_data)
    check=opener.open('http://www.ml-class.org/course/class/index')
    print 'We are in.'
    return opener

def get_vid_ids(page):
    x=re.findall('file: \'[0-9][0-9].*?\'',page)
    y=[""]*len(x)
    #print x
    for i in range(len(x)):
        z=re.findall('\'.*\'',x[i])
        #print("z = %s",z)
        y[i]=z[0]
        y[i]=y[i].strip('\'')
    return y

def make_url(id):
    print id
    url = r"http://download-videos.ml-class.org/cs229/videos/%s.mp4" % id
    return url

def downloadVid(opener,url):
    file_name = url.split('/')[-1]
    u = opener.open(url)
    file_path = "vids/"
    file_path+=file_name
    f = open(file_path, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)

    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()



ml_opener=get_login(argv[1],argv[2])
page=ml_opener.open('http://www.ml-class.org/course/video/list?mode=download')

ids = get_vid_ids(page.read())


for i in ids:
   url=make_url(i)
   #print url
   downloadVid(ml_opener,url)
