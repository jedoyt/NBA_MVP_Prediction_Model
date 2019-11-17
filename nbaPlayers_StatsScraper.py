#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 21:21:35 2019

@author: jedunalivia
"""

# Import libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def scrapeNBAStats(year=datetime.now().year):
    '''
    Scrapes for per game statistics of all NBA Players on a given season
    
    scrapeNBAStats(year=datetime.now().year)
    year: int object; defaults to current year
    
    OUTPUT: 'nbaPlayers_statsPerGame_yyyy.csv'
    'yyyy' is the year of the season
    '''
    # URL to be requested
    url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
    
    # Create requests object: res
    print("Now requesting...", url)
    res = requests.get(url)
    print(res.raise_for_status)

    # Create BeautifulSoup Object: `soup`
    soup = BeautifulSoup(res.text, features='lxml')
    print("Created BeautifulSoup object: soup")
    
    # Parse the column headers and store them in a list
    headers = soup.thead.getText().split('\n')[3:-2] # Slicers are intended to exclude unnecessary headers
    
    # Parse the rows(player stats) and store them in a list
    rows = soup.findAll('tr')[1:]
    
    # Create the rows for each player and their stats as a list of list
    player_stats = []
    for i in range(0,len(rows)):
        try:
            row = [td.getText() for td in rows[i]][1:] # Parses the texts within the tags and excludes the values
                                                    # under 'Rk' column since it was also excluded in our headers
            player_stats.append(row)
        except AttributeError: # For every 20 iteration of this loop, it encounters this error
                                # and needs to pass over it and continue on the next iteration
            pass

    print("Scraping and Parsing Complete!")         
    
    # Create a pandas DataFrame
    stats = pd.DataFrame(player_stats, columns=headers)
    
    season_prefix = str(year-1)
    season_suffix = str(year)[2:]
    
    season = "{}-{}".format(season_prefix,season_suffix)
    
    stats['Season'] = season
    
    # Create a csv file from this DataFrame
    filename = 'nbaPlayers_statsPerGame_{}.csv'.format(year)
    stats.to_csv(filename,header=True, index=False)
    print("Generated csv file last {}: {}".format(datetime.now(),filename))

def scrapeMVPs():
    '''
    Scrapes for NBA MVPs from to 2000 to 2018
    OUTPUT: 'nbaMVPs.csv'
    '''
    # URL to be requested
    url = "https://www.basketball-reference.com/awards/mvp.html"

    # Create requests object: res
    print("Now requesting...", url)
    res = requests.get(url)
    print(res.raise_for_status)

    # Create BeautifulSoup Object: `soup`
    soup = BeautifulSoup(res.text, features='lxml')
    print("Created BeautifulSoup object: soup")
    
    # Parse the table
    html_table = soup.findAll('tr')[1:] # Sliced first header

    # Parse the column headers and store them in a list
    headers = [col_head.getText() for col_head in html_table][0].split('\n')[1:4] # Slicers are intended to exclude unnecessary headers

    # Parse the rows and store them in a list
    raw_rows = [col_head.getText() for col_head in html_table][1:21]
    players = []
    for row in raw_rows:
        season = row[:7]
        league = row[7:10]
        player = row[10:].split('(V)')[0]
        players.append([season,league,player])
    
    print("Scraping and Parsing Complete!")         
    
    # Create a pandas DataFrame
    mvp = pd.DataFrame(players, columns=headers)

    # Create a csv file from this DataFrame
    filename = 'nbaMVPs.csv'
    mvp.to_csv(filename,header=True, index=False)
    print("Generated csv file last {}: {}".format(datetime.now(),filename))    
