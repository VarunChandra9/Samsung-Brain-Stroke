# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 17:09:24 2020

@author: Varun Chandra
"""

import pandas as pd
import numpy as np
import pickle
import seaborn as sns

pickle_in = open('eng_Data.pickle', 'rb')
data = pickle.load(pickle_in)
pickle_in.close()

sns.pairplot(data)