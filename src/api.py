"""API module for connecting and preparing results."""

import requests
import properties
from bs4 import BeautifulSoup

class UrlAPI:
    def __init__(self):
        self.__long_url = ""

    def set_url(self, url):
        self.__long_url = url

    def get_short_url(self):
        return self.__short_url

    def request_short_url(self):
        
        prarams = {properties.API_PARAM: self.__long_url}

        try:
            result = requests.post(properties.API_URL, data = prarams)
        except ConnectionError as err:
            return -1, err

        return result

    def extract_data_from_html(self, html_page):
        
        soup = BeautifulSoup(html_page, 'html.parser')
        input_tag = soup.find("input", attrs={"id": "shortenurl"})
        self.__short_url = input_tag.attrs["value"]
