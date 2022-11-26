from itertools import cycle
import os, csv, random
from pathlib import Path


current_path = os.path.dirname(os.path.realpath(__file__))
path = Path(current_path).parent.absolute()
base_path = os.path.join(path,'csv')


class UserAgents():

    def __init__(self):
        self.dict_files = dict()
        
        for ufile in os.listdir(base_path):
            file_path = os.path.join(base_path,ufile)
            self.dict_files[ufile.split('.')[0]] = file_path

    def gen_ua(self,profile):
        file_path =self.dict_files[profile]
        with open(file_path,'r') as f:
            csvr = csv.DictReader(f)
            for line in csvr:
                yield line['ua']
