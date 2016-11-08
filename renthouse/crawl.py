from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
import csv


url = "http://hz.58.com/pinpaigongyu/pn/{page}/?minprice=2000_4000"