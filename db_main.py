from bs4 import BeautifulSoup
import openpyxl.workbook
import requests
import pandas as pd

workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Movies"

sheet.append(['Movie', 'Year of release'])
try:
    response = requests.get(
        "https://www.themoviedb.org/tv")
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    movies = soup.find(
        'div', class_="page_wrapper").find_all('div', class_='content')
    movie_list = {"Movie": [], "Year": []}
    for movie in movies:
        # print(movie)
        movie_name = movie.a.text.strip()
        date = movie.p.text.strip()
        # print(movie_name, date)
        # sheet.append([movie_name, date])
        movie_list['Movie'].append(movie_name)
        movie_list['Year'].append(date)


except Exception as e:
    print(e)
df = pd.DataFrame(data=movie_list)
print(df.head())
