# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 01:14:04 2021

@author: yejin
"""

#%%
import pandas as pd
import numpy as np
from tqdm import tqdm
import os

#%%
stock_close = pd.read_csv('stock_close.csv')
stock_close_re = stock_close.rename(columns={'Unnamed: 0' : 'code'})
stock_close_index = stock_close_re.set_index('code')
col_re = [c.replace('-', '') for c in list(stock_close_index.columns)]
stock_close_index.columns = col_re
df_stock_close = stock_close_index

#%%
stock_df = pd.read_csv('G:/dacon/NH/stk_hld_test.csv')
stock_df['close'] = np.zeros(shape=(stock_df.shape[0], 1))

#%%
err = []
for i in tqdm(range(len(stock_df))):
    code = stock_df.loc[i, "iem_cd"]
    date = stock_df.loc[i, "byn_dt"]

    try:
        stock_df.loc[i, "close"] = df_stock_close.loc[code, str(date)]
    except:
        err.append(code)
        
#%%
stock_df.to_csv('test_close.csv')


#%% save_err
df_non = pd.DataFrame({'non_code':err})
df_non.to_csv("non_merge.csv")