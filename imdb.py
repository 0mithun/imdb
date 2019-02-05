import requests
from bs4 import BeautifulSoup
#url = "https://www.imdb.com/search/title?user_rating=8.0,&start=1&ref_=adv_nxt"


# html = requests.get(url).text
#soup = BeautifulSoup(html,'lxml')

class Imdb():
    url = ''
    per_page = ''
    start = ''
    end = ''
    total_page = 0
    movie_links = []
    def __init__(self, url, per_page=50, start=0,end=0):#1005, 1007
            self.url=url
            self.per_page = per_page
            self.start = start
            self.end = end

    def browse_all_page(self):
        for i in range(self.start, self.end, self.per_page):
            url = self.url + "&start={}".format(i)
            html = requests.get(url).content 
            soup = BeautifulSoup(html,'lxml')
            print(url)
            self.extract_movies_url(soup)
         
    def extract_movies_url(self, data):
        movies = data.find_all('div', class_="lister-item")
        
        for movie in movies:
            serial = movie.find('span', class_="lister-item-index unbold text-primary").text
            serial = int(serial.replace('.','').replace(',',''))
            if(serial >self.end):
                break
            link = "https://www.imdb.com"+ movie.find('div', class_="lister-item-image").a['href']
            self.movie_links.append(link)
            print(link)




        
imdb = Imdb(url='https://www.imdb.com/search/title?user_rating=8.0', per_page=50, start=1005,  end=1018)

imdb.browse_all_page()




        

        

