import requests

from api import API


class Public(API):
    def ping(self) -> bool:
        response = requests.get(f'{self.URL}/ping')
        success = response.status_code == 200 and response.text.startswith('pong')

        return success
