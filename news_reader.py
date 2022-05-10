
from hashlib import new
import requests
import json
def news_Reader(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)

s="My name is kishore"

if __name__ == '__main__':
    r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=330a890633df4c90a66b5550e50aab56")
    data=json.loads(r.content)
    
    
    for i in range(10):
        title=(data['articles'][i]['title'])
        description=(data['articles'][i]['description'])
        news_Reader(title)
        news_Reader(description)
    
