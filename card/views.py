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
import json
import os


def rates(request):

    gold = None
    silver = None

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:
        scraper = cloudscraper.create_scraper()

        # SILVER
        silver_url = "https://www.goodreturns.in/silver-rates/salem.html"
        res = scraper.get(silver_url, headers=headers, timeout=10)

        soup = BeautifulSoup(res.text, "html.parser")
        silver_tag = soup.find("span", id="silver-1g-price")

        if silver_tag:
            silver = silver_tag.text.strip().replace("₹", "").replace(",", "")

        # GOLD
        gold_url = "https://www.goodreturns.in/gold-rates/salem.html"
        res2 = scraper.get(gold_url, headers=headers, timeout=10)

        soup2 = BeautifulSoup(res2.text, "html.parser")
        gold_tag = soup2.find("span", id="22K-price")

        if gold_tag:
            gold = gold_tag.text.strip().replace("₹", "").replace(",", "")

    except Exception as e:
        print("Scraping error:", e)

    # 🔥 fallback
    if not gold or not silver:
        try:
            file_path = os.path.join(os.path.dirname(__file__), "rates.json")

            with open(file_path) as f:
                data = json.load(f)

            gold = gold or data.get("gold", "0")
            silver = silver or data.get("silver", "0")

        except Exception as e:
            print("Fallback error:", e)
            gold = gold or "0"
            silver = silver or "0"

    return JsonResponse({
        "gold": gold,
        "silver": silver
    })
# import cloudscraper
# from bs4 import BeautifulSoup
# from django.http import JsonResponse


# def rates(request):

#     scraper = cloudscraper.create_scraper()

#     # SILVER
#     silver_url = "https://www.goodreturns.in/silver-rates/salem.html"
#     res = scraper.get(silver_url)

#     soup = BeautifulSoup(res.text, "html.parser")

#     silver_tag = soup.find("span", id="silver-1g-price")

#     if silver_tag:
#         silver = silver_tag.text.strip().replace("₹", "").replace(",", "")
#     else:
#         silver = "0"


#     # GOLD
#     gold_url = "https://www.goodreturns.in/gold-rates/salem.html"
#     res2 = scraper.get(gold_url)

#     soup2 = BeautifulSoup(res2.text, "html.parser")

#     gold_tag = soup2.find("span", id="22K-price")

#     if gold_tag:
#         gold = gold_tag.text.strip().replace("₹", "").replace(",", "")
#     else:
#         gold = "0"


#     return JsonResponse({
#         "gold": gold,
#         "silver": silver
#     })




#############################################
