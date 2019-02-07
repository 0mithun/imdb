import requests
from bs4 import BeautifulSoup
import csv

total_page = 0
movie_links = []


def browse_all_page(url, start=1, end=0, per_page=50):
    for i in range(start, end, per_page):
        url = url + "&start={}".format(i)
        html = requests.get(url).content 
        soup = BeautifulSoup(html,'lxml')
        extract_movies_url(soup, end)
    
        
def extract_movies_url(data, end):
    movies = data.find_all('div', class_="lister-item")
    
    for movie in movies:
        serial = movie.find('span', class_="lister-item-index unbold text-primary").text
        serial = int(serial.replace('.','').replace(',',''))
        if(serial > end):
            break
        link = "https://www.imdb.com"+ movie.find('div', class_="lister-item-image").a['href']
        movie_links.append(link)

def get_movie_info(movie_links):
        for movie in movie_links:
            html = requests.get(movie).content
            soup = BeautifulSoup(html,'lxml')

            title = soup.find('div', class_="title_wrapper").h1.text
            
            year = title[-6:-2]
            title = title[:-7].strip()
            rating = soup.find('span', attrs={'itemprop':'ratingValue'}).text
            director = soup.find('div',class_="credit_summary_item").a.text.strip()
            metascore = soup.find('span', class_="metascore")
            
            if(metascore == None):
                metascore = "No Metascore"
            print(director)
            print(year)
            print(title)
            print(rating)
            print('-'*10)


def write_csv(data, filename="file.csv"):
    with open(filename, 'w', newline='') as csvfile:
        f = csv.writer(csvfile)
        for line in data:
            f.writerow([line])





browse_all_page(url="https://www.imdb.com/search/title?title_type=feature&user_rating=8.0,", start=1, end=18)
print('-'*30)
get_movie_info(movie_links)

try:
    pass
except expression as identifier:
    pass