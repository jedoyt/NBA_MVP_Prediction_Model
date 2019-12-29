#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 22:45:20 2019

@author: jedunalivia
"""

from nbaPlayers_StatsScraper import scrapeNBAStats
from nbaPlayers_StatsScraper import scrapeMVPs
import os

import pandas as pd

# Build a training dataset consisting of complete stats from year 1957 to 2019

##### UNCOMMENT TO GENERATE CSVs OF NBA STATS #####
years = [i for i in range(1957,2020)]

type = 'per_game' # Choose between 'per_game' or 'totals'

for i in years:
    scrapeNBAStats(year=i,type=type)
##### UNCOMMENT BLOCK ENDS HERE ###################

# Create an initial DataFrame for the year 1957
init_filepath = os.path.join(f'{type}_stats',f'nbaPlayers_stats_{type}_1957.csv')
training_df = pd.read_csv(init_filepath)

# Then create a for loop to concatenate the stats from 1958 to 2019
# to the DataFrame, "training_df"
years = [year for year in range(1958,2020)]

for season in years:
    filename = 'nbaPlayers_stats_{}_{}.csv'.format(type,season)
    filepath = os.path.join(f'{type}_stats',filename)
    df = pd.read_csv(filepath)
    training_df = pd.concat([training_df,df])

# This shall be the training data.
# Generate a csv file out of this compilation of stats.
training_filename = f'training_data_{type}.csv'
training_filepath = os.path.join(f'{type}_stats',training_filename) 
training_df.to_csv(training_filepath, header=True,index=False)

# Generate a csv file of MVPs from .
scrapeMVPs()
