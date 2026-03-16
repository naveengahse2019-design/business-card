import requests
from django.conf import settings
from django.shortcuts import render
from django.core.cache import cache
from bs4 import BeautifulSoup
from django.http import JsonResponse
import cloudscraper






def home(request):
    return render(request,"mangalla.html")

import cloudscraper
from bs4 import BeautifulSoup
from django.http import JsonResponse


def rates(request):

    scraper = cloudscraper.create_scraper()

    # SILVER
    silver_url = "https://www.goodreturns.in/silver-rates/salem.html"
    res = scraper.get(silver_url)

    soup = BeautifulSoup(res.text, "html.parser")

    silver_tag = soup.find("span", id="silver-1g-price")

    if silver_tag:
        silver = silver_tag.text.strip().replace("₹", "").replace(",", "")
    else:
        silver = "0"


    # GOLD
    gold_url = "https://www.goodreturns.in/gold-rates/salem.html"
    res2 = scraper.get(gold_url)

    soup2 = BeautifulSoup(res2.text, "html.parser")

    gold_tag = soup2.find("span", id="22K-price")

    if gold_tag:
        gold = gold_tag.text.strip().replace("₹", "").replace(",", "")
    else:
        gold = "0"


    return JsonResponse({
        "gold": gold,
        "silver": silver
    })




#############################################
