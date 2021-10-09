# Vix Predictor Functions

import pandas as pd
from arch import arch_model
import yfinance as yf
from datetime import datetime
import numpy as np


def garch_fit_and_predict(series, horizon=1, p=1, q=1, o=1):
    #p=1,q=1, o=1 
    #series=returns_df['spy']
    #horizon=1
    
    """
    This function takes a series of returns, and get back a series of conditional volatility
    modeled using a GJR-GARCH with one shock, and t-student distribution of errors that accepts a skew.
    
    In the NN model X is shifted in one lag to be able to predict.
    This GARCH series is the GARCH prediction for the volatility of r series that goes in paralell.
    Once X shift, we want to have (r_{t-1})^2 in one column, and the garch_prediction_t in another. 
    This way we are going to include the ARCH prediction to the model.
    If I think that I need to put e_{t-1}^2 together with garch_prediction_{t-1} I am wrong. Please think again.
    """

    series=series.dropna()
    shock_skew_gm_model=arch_model(
                    100*series, 
                    p=p, q=q, o=o,
                    mean='constant',
                    vol='GARCH',
                    dist='skewt'
    )
    #Fit GARCH model and predict
    results_shock_skew_gm=shock_skew_gm_model.fit(update_freq=0, disp="off")

    conditional_volatility=results_shock_skew_gm.conditional_volatility
    #summary               =results_shock_skew_gm.summary()
    forecast              =results_shock_skew_gm.forecast(horizon=1, reindex=False)

    # Prepare return of the series ready to include to X before shift
    serie_garch_before_shift=conditional_volatility.shift(-1)
    serie_garch_before_shift.iloc[-1,:]=forecast.variance.iloc[-1]

    return serie_garch_before_shift/100


def correlation_filter(series, min_corr=0.20, key_column='^VIX', eliminate_first_column=False):

    key_correlations=series.corr()[key_column]
    to_keep_columns=key_correlations[abs(key_correlations)>=min_corr].index
    filtered_series=series[to_keep_columns]
    
    if eliminate_first_column==True:
        filtered_series=filtered_series.iloc[:,1:]
    

    return filtered_series


def retrieve_yahoo_close(ticker = 'spy', start_date = '2007-07-02', end_date = '2021-10-01'):
    try:
        # get data based on ticker
        yahoo_data = yf.Ticker(ticker)
        print(f"Processing Close {ticker}")
        # select data using start date and end data and calculate the daily return
        price_df = yahoo_data.history(start=start_date, end=end_date).Close
        price_df.name = ticker
        # if no data retrieved raise exception
        if price_df.shape[0] == 0:
            raise Exception("No Prices.")
        return price_df
    # handle exception
    except Exception as ex:
        print(f"Sorry, Data not available for '{ticker}': Exception is {ex}")

        
# Define function to retrieve daily volume data from yahoo using ticker, start date and end date
def retrieve_yahoo_volume(ticker = 'spy', start_date = '2007-07-02', end_date = '2021-10-01'):
    try:
        # get data based on ticker
        yahoo_data = yf.Ticker(ticker)
        print(f"Processing Volume {ticker}")
        # select data using start date and end data and calculate the daily return
        price_df = yahoo_data.history(start=start_date, end=end_date).Volume
        price_df.name = ticker
        # if no data retrieved raise exception
        if price_df.shape[0] == 0:
            raise Exception("No Prices.")
        return price_df
    # handle exception
    except Exception as ex:
        print(f"Sorry, Data not available for '{ticker}': Exception is {ex}")

# Define function to retrieve put daily volume data from yahoo using ticker, start date and end date
def retrieve_yahoo_put_options_volume(ticker = 'spy', date = '2004-01-01'):
    try:
        # get data based on ticker
        yahoo_data = yf.Ticker(ticker)
        print(f"Processing put volume from {ticker}")
        # select data using start date and end data and calculate the daily return
        opts = yahoo_data.option_chain()
        price_df = opts.puts
        price_df.name = ticker
        price_df = price_df.volume
        # if no data retrieved raise exception
        if price_df.shape[0] == 0:
            raise Exception("No Prices.")
        return price_df
    # handle exception
    except Exception as ex:
        print(f"Sorry, Data not available for '{ticker}': Exception is {ex}")