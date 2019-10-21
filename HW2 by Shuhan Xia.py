#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 10:34:55 2019

@author: xiapeter
"""

import pandas as pd

def read(url):
    data = pd.read_csv("url")
    return data

def test_create_dataframe(dataframe,col_list):
    if list(dataframe.columns)==col_list and len(set(dataframe.dtypes))==1 and dataframe.shape[0]>=10:
        return True
    return False