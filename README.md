# NBA_MVP_Prediction_Model

### Quick Steps:
1. Run first the `datasetFactory.py` to generate the csv files
2. Then run `randForest.py` to run predictions
Note: Recommended IDE is Spyder due to many built in libraries that may not be available when running just IDLE

The objective of the predictive model is to return a number of players from the current season that have the highest potential to be the next MVP using statistics from years 2000 to 2019 as the training dataset.

This repository initially contains the following files
1. NBA MVP Prediction Model - Notes.ipynb --> This notebook is where I plan everything from pseudo code to final code before I paste them to the respective python files: `datasetFactory.py`, `nbaPlayers_StatsScraper.py`,`randForest.py`

2. `nbaPlayers_StatsScraper.py` --> A module containing two methods for webscraping data
3. `datasetFactory.py` --> Running this generates csv files of webscraped data from https://www.basketball-reference.com/
4. `randForest.py` --> Contains the Machine Learning Model.

Before running the `datasetFactory.py`, it's best to read and test the codes from the notebook for complete familiarization.
Open this first `NBA MVP Prediction Model - Notes.ipynb` using the Jupyter Notebook.

This notebook contains these 4 major parts:

## 1. Webscraping for Data

Methods from `nbaPlayers_StatsScraper.py` module:

`scrapeNBAStats(year)`
`scrapeMVPs()`

## 2. Preparation of Dataset/s

Running `datasetFactory.py` delivers these outputs:
1. csv files of NBA Players Statistics Per Game for every season (1999-00 to 2018-19)
2. `training_data.csv`
3. `nbaMVPs.csv'

## 3. Building the Machine Learning Model
Run `randForest.py`

The script shall perform these main steps:

a. PREPARE data - creating DataFrames and pre-processing

b. DEFINE model - choose model and instantiate

c. FIT model - train the model

d. PREDICT - Create a dataframe for the stats of current season.
   
   As of this time, the current season is 2019-20.

e. EVALUATE - using mean absolute error

f. RESULTS - display top 10 potential MVPs
