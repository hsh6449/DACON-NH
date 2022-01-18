# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 23:26:11 2021

@author: yejin
"""
#%%
import FinanceDataReader as fdr
import pandas as pd
import numpy as np
import tqdm
import os

#%% 
stock_df = pd.read_csv('open\\iem_info_20210902.csv')
stock_codes = stock_df['iem_cd']
stock_codes_list = [c[1:] for c in stock_codes]

#%%
non_codes = []
for code in tqdm.tqdm(stock_codes_list):
    if code == '000020':
        df1 = fdr.DataReader(code, start='2016', end='20210731')
        df2 = pd.DataFrame({'A'+code:df1.Close} ,index=df1.index)
        df = df2.T
    
    else:
        df1 = fdr.DataReader(code, start='2016', end='20210731')
        if len(df1) == 0:
            non_codes.append('A'+code)
        else:
            df2 = pd.DataFrame({'A'+code:df1.Close} ,index=df1.index)
            df3 = df2.T
            df = pd.concat([df, df3])

#%%
df.to_csv('stock_close.csv')

#%%
df_non = pd.DataFrame({'non_code':non_codes})
df_non.to_csv("non_codes.csv")