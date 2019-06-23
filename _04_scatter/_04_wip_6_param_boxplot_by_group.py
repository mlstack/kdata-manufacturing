#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Boxplot Chart
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Boxplot Chart for FDC Parameters 
"""
# %matplotlib inline

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import pandas as pd


df =pd.read_csv("WIP_HISTORY.csv")
# print(df.columns)
# Index(['TARGET_VALUE', 'GOOD_BAD', 'LINE', 'EQUIPMENT', 'GAS_PRESSURE',
       # 'TEMPERATURE', 'THICKNESS', 'WAITING_TIME', 'PROCESS_TIME', 'INTENSITY',
       # 'RPM', 'TIME_GAP', 'SPEED']
# df = df[['TARGET_VALUE','GAS_PRESSURE', 'TEMPERATURE', 'THICKNESS','WAITING_TIME','PROCESS_TIME','INTENSITY','RPM','TIME_GAP','SPEED']]


df.boxplot(column=['PROCESS_TIME'], by='GOOD_BAD')
plt.show()
