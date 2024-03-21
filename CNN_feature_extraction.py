# This script perform CNN feature extraction using the Gelderman SOD classification models.
# To run: python3 CNN_feature_extraction.py
# Prior to running, modify model and image file paths where indicated.
# This script outputs a pickle file containing a dictionary with key-value pairs img:img_embedding (numpy array)
import cv2
import numpy as np
from tensorflow.keras.models import load_model
import csv
import sys
import os
from tensorflow.keras.preprocessing import image
import pandas as pd
import tensorflow as tf
import pickle
import random

# define CNN feature extractor model
#model_name = '/data/anau/SOD_classification_G/models/head/xception_070523'  ### modify ###
#model_name = '/data/anau/SOD_classification_G/models/torso/xception_070723'  ### modify ###
model_name = '/data/anau/SOD_classification_G/models/limbs/xception_071323'  ### modify ###
model_type = 'xception'  ## modify
model = load_model(model_name)
# remove last layer of model
x = model.layers[-2].output 
model2 = tf.keras.Model(inputs = model.input, outputs = x)

# import data where each row is: img_img
data_df = pd.read_csv('./data/Gelderman_SOD_cohort/limbs_imgs.csv', header=None)  ### modify ###
data_df.columns = ['img']

# function to generate embeddings
def gen_embeddings(df):
    not_found = 0
   
    img_emb_dict = {}
    counter = 1
    for ind in df.index:
        img_data = []
        print(counter,  df['img'][ind])
        img_path = '/da1_data/icputrd/arf/mean.js/public/anau_img3/' + df['img'][ind][:3] + '/' + df['img'][ind] 
        try:
            if model_type == 'xception':
                img = image.load_img(img_path,
                        target_size = (299, 299, 3),
                        grayscale = False)
            img = image.img_to_array(img)
            img = img/255
            img_data.append(img)
            img_data_arr = np.array(img_data)

            prediction = model2.predict(img_data_arr)
            img_emb_dict[df['img'][ind]] = prediction
        except:
            not_found += 1
            img_emb_dict[df['img'][ind]] = ''
        
        counter += 1
        
    print('Number of imgs not found:', not_found) 
    return img_emb_dict

# generate embeddings
img_emb_dict = gen_embeddings(data_df)
with open('/data/anau/PMI_estimation/data/Gelderman_SOD_cohort/embeddings/limbs_img_emb_dict', 'wb') as f:  ### modify ####
    pickle.dump(img_emb_dict, f)


