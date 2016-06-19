#! usr/bin/python3
import requests
from bs4 import BeautifulSoup

res = requests.get("http://www.cricbuzz.com/cricket-match/live-scores")

soup = BeautifulSoup(res.content,"lxml")

print("\t\t\t\tWELCOME TO LIVE CRICKET SCORE")
print("\n\n\n\n")
#print(soup.find_all("a",{"class":"cb-lv-scrs-well-live"})[0].text)
for item in soup.find_all("a",{"class":"cb-lv-scrs-well-live"}):
	print("\t\t\t"+item.text)	

print("\n\n\n")
print("\n\n\n powered by cricbuzz.com")

