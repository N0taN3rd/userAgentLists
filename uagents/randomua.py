from itertools import cycle
import ujson
import random
import os


current_path = os.path.dirname(os.path.realpath(__file__))

class UserAgents():
    def __init__(self,browser):

        chrome_file = os.path.join(current_path,'json/chrome.json')
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