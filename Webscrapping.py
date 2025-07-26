import pandas
import requests
from bs4 import BeautifulSoup

Web_url = "https://www.pchotels.com/hotel-and-resort/pearl-continental-hotel-karachi?gad_source=1&gad_campaignid=22773155038&gbraid=0AAAAADMyAoh4BPCCqnNiRHO5vvdU-QYQt&gclid=Cj0KCQjw-ZHEBhCxARIsAGGN96L311nsZ2DD-fEKd2ETxLqX6CflMPxtdiLqfuHmjKA2bRNzg_cVTmAaAlMCEALw_wcB"
response =requests.get(Web_url)
print(response)
data_uthao = BeautifulSoup(response.text,"html.parser")
data_lao =data_uthao.find_all("div",class_="accomodation-content-bx")
RoomName,Description =[],[]

for lala in data_lao:
    h3kolao=lala.find_all("h3")
    p_lao= lala.find_all("p")
    for h3 in h3kolao:
        print(h3.text)
        RoomName.append(h3.text)
        for p in p_lao:
            print(p.text)
            Description.append(p.text)
room_data ={
"RoomName" :RoomName,
"Description":Description
}
df =pandas.DataFrame(room_data)
print(df)
df.to_csv("room_data.csv",index=False)

