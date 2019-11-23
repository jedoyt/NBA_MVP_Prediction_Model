#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:00:00 2019

@author: jedunalivia
"""

# Import needed libraries
from sklearn.ensemble import RandomForestRegressor
from nbaPlayers_StatsScraper import scrapeNBAStats
from datetime import datetime
import numpy as np
import pandas as pd


# PREPARE: Pre-processing
# Create DataFrames for building training data
train_df = pd.read_csv('training_data.csv')
mvp_df = pd.read_csv('nbaMVPs.csv')

# Add an additional feature for the training data: 'MVP'
# contains only two unique values of 0 and 1. 0 for 'not MVP' and 1 for 'MVP'

# Add additional column ['Season-Player'] on train_df and mvp_df
# This additional column shall served as an MVP marker reference
train_df['Season-Player'] = train_df['Season'] + '_' + train_df['Player'].str.replace(' ','_')
mvp_df['Season-Player'] = mvp_df['Season'] + '_' + mvp_df['Player'].str.replace(' ','_')

# Create a list that shall contain the values for the 'MVP' column for train_df

mvp_colvals = [] # The contents of this list shall be stored under the new column,"MVP" on train_df

# Convert the 'Season-Player' column into an array for faster computing
train_array = np.array(train_df['Season-Player'])
mvp_array = np.array(mvp_df['Season-Player'])

# Perform a for loop to store values on mvp_colvals
for val in train_array:
    if val in mvp_array:
        mvp_colvals.append(1)
    else:
        mvp_colvals.append(0)

# Add additional column 'MVP' on train_df. This column shall be the target(y) for our training dataset
train_df['MVP'] = mvp_colvals

# Update the 'training_data.csv' by overwriting it with the data under train_df
train_df.to_csv('training_data.csv', header=True,index=False)

# Drop NaN values from train_df
train_df.dropna(axis=0,inplace=True)

# Set index to 'Season-Player' column
train_df = train_df.set_index('Season-Player')

# DEFINE: Set features & target, apply train_test_split, define model

features = ['G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P','3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB','DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']
X = train_df[features]
y = train_df['MVP']

# Define model by creating an instance of RandomForestRegressor
model = RandomForestRegressor(n_estimators=1000,random_state=0)

# FIT: Train the model
model.fit(X,y)

# Build dataframe containing the stats of current ongoing season (2019-20): X_currentSeason
scrapeNBAStats(datetime.now().year + 1)
X_currentSeason = pd.read_csv('nbaPlayers_statsPerGame_{}.csv'.format(datetime.now().year + 1))

# Drop NaN values from test_df
X_currentSeason.dropna(axis=0,how='any',inplace=True)

# Add 'Season-Player' column
X_currentSeason['Season-Player'] = X_currentSeason['Season'] + '_' + X_currentSeason['Player'].str.replace(' ','_')

# Set index to 'Season-Player' column
X_currentSeason = X_currentSeason.set_index('Season-Player')

# PREDICT:
X_subject = X_currentSeason[features]
model_predictions = model.predict(X_subject)

# DISPLAY RESULTS:
results = X_subject.copy()
results['Prediction'] = model_predictions
# TOP 10 Candidates
print(results.nlargest(10,'Prediction'))