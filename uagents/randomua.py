from itertools import cycle
import ujson
import random

class UserAgents():
    def __init__(self,browser):

        chrome_file = 'json/chrome.json'
        dict_data = dict()

        if browser == 'chrome':
            with open(chrome_file,'r') as f:
                self.dict_data = ujson.load(f)
        self.list_data = [el['ua'] for el in self.dict_data] 
        self.dict_data = dict()

        random.shuffle(self.list_data)
        self.cuseragent = cycle(self.list_data)
        
if __name__ == '__main__':
    ua = UserAgents('chrome')
    print(next(ua.cuseragent))