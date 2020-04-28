# Encephalo Investments Coding Pre-Test - Revised April 2020

import pandas as pd
import numpy as np
import math

def cleanse_data(df):
    # Your task here is to remove data from any ticker that isn't XXY, sort chronologically and return a dataframe
    # whose only column is 'Adj Close'
    df = df.loc[df["Ticker"] == 'XXY']

    df = df.sort_values(by = 'Date')

    df = df.drop(['Date'], axis=1)
    df = df.drop(['Ticker'], axis=1)

    dfclean = df

    return dfclean


def mc_sim(sims, days, df):
    # The code for a crude monte carlo simulation is given below. Your job is to extract the mean expected price
    # on the last day, as well as the 95% confidence interval.
    # Note that the z-score for a 95% confidence interval is 1.960
    returns = df.pct_change()

    last_price = df.iloc[-1]

    last_price = last_price['Adj Close']

    simulation_df = pd.DataFrame()

    price_series_all = []

    for x in range(sims):
        count = 0
        daily_vol = returns.std()

        price_series = []

        price = last_price * (1 + np.random.normal(0, daily_vol))
        price_series.append(price)

        for y in range(days):
            price = price_series[count] * (1 + np.random.normal(0, daily_vol))
            price_series.append(price)
            count += 1


        price_series_all.append(price_series)
        
        simulation_df[x] = price_series

    price_series_all = sorted(price_series_all)
  
    #sample standard deviation
    std_sample = np.std(price_series_all, ddof=1)
    mean_sample = np.mean(price_series_all)
    print(std_sample)
    print(mean_sample)
    
    # confidence_coef = 0.95
    z_score = 1.960

    low_limit = mean_sample - z_score*std_sample
    up_limit = mean_sample + z_score*std_sample
    print('--ping6--')
    print(low_limit)
    print(up_limit)
    print(z_score*std_sample)

    # FILL OUT THE REST OF THE CODE. The above code has given you 'sims' of simulations run 'days' days into the future.
    # Your task is to return the expected price on the last day +/- one standard deviation.
    return



def main():
    filename = '20192020histdata.csv'
    rawdata = pd.read_csv(filename)
    
    cleansed = cleanse_data(rawdata)

    simnum = 2 #len(cleansed)  # change this number to one that you deem appropriate
    days = 25
    mc_sim(simnum, days, cleansed)
    return


if __name__ == '__main__':
    main()
