import pandas as pd
import numpy as np


df = pd.read_csv(r'./healthcare-dataset-stroke-data.csv', index_col='id')


for idx in list(df.index):

    gender = df.loc[idx, 'gender']
    ever_married = df.loc[idx, 'ever_married']
    work_type = df.loc[idx, 'work_type']
    residence_type = df.loc[idx, 'Residence_type']
    smoking_status = df.loc[idx, 'smoking_status']
    bmi = df.loc[idx, 'bmi']
    if gender == 'Male':
        df.loc[idx, 'gender'] = 0
    if gender == 'Female':
        df.loc[idx, 'gender'] = 1
    if gender == 'Other':
        df.loc[idx, 'gender'] = 2

    if ever_married == 'Yes':
        df.loc[idx, 'ever_married'] = 1
    if ever_married == 'No':
        df.loc[idx, 'ever_married'] = 0

    if work_type == 'children':
        df.loc[idx, 'work_type'] = 1
    if work_type == 'Govt_job':
        df.loc[idx, 'work_type'] = 2
    if work_type == 'Never_worked':
        df.loc[idx, 'work_type'] = 3
    if work_type == 'Private':
        df.loc[idx, 'work_type'] = 4
    if work_type == 'Self-employed':
        df.loc[idx, 'work_type'] = 5

    if residence_type == 'Rural':
        df.loc[idx, 'Residence_type'] = 0
    if residence_type == 'Urban':
        df.loc[idx, 'Residence_type'] = 1

    if np.isnan(bmi):
        df.loc[idx, 'bmi'] = -1

    if smoking_status == 'formerly smoked':
        df.loc[idx, 'smoking_status'] = 0
    if smoking_status == 'never smoked':
        df.loc[idx, 'smoking_status'] = 1
    if smoking_status == 'smokes':
        df.loc[idx, 'smoking_status'] = 2
    if smoking_status == 'Unknown':
        df.loc[idx, 'smoking_status'] = 3

df.to_csv(path_or_buf=r'./healthcare-dataset-stroke-data-adapter.csv', header=None)
