# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 12:24:58 2016

@author: Chang
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# import data and clean data
df =pd.read_csv('/Users/Chang/Desktop/data_science/loansData.csv')

df.dropna()

# generate boxplot and histogram
df.boxplot(column='Amount.Requested')
df.hist(column='Amount.Requested',bins=20)

# generate QQ plot to test normality of data
fig =plt.figure(figsize=(6,6))
pp = stats.probplot(df['Amount.Requested'],dist='norm',plot=plt)
plt.show()