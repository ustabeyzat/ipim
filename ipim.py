
import socket as soc
import urllib.request as req
import re

try:
 rec = soc.socket()
 rec.connect(("www.ipsorgu.com", 80))
 val = req.urlopen("http://www.ipsorgu.com/").read().decode("latin")

 name = soc.gethostname()
 pub = re.findall('<span class="yazi">.+</span>', val)[3][19:-7]
 loc = rec.getsockname()[0]

 rec.close()

 print(f"{name}\n{pub}\n{loc}")
 print(f"\nCihaz adi(hostname): {name} \nGenel(public) ip: {pub} \nYerel(local) ip: {loc}")
 input("enter 'a basarak kapat..")
except:
 input("Hata! Daha sonra tekrar deneyin..")
