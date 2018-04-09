import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np



  

    
with open ('/Users/jennifer/Desktop/metis/Project3/Pickle Data/df_all_downsamp.pkl','rb') as picklefile:
    df_all_down_train = pickle.load(picklefile)
y_D = df_all_down_train[['certified']]
# X
X_D = df_all_down_train[df_all_down_train.columns[0:12]]

    

log_model = LogisticRegression(class_weight='balanced',C=.1,penalty='l1')

log_model.fit(X_D,np.ravel(y_D))

mc_model = log_model

def certified_or_denied(prevailing_wage_float,
                            accept_rate_soc_float,
                            total_apps_soc_int,
                            accept_rate_emp_float,
                            total_apps_emp_int,
                            yr_2011_int,
                            yr_2012_int,
                            yr_2013_int,
                            yr_2014_int,
                            yr_2015_int,
                            yr_2016_int,
                            full_time_int,
                        mc_model=mc_model):
    
    input_df = pd.DataFrame({'Prevailing Wage': prevailing_wage_float,
                             'Certified Rate by SOC':accept_rate_soc_float,
                            'Total Petitions by SOC':total_apps_soc_int,
                            'Certified Rate by Employer':accept_rate_emp_float,
                            'Total Petitions by Employer': total_apps_emp_int,
                            'Petition submitted in 2011': yr_2011_int,
                            'Petition submitted in 2012': yr_2012_int,
                            'Petition submitted in 2013': yr_2013_int,
                            'Petition submitted in 2014': yr_2014_int,
                            'Petition submitted in 2015': yr_2015_int,
                            'Petition submitted in 2016': yr_2016_int,
                            'Full Time Position': full_time_int}, index=[0])
                 

    prediction = mc_model.predict(input_df)[0]

    predict_pct1 = str(round(mc_model.predict_proba(input_df)[0][1],4) * 100)
    

    message = ['The petition will likely be denied!','The petition will likely be certified!']

    return message[prediction]


