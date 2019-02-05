import requests
from bs4 import BeautifulSoup
#url = "https://www.imdb.com/search/title?user_rating=8.0,&start=1&ref_=adv_nxt"


# html = requests.get(url).text
#soup = BeautifulSoup(html,'lxml')

class Imdb():
    url
    total_page
    per_page
    start_page
    end_page
    def __init__(self, url, total_page='', per_page=50, start_page=1,end_page=''):
            self.url=url
            self.total_page = total_page
            self.per_page = per_page
            self.start_page = start_page
            self.end_page = end_page
    

        

        

