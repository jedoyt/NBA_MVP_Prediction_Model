# NBA_MVP_Prediction_Model

### Requirements/Dependencies:
1. Have Anaconda installed in your system: https://www.anaconda.com/distribution/
   - I recommend using Spyder(included in Anaconda Distribution) for the running the python scripts.
   - You can run Spyder through Anaconda Navigator or through terminal by typing 'Spyder' then press Enter.
2. Make sure the following modules/packages are available:
   - numpy, pandas, requests, BeautifulSoup4, datetime, sklearn (All of these are built-in packages in Anaconda)

### Quick Steps:
1. Run first the `datasetFactory.py` to generate the csv files
2. Then run `randForest.py` to run predictions
Note: Recommended IDE is Spyder(from Anaconda Distribution) due to many built in libraries that may not be available when running just IDLE the comes with the typical Python installer.

The objective of the predictive model is to return a number of players from the current season that have the highest potential to be the next MVP using statistics from years 1957 to 2019 as the training dataset.

This repository initially contains the following files
1. `NBA MVP Prediction Model - Notes.ipynb` --> This notebook is where I plan everything from pseudo code to final code before I paste them to the respective python files: `datasetFactory.py`, `nbaPlayers_StatsScraper.py`,`randForest.py`

2. `nbaPlayers_StatsScraper.py` --> A module containing two methods for webscraping data https://www.basketball-reference.com/
3. `datasetFactory.py` --> Running this generates csv files of webscraped data from https://www.basketball-reference.com/
4. `randForest.py` --> Contains the Machine Learning Model. Now currently using Random Forest Regression. But I might consider another model that is more applicable.

The notebook, `NBA MVP Prediction Model - Notes.ipynb`, elaborates these 4 major steps:

## 1. Webscraping for Data

Methods from `nbaPlayers_StatsScraper.py` module:

`scrapeNBAStats(year,type)`
`scrapeMVPs()`

## 2. Preparation of Dataset/s

Running `datasetFactory.py` delivers these outputs:
1. csv files of NBA Players Statistics Per Game for every season (1956-57 to 2018-19)
2. `training_data.csv`
3. `nbaMVPs.csv`

## 3. Building the Machine Learning Model
Running `randForest.py` delivers these csv outputs:
1. `mvpTop10candidates.csv`
2. `CompletePredictions.csv`

The script shall perform these main steps:

a. PREPARE data - creating DataFrames and pre-processing

b. DEFINE model - choose model and instantiate

c. FIT model - train the model

d. PREDICT - Create a dataframe for the stats of current season.
   
   As of this time, the current season is 2019-20.

e. EVALUATE - using mean absolute error (only shown in the .ipynb file)

f. RESULTS - display top 10 potential MVPs
