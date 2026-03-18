import requests
from bs4 import BeautifulSoup

# GOLD
gold_url = "https://www.goodreturns.in/gold-rates/salem.html"
r = requests.get(gold_url)

soup = BeautifulSoup(r.text,"html.parser")
gold = soup.find("span", id="22K-price").text.strip().replace("₹","").replace(",","")

# SILVER
silver_url = "https://www.goodreturns.in/silver-rates/salem.html"
r2 = requests.get(silver_url)

soup2 = BeautifulSoup(r2.text,"html.parser")
silver = soup2.find("span", id="silver-1g-price").text.strip().replace("₹","").replace(",","")

# SEND TO DJANGO
requests.post(
    "https://gnanavel.pythonanywhere.com/update_rates/",
    json={"gold": gold, "silver": silver}
)

print("Rates updated:", gold, silver)