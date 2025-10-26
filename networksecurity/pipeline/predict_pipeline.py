import sys,os
import pandas as pd
import numpy as np
from networksecurity.utils.converting import load_object
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging import logger

class PredictPipeline:
    def __init__(self):
        pass

class CustomData:
    def __init__(self,
                gender:str,
                age:float,
                height:float,
                weight:float,
                family_history_with_overweight:str,
                favc:str,
                fcvc:float,
                ncp:float,
                caec:str,
                smoke:str,
                ch2o:str,
                scc:str,
                faf:float,
                tue:float,
                calc:str,
                mtrans:str):
        
        try:
            self.gender = gender
            self.age = age
            self.height = height
            self.weight = weight
            self.family_history_with_overweight = family_history_with_overweight
            self.favc = favc
            self.fcvc = fcvc
            self.ncp = ncp
            self.caec = caec
            self.smoke = smoke
            self.ch2o = ch2o
            self.scc = scc
            self.faf = faf
            self.tue = tue
            self.calc = calc
            self.mtrans = mtrans

        except Exception as e:
            raise NetworkSecurityException(e)



    # '':'Female',
    # 'age':21.0,
    # 'height':1.62,
    # 'weight':64.0,
    # 'family_history_with_overweight':'yes',
    # 'favc':'no',
    # 'fcvc':2.0,
    # 'ncp':3.0,
    # 'caec':'Sometimes',
    # 'smoke':'no',
    # 'ch2o':2.0,
    # 'scc':'no',
    # 'faf':0.0,
    # 'tue':1.0,
    # 'calc':'no',
    # 'mtrans':'Public_Transportation'