# NBA_MVP_Prediction_Model
The objective of the predictive model is to return a number of players from the current season that have the highest potential to be the next MVP using statistics from years 2000 to 2018 as the training dataset.

This repository initially contains the following files
1. NBA MVP Prediction Model - Notes.ipynb --> This notebook is where I plan everything from pseudo code to final code before I    paste them to the respective python files: `datasetFactory.py`, `nbaPlayers_StatsScraper.py`,`model.py`

2. nbaPlayers_StatsScraper.py --> A module containing two methods for webscraping data
3. datasetFactory.py --> Running this generates csv files of webscraped data from https://www.basketball-reference.com/
4. model.py --> Contains the Machine Learning Model. Not yet available for now. Once available this the next program to run after datasetFactory.py and would finally generate the predictions

Before running the datasetFactory.py, it's best to read and test the codes from the notebook for complete familiarization.
Open this first `NBA MVP Prediction Model - Notes.ipynb` using the Jupyter Notebook.

This notebook contains these 4 major parts:

## 1. Webscraping for Data

Methods from `nbaPlayers_StatsScraper.py` module:

`scrapeNBAStats(year)`
`scrapeMVPs()`

## 2. Preparation of Dataset/s

Running `datasetFactory.py` delivers this output:

`training_data.csv`


## 3. Building the Machine Learning Model

Not available yet but shall follow these main steps:

a. PREPARE data - creating DataFrames and data cleansing

b. DEFINE model - choose model and instantiate

c. FIT model - train the model

d. PREDICT

e. EVALUATE - using mean absolute error
