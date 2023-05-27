import itertools
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', 50)
import matplotlib.pyplot as plt

from geopy import distance

from scipy import stats
from scipy.stats import norm
import seaborn as sns

import statsmodels.api as sm
from statsmodels.formula.api import ols
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.preprocessing import FunctionTransformer, scale, StandardScaler, MinMaxScaler, StandardScaler, Normalizer
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("/Users/boula/Documents/GitHub/Public/house-price-prediction/data/kc_house_data.gz", index_col=None)

for i in df.columns:
    total_nan = df[i].isnull().sum()
    if total_nan > 0:
        print("total missing value of {0:<15}  is: {1:>5}".format(i, total_nan))
del total_nan


df['waterfront'].fillna(value=0, axis=0, inplace=True)
df['view'].fillna(value=0, axis=0, inplace=True)

df['yr_renovated'].fillna(value=0, axis=0, inplace=True)
df.loc[df['yr_renovated']!=0, ['yr_renovated']] = 1
df.loc[:,'yr_renovated'] = df['yr_renovated'].apply(np.int)  #.astype('int')
df.rename(columns={'yr_renovated': 'renovated'}, inplace=True)

un_named_columns = df.iloc[:,df.columns.str.contains('^Unnamed', case=False, regex=True)]
df.drop(un_named_columns, axis=1, inplace=True)

df.drop(columns=['id'], inplace=True)
df['date'] = pd.to_datetime(df['date'], utc=False)

var_excluded = set()
var_excluded.add(('view'))
var_excluded.update(('sqft_above', 'sqft_basement'))
var_excluded.update(('lat','long', 'zipcode', 'bedrooms', 'bathrooms','date'))

var_predictors = set(df.columns)-var_excluded

lat_long=[(x,y) for x,y in zip(df['lat'], df['long'])]
kc = (47.6062, -122.3321) # king county usa downtown lat long
miles = [round(distance.distance(i, kc).miles,1) for i in lat_long ]
df['distance'] = miles
var_predictors.add(('distance'))

var_categories =  {'condition', 'waterfront', 'floors', 'renovated', 'yr_built'}

yr_built_bins = [1900,1923,1946,1969,1992,2015]
yr_built_labels = ['1900_1923','1924_1946','1947_1969','1970_1992','1993_2015']
yr_built_cat = pd.cut(x=df['yr_built'], bins=yr_built_bins, labels=yr_built_labels, include_lowest=True)
df['yr_built'] = yr_built_cat.cat.as_unordered()

df.condition=df.condition.astype(int)
df.waterfront=df.waterfront.astype(int)
df.floors=df.floors.astype(int)
df.renovated=df.renovated.astype(int)
df.grade=df.grade.astype(int)

#create a dummy data by removing redundant columns when using get_dummies
df_categories = pd.DataFrame()

for cat in var_categories:
    df_categories[cat]=df[cat].astype('category')
    df_dummy = pd.get_dummies(df_categories[cat], prefix=cat, drop_first=True) 
    df_categories = df_categories.join(df_dummy)
    df_categories.drop(labels=cat, axis=1, inplace=True)

df_features = pd.DataFrame(df[var_predictors-var_categories])

price_scaled = StandardScaler().fit_transform(df_features['price'].values.reshape(-1,1))

for col in df_features.columns.difference(['price']):
    df_features[col] = StandardScaler().fit_transform(df_features[col].values.reshape(-1,1))

x          = df_features.drop(labels='price', axis=1)
y          = df_features['price']
x_constant = sm.add_constant(x)
model      = sm.OLS(y,x_constant).fit()
print(str(model.summary()))

df_model = pd.concat([df_features, df_categories], axis= 1)
x = df_model.drop(labels='price', axis=1)
y = df_model['price']
x_constant = sm.add_constant(x)
model      = sm.OLS(y,x_constant).fit()
print(str(model.summary()))




def StepWise(df:'dataframe',
                y:'Target (column name)',
                intial_list = [], 
                excluded_list = [],
                threshold_in. = 0.01, 
                threshold_out = 0.05, 
                verbose=True):
    
    
    included = list(initial_list)
    features = y.columns

    excluded = set(x.columns)-set(included)
    pvalue = dict()
    for column in x.columns:
        pd.DataFrame(column+)
        model = sm.OLS(y, sm.add_constant(df[excluded+column]))