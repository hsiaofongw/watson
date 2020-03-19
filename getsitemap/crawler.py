import urllib
from typing import List
from typing import Dict
from urllib.request import Request

# crawl the sitemap response (bytes) by using urllib
class Crawler:

    def __init__(self, user_agent: str):
        self.user_agent = user_agent
    
    def make_request(self, url: str, headers: Dict[str, str]) -> Request:
        request = Request(url, None, headers)
        return request

    def crawl(self, url: str) -> bytes:
        user_agent = self.user_agent
        headers = {
            'User-Agent': user_agent
        }

        request = self.make_request(url, headers)
        response = urllib.request.urlopen(request)
        data = response.read()
        return data
