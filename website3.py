import requests
from bs4 import BeautifulSoup
import camelcase

class paragraph:
    def __init__ (self,url,cname):
        self.url=url
        self.cname=cname
    
        urld =requests.get(url)
        data=urld.content
        soup = BeautifulSoup(data,'html.parser')
        parapettify=soup.prettify()
        para = soup.find_all('p')
        para2= str(para)
        para3= para2.split("</p>,")
        company=0
        # CompanyFind= para2.find("Vmoksha Technologies" or "vmoksha technologies" or "VMOKSHA TECHNOLOGIES" )


        for item in para3:
            # print(item +"\n")
            if cname in item:
                company = company +1
            #if item == f"{cname}" or item == f"cname.upper()" or item == f"cname.lower()" 
        if company>0:
            print(f"yes, your company is mention on this website {url}")
        else:
            print(f"No, your company is not mention on this website{url}")    
        #print(company)
        # print(CompanyFind)

if __name__ == '__main__':
    
    url=input("Enter the url : ")
    companyname=input("Enter the company name : ")

    paragraph(url,companyname)
    