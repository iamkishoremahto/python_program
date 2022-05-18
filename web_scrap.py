from cgitb import html
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

from cv2 import split


My_Url= 'https://www.flipkart.com/search?q=television&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
uClient = uReq(My_Url)
html_page= uClient.read()
uClient.close()

soup= bs(html_page,'html.parser')
# print(soup.prettify)
containers= soup.find_all("div",{"class":"_1AtVbE col-12-12"})
urlslink=soup.find_all("a")
tv_name=(soup.findAll("div",{"class":"_4rR01T"}))
tv_specification=(soup.find_all("ul",{"class":"_1xgFaf"}))
tv_price=( soup.find_all("div",{"class":"_30jeq3 _1_WHN1"}))
tv_rating=(soup.find_all("span",{"class":"_2_R_DZ"}))

# for i in range(len(tv_name)):
#     print("\n",tv_name[i].getText())
#     print((tv_specification[i].getText()))
#     print(tv_price[i].getText())
#     print(tv_rating[i].getText(),"\n")
print(urlslink['href='])