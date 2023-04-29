import numpy as np
import pandas as pd
import random as rm

dict_default=dict(Dataframe=None,Nan_expected=None,column=None)
column=None

while 1:
    Dataframe_location=input('Enter the location of DataFrame: ')
    try:
      Dataframe=pd.read_csv(Dataframe_location)
      break
    except:
      print('Invalid file location :',Dataframe_location,'entered')
      continue
while 1:
    try:
      Nan_expected=float(input('Enter the percentage of nan values required:'))
      break
    except:
      print('Only int and float are valid')
      continue    
while 1:
  column_choice=input('Select a particular column[y/n]: ')
  if column_choice=='y' or column_choice=='Y':
    while 1:
      column=input('Enter the name of the column:')
      try:
        Dataframe[column].unique()
        break
      except:
        print('Please enter the valid column name from the given Dataframe')
        continue
    break   
  elif column_choice=='n' or column_choice=='N':
    break
  else : 
    continue



dict_sorted=dict(Dataframe=Dataframe,Nan_expected=Nan_expected,column=column)
dict_default.update(dict_sorted)

def nan_value_generator(dict_default):
  if column_choice=='y' or column_choice=='Y':
    percent_nan= 100*((Dataframe[column].isnull().sum()) /(Dataframe.shape[0]))
  else :
    percent_nan= 100*((Dataframe.isnull().sum().sum()) /( Dataframe.size))
  print('PROCESSING....')
  while (percent_nan<Nan_expected):
    if column_choice=='n':
      column_num=rm.randint(0,Dataframe.shape[1]-1)
    else:
      column_num=Dataframe.columns.get_loc(column)
    row=rm.randint(0,Dataframe.shape[0]-1)
    Dataframe.iat[row,column_num]=np.nan
    if column_choice=='y' or column_choice=='Y':
      percent_nan= 100*((Dataframe[column].isnull().sum()) /(Dataframe.shape[0]))
    else :
      percent_nan= 100*((Dataframe.isnull().sum().sum()) /( Dataframe.shape[0]*Dataframe.shape[1]))
  Dataframe.to_csv('Generated.csv')
  print("The Required NaN Values been generated in DataFrame and Saved as 'Generated.csv'")
  if column_choice=='y' or column_choice=='Y':
    print("The number of missing values generated are",Dataframe[column].isnull().sum(),"out of",Dataframe.shape[0],'.')
  else :
    print("The number of missing values generated are",Dataframe.isnull().sum().sum(),"out of",Dataframe.shape[0]*Dataframe.shape[1],'.')

nan_value_generator(dict_default)



