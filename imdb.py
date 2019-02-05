import requests
from bs4 import BeautifulSoup


class Imdb():
    url = ''
    per_page = ''
    start = ''
    end = ''
    total_page = 0
    movie_links = []
    def __init__(self, url, per_page=50, start=1,end=0):#1005, 1007
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

    def get_movie_info(self):
        for movie in self.movie_links:
            html = requests.get(movie).content
            soup = BeautifulSoup(html,'lxml')

            title = soup.find('div', class_="title_wrapper").h1.text
            
            year = title[-6:-2]
            title = title[:-7].strip()
            rating = soup.find('span', attrs={'itemprop':'ratingValue'}).text
            director = soup.find('div',class_="credit_summary_item").a.text.strip()
            metascore = soup.find('span', class_="metascore")
            
            if(metascore == None):
                metascore = "No Metascore Found"
            print(director)
            print(year)
            print(title)
            print(rating)
            print('-'*10)




        
imdb = Imdb(url='https://www.imdb.com/search/title?user_rating=8.0', per_page=50, end=5)

imdb.browse_all_page()

imdb.get_movie_info()





        

        

