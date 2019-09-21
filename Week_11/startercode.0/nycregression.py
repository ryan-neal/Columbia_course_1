import numpy as np
import pandas as pd
from sklearn import datasets, linear_model

# Question 1: transforming the data
def filter_nyc():
    df = pd.read_csv('nyc.csv',header=0)

    # Your work here
    
    # Helping code for agency:
    #
    # agency_num = {}
    # for num, agency in enumerate((df['Agency'].unique())): 
    #     agency_num[agency] = num
    # df['agency_num'] = df['Agency'].apply(lambda x: agency_num[x])

    
    df.to_csv('filtered.csv',index=False)
    
# Question 2: build the model and predict
def build_and_predict():
    #data = pd.read_csv('filtered.csv')
    #test = pd.read_csv('topredict.csv')
    
    # Your work here
    
    # yourDF.to_csv('predictions.csv',index=True,index_label='index') (you can change this line if you want)
    