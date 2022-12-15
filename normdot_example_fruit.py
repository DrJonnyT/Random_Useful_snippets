# -*- coding: utf-8 -"*-
"""
An example of normalised dot product vs Pearson's R, using baskets of fruit
"""

import pandas as pd
import numpy as np

def normdot(X,Y):
    """
    Normalised dot product of two arrays

    Parameters
    ----------
    X : array
        
    Y : array
        

    Returns
    -------
    float

    """
    return np.dot(X,Y) / np.sqrt( np.dot(X,X) * np.dot(Y,Y)   )




fruits = ['apples','bananas','oranges','pears']

basket1 = pd.Series([2,3,0,0],index=fruits)
basket2 = pd.Series([1,2,1,0],index=fruits)
basket3 = pd.Series([0,0,3,3],index=fruits)
basket4 = pd.Series([0,0,3,1],index=fruits)
basket5 = pd.Series([0,0,2,2],index=fruits)

#You would want baskets 1 and 2 to have medium correlation
#Basket 1 and 3&4 to have no correlation, and also the same value
#Baskets 3 and 4 to have very high correlation
#Baskets 3 and 5 to be very similar


Pr_1_2 = basket1.corr(basket2)
Pr_1_3 = basket1.corr(basket3)
Pr_1_4 = basket1.corr(basket4)
Pr_3_5 = basket3.corr(basket5)

normdot_1_2 = normdot(basket1,basket2)
normdot_1_3 = normdot(basket1,basket3)
normdot_1_4 = normdot(basket1,basket4)
normdot_3_5 = normdot(basket3,basket5)
