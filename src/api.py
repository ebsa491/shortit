"""API module for connecting and preparing results."""

import requests
import properties
from bs4 import BeautifulSoup

class UrlAPI:
    """A class for managing the API results."""

    def __init__(self):
        """ __init__ """
        self.__long_url = ""

    def set_url(self, url):
        """This method sets the self.__long_url = url (self.__long_url setter)."""
        self.__long_url = url

    def get_short_url(self):
        """This method returns the self.__short_url (self.__short_url getter)."""
        return self.__short_url

    def request_short_url(self):
        """This method sends a POST request to the API and returns the result text."""
        
        prarams = {properties.API_PARAM: self.__long_url}

        try:
            result = requests.post(properties.API_URL, data = prarams)
        except ConnectionError as err:
            return -1, err

        return 1, result

    def extract_data_from_html(self, html_page):
        """This method parses the html text and finds the input tag with id=\'shortenurl\' for shorten url."""
        
        soup = BeautifulSoup(html_page, 'html.parser')
        input_tag = soup.find("input", attrs={"id": "shortenurl"})
        self.__short_url = input_tag.attrs["value"]
