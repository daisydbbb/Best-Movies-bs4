from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.imdb.com/list/ls055592025/')
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')
movie_titles = []
movie_links = []
movie_scores = []

movies = soup.find_all(name='h3', class_='lister-item-header')
for movie in movies:
  movie_title = movie.find('a')
  movie_titles.append(movie_title.getText())
  movie_links.append('https://www.imdb.com'+movie_title.get('href'))

scores = soup.find_all(name='div', class_='ipl-rating-star small')
for score in scores:
  num = score.find(name='span', class_='ipl-rating-star__rating').getText()
  movie_scores.append(num)


with open('movie.txt', 'w') as file:
  for i in range(100):
    file.write(f'({i}) {movie_titles[i]}, {movie_links[i]}, Rate: {movie_scores[i]} \n')