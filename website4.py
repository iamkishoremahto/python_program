from bs4 import BeautifulSoup
import requests
from camelcase import CamelCase

class paragraph:
    def __init__(self,url,cname=""):
        self.Url=url
        self.cname=cname
    
        Web_url= requests.get(url)
        company_name=cname
        data= Web_url.content
        soup= BeautifulSoup(data, 'html.parser')
        para= str(soup.find_all('a'))
        up_cname=cname.upper()
        lo_cname=cname.lower()
        camel_cname= CamelCase(cname)
        #c_name=[up_cname,lo_cname,camel_cname]
        
        # print(para)
        if up_cname or lo_cname or camel_cname  in para:
            print(f"yes, your company is mention on this website {url}")
        else:
            print(f"No, your company is not mention on this website{url}")

if __name__ == "__main__":
    url= input("Enter url")
    cname= input("Enter Company Name : ")
    paragraph(url,cname)
    
    
    

