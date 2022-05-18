from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

from matplotlib import container

My_url= 'https://en.wikipedia.org/wiki/Hrithik_Roshan'

uClient= uReq(My_url)
page_Html= uClient.read()
uClient.close()

page_soup= soup(page_Html, 'html.parser')
containers = page_soup.find_all('a')
len(containers)
container = str(containers[1])
client_url=(container.split("href=\"")[1].split("\"")[0])
full_url=("https://en.wikipedia.org/"+client_url)
print(full_url)