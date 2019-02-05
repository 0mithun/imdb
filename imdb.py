import requests
from bs4 import BeautifulSoup
#url = "https://www.imdb.com/search/title?user_rating=8.0,&start=1&ref_=adv_nxt"


# html = requests.get(url).text
#soup = BeautifulSoup(html,'lxml')

class Imdb():
    url = ''
    total_movie = ''
    per_page = ''
    start_page = ''
    end_page = ''
    total_page = 0
    movie_links = []
    def __init__(self, url, total_movie, per_page=50, start_page=1,end_page=''):
            self.url=url
            self.total_movie = total_movie
            self.per_page = per_page
            self.start_page = start_page
            self.end_page = end_page

    def calculate_total_page(self):
        if((self.total_movie % self.per_page) == 0 ):
            self.total_page = self.total_movie / self.per_page
        else:
            self.total_page = (self.total_movie // self.per_page)+1

    def browse_all_page(self):
        self.calculate_total_page()
        for i in range(self.start_page, self.total_page+1):
            url = self.url + "&start={}".format(i)
            html = requests.get(url).content 
            soup = BeautifulSoup(html,'lxml')
            self.extract_movies_url(soup)
            
    def extract_movies_url(self, data):
        movies = data.find_all('div', class_="lister-item")
        total_movies = len(movies)
        print(total_movies)
        for movie in movies:
            link = "https://www.imdb.com"+ movie.find('div', class_="lister-item-image").a['href']
            print(link)



        
imdb = Imdb(url='https://www.imdb.com/search/title?user_rating=8.0', per_page=50, total_movie=45)


imdb.browse_all_page()




        

        

