# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 12:27:24 2022

@author: mbcx5jt5

Search within files in a specified directory
Based on the top comment 
https://stackoverflow.com/questions/34530237/find-files-in-a-directory-containing-desired-string-in-python

"""

import os

user_input = r"C:\Work\Python\Github\Orbitrap_Clustering\old_scripts"
directory = os.listdir(user_input)

searchstring = 'import numpy'

for fname in directory:
    print("Trying " + user_input + os.sep + fname)
    if os.path.isfile(user_input + os.sep + fname):
        # Full path
        
        f = open(user_input + os.sep + fname, 'r')

        if searchstring in f.read():
            print('found string in file %s' % fname)
        else:
            print('string not found')
        f.close()