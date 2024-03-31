# This script computes weather-history-related image features per image (row of img_file) using the multiprocessing package because create_weather_related_features.py was taking too long.
# For approx 6000 imgs, script ran for about 5 hours. 
# To run: python3 create_weather_related_features_parallelized.py
import pandas as pd
import numpy as np
import datetime
import sys
import multiprocessing as mp
import pickle
import time
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def create_weather_features_for_img(row):
    print(row['donor_date'])
    placement_date = row['date_placed_ARF']
    img_date = row['correct_img_date']

    ADD_thres0 = 0
    ADD_thres5 = 0
    ADD_thres10 = 0
    ADD_thres15 = 0
    ADD_thres20 = 0
    ADD_thres25 = 0
    ADD_thres30 = 0
    '''    
    ADH_thres0 = 0
    ADH_thres5 = 0
    ADH_thres10 = 0
    ADH_thres15 = 0
    '''

    while (placement_date <= img_date):
        # get weather for placement_date
        weather_current_df = weather_df[weather_df.date_time.dt.date == placement_date]
        #print(weather_current_df)

        # calculate ADD with varying temp thresholds
        avg_temp = weather_current_df.loc[:, 'HourlyDryBulbTemperature'].mean()
        if avg_temp >= 0:
            ADD_thres0 += avg_temp
        if avg_temp >= 5:
            ADD_thres5 += avg_temp
        if avg_temp >= 10:
            ADD_thres10 += avg_temp
        if avg_temp >= 15:
            ADD_thres15 += avg_temp
        if avg_temp >= 20:
            ADD_thres20 += avg_temp
        if avg_temp >= 25:
            ADD_thres25 += avg_temp
        if avg_temp >= 30:
            ADD_thres30 += avg_temp
        '''
        # calculate ADH with varying temp thresholds
        total_temp_thres0 = weather_current_df[weather_current_df.HourlyDryBulbTemperature >= 0]['HourlyDryBulbTemperature'].sum()
        ADH_thres0 += total_temp_thres0
        
        total_temp_thres5 = weather_current_df[weather_current_df.HourlyDryBulbTemperature >= 5]['HourlyDryBulbTemperature'].sum()
        ADH_thres5 += total_temp_thres5
        
        total_temp_thres10 = weather_current_df[weather_current_df.HourlyDryBulbTemperature >= 10]['HourlyDryBulbTemperature'].sum()
        ADH_thres10 += total_temp_thres10
        
        total_temp_thres15 = weather_current_df[weather_current_df.HourlyDryBulbTemperature >= 15]['HourlyDryBulbTemperature'].sum()
        ADH_thres15 += total_temp_thres15
        '''
        # go to the next day
        placement_date += datetime.timedelta(days=1)

    # add to dict
    row['ADD_thres0'] = ADD_thres0
    row['ADD_thres5'] = ADD_thres5
    row['ADD_thres10'] = ADD_thres10
    row['ADD_thres15'] = ADD_thres15
    row['ADD_thres20'] = ADD_thres20
    row['ADD_thres25'] = ADD_thres25
    row['ADD_thres30'] = ADD_thres30
    ''' 
    row['ADH_thres0'] = ADH_thres0
    row['ADH_thres5'] = ADH_thres5
    row['ADH_thres10'] = ADH_thres10
    row['ADH_thres15'] = ADH_thres15
    '''
    return row


if __name__=="__main__":
    subset_df = pd.read_pickle('./data/Gelderman_SOD_cohort/unique_donor_date.pkl')
    weather_df = pd.read_pickle('/data/anau/temp_humidity_data/data/LCD/lcd_hourly.pkl')
    print('# of imgs:', subset_df.shape[0])

    subset_dict = subset_df.to_dict('records')
    starttime = time.time()
    p = mp.Pool()
    result_ls = p.map(create_weather_features_for_img, subset_dict)
    p.close()
    p.join()
    endtime = time.time()
    print(f"Time taken {endtime-starttime} seconds")
    
    with open('./data/Gelderman_SOD_cohort/unique_donor_date_w_ADD.pkl', 'wb') as f:
        pickle.dump(result_ls, f)

