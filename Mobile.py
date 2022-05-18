from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys
from matplotlib import container
def get_MobileDetails_from_Flipkart(*args):
    My_url= args[0]

    uClient= uReq(My_url)
    page_Html= uClient.read()
    uClient.close()

    page_soup= soup(page_Html, 'html.parser')
    f= open("AppleMobile.txt","a+")

    # print(page_soup.prettify)

    containers = page_soup.find_all("div", {"class":"_13oc-S"})
    for i in range(len(containers)):
        container= containers[i]

        model = str(container.find_all("div", {"class":"_4rR01T"}))

        str_model=(model.split(">")[1].split("<")[0])

        price= str(container.find_all("div", {"class":"_30jeq3 _1_WHN1"}))
        str_price=(price.split(">")[1].split("<")[0])

        configuration = str(container.find_all("div",{"class":"fMghEO"}))
        str_configuration=(configuration.split(">")[3].split("</li")[0] + " "+ configuration.split(">")[5].split("</li")[0]+" "+ configuration.split(">")[7].split("</li")[0]+" "+ configuration.split(">")[8].split("</li")[0].split("<li class=\"rgWa7D\"")[0]+" "+ configuration.split(">")[9].split("</li")[0].split("<li class=\"rgWa7D\"")[0])

        rating = str(container.find_all("div",{"class":"gUuXy-"}))
        str_rating=(rating.split("<span>")[2].split("</span")[0])
        str_reviews=(rating.split("<span>")[3].split("</span")[0])
        print(f"\nModel : {str_model}")
        print(f"Details : {str_configuration}")
        print(f"Price : {str_price}")
        print(f"Ratings : {str_rating}")
        print(f"Reviews : {str_reviews}\n")

def main():
    if len(sys.argv) <=2:
            ("you havent given enough info")
    else:
        function= sys.argv[1]
        if function == "get_MobileDetails_from_Flipkart":
            if( len(sys.argv)<2):
                print(sys.argv[1])
            else:
                My_url= sys.argv[2]
                get_MobileDetails_from_Flipkart(My_url)
                
if __name__ == '__main__':

    main()
