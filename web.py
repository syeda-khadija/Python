import pandas
import requests
from bs4 import BeautifulSoup

Web_url = "https://www.nueplex.com/ticket.html"
response =requests.get(Web_url)
print(response)
data_uthao = BeautifulSoup(response.text,"html.parser")
data_lao =data_uthao.find_all("div",class_="table-responsive ticket")
print(data_lao)
moviename ,price=[],[]


for data in data_lao:
     tbody_lao=data.find_all("tbody")
     print(tbody_lao)
     for tr in tbody_lao:
         th=data.find_all("th")
         td=data.find_all("td")
         for th_lao in th:
           moviename.append(th_lao.text)
 # for td_lao in td:
        #     price.append(td_lao.text)

Movies_data = {
"Movie Name":moviename,
# "Price":price
}
movie_df = pandas.DataFrame(Movies_data)
print(movie_df)