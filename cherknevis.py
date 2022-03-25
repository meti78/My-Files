from sklearn import linear_model
import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np

df = pd.read_csv("D:\Jadi\Machine Learning\house.csv")
df['Area'] = pd.to_numeric(df['Area'], errors='coerce', downcast="float").astype('float64')
#print(df.head())
print(df['Area'][709])