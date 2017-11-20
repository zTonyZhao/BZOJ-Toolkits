#! python3
#BZOJ Crawler Version 0.1
#A Simple Crawler of BZOJ
#Code is ugly because time is limited.
#Please run it under the environment Python 3
#Powered by Tony Zhao
#https://tonyzhao.xyz/bzoj-toolkits
#No input or interaction designed.
#DO NOT USE IF YOU ARE NOT A PERMITTED USER.

import requests
import codecs

# Input the username, password, L & R (Beginning and End ID of the Tasks which is crawed)

UserName = ""
Password = ""

l = 
r = 

Dir = "CrawedFiles"

login_url = 'http://www.lydsy.com/JudgeOnline/login.php'
s = requests.Session()
s.post(login_url, {'user_id': UserName, 'password': Password})
for i in range(l,r):
	r = s.get("http://www.lydsy.com/JudgeOnline/problem.php?id=%d" % i)
	r.encoding = 'utf-8'
	f = open("%s\\%d.html" % (Dir,i),"w",encoding="utf8")
	f.write(r.text)
	print("%d: OK" % i)
