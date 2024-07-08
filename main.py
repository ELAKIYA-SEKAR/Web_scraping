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
    for movie in movies:
        # print(movie)
        movie_name = movie.a.text.strip()
        date = movie.p.text.strip()
        # print(movie_name, date)
        # sheet.append([movie_name, date])

except Exception as e:
    print(e)
workbook.save("Movies.xlsx")
