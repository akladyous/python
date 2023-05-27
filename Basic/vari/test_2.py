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

# x          = df_features.drop(labels='price', axis=1)
# y          = df_features['price']
# x_constant = sm.add_constant(x)
# model      = sm.OLS(y,x_constant).fit()
# print(str(model.summary()))

df_model = pd.concat([df_features, df_categories], axis= 1)
x = df_model.drop(labels='price', axis=1)
y = df_model['price']

# x_constant = sm.add_constant(x)
# model      = sm.OLS(y,x_constant).fit()
# print(str(model.summary()))




def stepwise_selection(X, y,
                       initial_list=[],
                       threshold_in=0.01,
                       threshold_out = 0.05,
                       verbose=True):
    """ Perform a forward-backward feature selection
    based on p-value from statsmodels.api.OLS
    Arguments:
        X - pandas.DataFrame with candidate features
        y - list-like with the target
        initial_list - list of features to start with (column names of X)
        threshold_in - include a feature if its p-value < threshold_in
        threshold_out - exclude a feature if its p-value > threshold_out
        verbose - whether to print the sequence of inclusions and exclusions
    Returns: list of selected features
    Always set threshold_in < threshold_out to avoid infinite looping.
    See https://en.wikipedia.org/wiki/Stepwise_regression for the details
    """
    included = list(initial_list)
    while True:
        changed=False
        # forward step
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded, dtype='float64')
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True
            if verbose:
                print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        # backward step
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            # worst_feature = pvalues.argmax()
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included

result = stepwise_selection(x, y, verbose=True)
print(result)
