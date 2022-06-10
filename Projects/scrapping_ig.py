#!usr/bin/python

########################
#          Scrapping Ig #Draft
#          Name: 
#          Date: 10/6/2021
########################
import requests
from bs4 import BeautifulSoup as bs

user_name = "_m.a.r.l.e.y_gone_r.o.g.u.e" # input ("user-name")
url = "https://instagram/"+user_name #input ("Enter site url")
results= requests.get(url)

soup = bs(results.content, "html.parser")
profile_pic = soup.find('img',{'alt':'Avatar'})
print(profile_pic)