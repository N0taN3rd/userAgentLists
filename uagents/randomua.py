from itertools import cycle
import os, csv, random
from pathlib import Path


current_path = os.path.dirname(os.path.realpath(__file__))
base_path = os.path.join(current_path,'csv')

class UserAgents():

    def __init__(self,profile):
        self.dict_files = dict()
        self.profile = profile 
        
        for ufile in os.listdir(base_path):
            file_path = os.path.join(base_path,ufile)
            self.dict_files[ufile.split('.')[0]] = file_path
        
        self.iterator = self._gen_iter(profile=profile)
    
    def _gen_iter(self,profile):
        file_path =self.dict_files[profile]
        with open(file_path,'r') as f:
            csvr = csv.DictReader(f)
            for line in csvr:
                yield line

    def return_ua(self):
        try:
            return next(self.iterator)
        except StopIteration as si:
            self.iterator = self._gen_iter(profile=self.profile)
            return next(self.iterator)
