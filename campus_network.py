#!coding: utf-8

import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
from optparse import OptionParser
'''
The urllib2 module has been split across several modules in Python 3 named urllib.request and urllib.error. 
The 2to3 tool will automatically adapt imports when converting your sources to Python 3.
'''
parser = OptionParser()
parser.add_option("-u", "--username", action="store", dest="username", default=None,
    help="Your username.")
parser.add_option("-p", "--password", action="store", dest="passwd", default=None, 
    help="Your passwd.")
parser.add_option("-i", "--login", action="store_true", dest="login",
    default=False, help="The flag indicating: login.")
parser.add_option("-o", "--logout", action="store_true", dest="logout",
    default=False, help="The flag indicating: logout.")

(options, args) = parser.parse_args()
login = options.login
logout = options.logout
username = options.username
passwd = options.passwd
if login and logout:
    parser.error("options -i and -o are mutually exclusive.") 
if not (login or logout):
    parser.error("Please specify -i or -o.") 
if login:
    if (username is None) or (passwd is None):
        parser.error("You are intended to login, please specify username and passwd.")
    else:
        host = "http://10.3.8.211/login"
        # data = {"DDDDD": username, "upass": passwd, "0MKKey":""}
        data = {"user": username, "pass": passwd, "0MKKey":""}
        data = urllib.parse.urlencode(data)
        data = data.encode("utf8")
        req = urllib.request.Request(host, data)
        response = urllib.request.urlopen(req)
        html = response.read().decode("utf-8")
        # print(type(html))
        # print(html)
        if response.code == 200 and "您已经登录成功" in html:
            print("Login Successfully!")
        else:
            print("Login failed!")
            if "账号或密码不对，请重新输入" in html:
                print("Ivalid account or password, please login again.")
            else:
                print("Failed because of some other reason(s). Please try again.")
else:
    print("You are intended to logout.")
    url = "http://10.3.8.211/logout"
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    # print(html)
    if response.code == 200:
        print("Logout Successfully!")
    else:
        print("Logout failed!")
        if "msga='Logout Error(-1)'" in html:
            print("You had not logged in.")
        else:
            print("Failed because of some other reason(s). Please try again.")
