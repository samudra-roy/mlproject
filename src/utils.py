#  any functionalities that i am writing in a common way, to be used in entire application

import os
import sys
import dill

from src.exception import CustomException
from src.logger import logging

import numpy as np
import pandas as pd


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)