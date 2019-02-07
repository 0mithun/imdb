import requests
from bs4 import BeautifulSoup
import csv

total_page = 0
movie_links = []
movie_details = []


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

def write_csv(data, filename="file.csv"):
    with open(filename, 'w', newline='') as csvfile:
        f = csv.writer(csvfile)
        for line in data:
            f.writerow([line['title'],line['year'],line['director'],line['rating'], line['metascore'], line['budget']])

def get_movie_details(movie_links):
        for movie in movie_links:
            html = requests.get(movie).content
            soup = BeautifulSoup(html,'lxml')
            title = soup.find('div', class_="title_wrapper").h1.text
            year = title[-6:-2]
            title = title[:-7].strip()
            rating = soup.find('span', attrs={'itemprop':'ratingValue'}).text
            director = soup.find('div',class_="credit_summary_item").a.text.strip()
            metascore = soup.find('div', class_="metacriticScore")
            if(metascore == None):
                metascore = "No Metascore"
            else:
                metascore = soup.find('div', class_="metacriticScore").text.strip()              
            box = soup.find('h4', text="Budget:")            
            if(box == None):
                budget = "No Budget Found"
            else:
                budget = box.parent.text.strip().split('\n')[0]
                try:
                    budget = budget.split('$')[1]
                except IndexError:
                    budget = budget.split('\xa0')[1]
            
            data = {'title': title,'year':year,'director':director,'rating':rating,'metascore':metascore,'budget':budget}
            movie_details.append(data)



browse_all_page(url="https://www.imdb.com/search/title?title_type=feature&user_rating=8.0,", start=1, end=100)

get_movie_details(movie_links)

write_csv(data=movie_details, filename='movies.csv')
