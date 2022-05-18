from pysitemap import crawler
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import sys

def get_Links(*arg):
    root_url= arg[0]
    crawler(root_url,out_file='sitemap.txt')

def get_word_count():
    f=open("sitemap.txt","r")
    cont=f.readlines()
    total_pages=0
    total_words=0
    
    for i in range(2,len(cont)-1):

        url2=((cont[i].split("<url><loc>")[1].split("</loc></url>")[0]))
        total_pages = total_pages+1
        uClient= uReq(url2)
        page_Html= uClient.read()
        uClient.close()

        page_soup= soup(page_Html, 'html.parser')
        para=str(page_soup.find_all('p'))
       


        p=(para.split("</p>") and para.split("<p>") and para.split(" "))
        total_words= total_words + len(p)

        
        print(url2+"  Total words in this page is ", len(p))
    print(f" Total pages : {total_pages}")
    print(f" Total Words : {total_words}")
    print(f"Average words per page : {total_words/total_pages}")

def main():
    if len(sys.argv) <=2:
            ("you havent given enough info")
    else:
        function= sys.argv[1]
        if function == "get_Links":
            if( len(sys.argv)<2):
                print(sys.argv[1])
            else:
                root_url= sys.argv[2]
                
                get_Links(root_url)
                get_word_count()
if __name__ == '__main__':
    # links('https://en.wikipedia.org/wiki/Salman_Khan')
    # word_count()
    main()
        






# site_map= xmltodict.parse(requests.get('sitemap.xml'))
# print(site_map)