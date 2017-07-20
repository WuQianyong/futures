#!/usr/bin/env Python3
# -*- coding: utf-8 -*-
# 
# Name   : pickle_demo
# Fatures:
# Author : qianyong
# Time   : 2017-06-09 09:16
# Version: V0.0.1
#

import sys, os
import pickle
pickle_file = r'E:\susheng\riskmanage\fail_company.pkl'

# f = open(pickle_file,'wb')
# c = [1,2,4]
# pickle.dump(c,f)
# f.close()

ff = open(pickle_file,'rb')
a = pickle.load(ff)

print(a,type(a))
ff.close()
for item in a.items():
    print(item[0],len(item[1]))

print(pickle_file)
