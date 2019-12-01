#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:45:20 2019

@author: jedunalivia
"""

from nbaPlayers_StatsScraper import scrapeNBAStats
from nbaPlayers_StatsScraper import scrapeMVPs

import pandas as pd

# Build a training dataset consisting of complete stats from year 1957 to 2019

##### UNCOMMENT TO GENERATE CSVs OF NBA STATS #####
years = [i for i in range(1957,2020)]

for i in years:
    scrapeNBAStats(i)
##### UNCOMMENT BLOCK ENDS HERE ###################

# Create an initial DataFrame for the year 1957
training_df = pd.read_csv('nbaPlayers_statsPerGame_1957.csv')

# Then create a for loop to concatenate the stats from 1958 to 2019
# to the DataFrame, "training_df"
years = [year for year in range(1958,2020)]

for season in years:
    filename = 'nbaPlayers_statsPerGame_{}.csv'.format(season)
    df = pd.read_csv(filename)
    training_df = pd.concat([training_df,df])

# This shall be the training data.
# Generate a csv file out of this compilation of stats.
training_df.to_csv('training_data.csv', header=True,index=False)

# Generate a csv file of MVPs from .
scrapeMVPs()