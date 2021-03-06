excel_files = ['water_data2015.xlsx', 'water_data2016.xlsx', 'water_data2017.xlsx']

# dataset attributes
attributes = ['Time', 
                'RW-Temp','RW-Ni','RW-CD','RW-pH', 'RW-TB', 
                'RW-DO','RW-AN','RW-Mn','RW-COD', 
                'Enter Water-1','Enter Water-2','Enter Water-3','Enter Water-4', 
                'Al Dosage-1','Al Dosage-2','Al Dosage-3','Al Dosage-4', 
                'SW-TB-1','SW-TB-2','SW-TB-3','SW-TB-4',
                'PC-TB-1','SW-DO-1','SW-COD-1','SW-AN-1', 
                'PC-TB-2','SW-DO-2','SW-COD-2','SW-AN-2', 
                'C-TB-1','C-pH-1','C-DO-1','C-COD-1','C-AN-1','C-RC-1', #36
                'C-TB-2','C-pH-2','C-DO-2','C-COD-2','C-AN-2','C-RC-2', #42
                'S-TB-1','S-TB-2','S-RC-1','S-RC-2', #46
                'F-TB-1','F-TB-2','F-RC-1','F-RC-2','F-pH-1','F-pH-2'] #52

cor_attributes = ['Time', 'OD', 
                  'RW-Ni','RW-CD','RW-pH','RW-TB','RW-DO','RW-AN','RW-Mn','RW-COD',
                  'SW-TB1', 'SW-TB2', 'SW-DO', 'SW-COD', 'SW-AN',
                  'C-TB', 'C-pH', 'C-DO', 'C-COD', 'C-AN', 'C-RC',
                  'S-TB', 'S-RC',
                  'F-TB', 'F-RC', 'F-pH']

cor_time = [['2016-07-04 00:00:00','2016-08-01 00:00:00']]


experiments = {
 
#  Train:3; 4 Test: 5  
'spring': {'times':
               ([('2016-03-01 00:00:00','2016-04-01 00:00:00'),
                 ('2016-04-01 00:00:00','2016-05-01 00:00:00')],
                [('2016-05-01 00:00:00','2016-06-01 00:00:00')]),
           'normalize': [0],
           'clustering': [0],
           'lag_time': [2, 3, 8, 10, 12, 14],
            },

#  Train:6; 7 Test: 8      
'summer': {'times':
               ([('2016-06-01 00:00:00','2016-07-01 00:00:00'),
                 ('2016-07-01 00:00:00','2016-08-01 00:00:00')],
                [('2016-08-01 00:00:00','2016-09-01 00:00:00')]),
           'normalize': [0],
           'clustering': [0],
           'lag_time': [2, 3, 8, 10, 12, 14],
           
          },
    
#  Train:9; 7 Test: 10      
'autumn': {'times':
               ([('2016-03-01 00:00:00','2016-04-01 00:00:00'),
                 ('2016-04-01 00:00:00','2016-05-01 00:00:00')],
                [('2016-05-01 00:00:00','2016-06-01 00:00:00')]),           
           
               ([('2016-09-01 00:00:00','2016-10-01 00:00:00'),
                 ('2016-10-01 00:00:00','2016-11-01 00:00:00')],
                [('2016-11-01 00:00:00','2016-12-01 00:00:00')]),
           'normalize': [0],
           'clustering': [0],
           'lag_time': [3, 5, 8, 9, 10, 12],
           
          },
           
#  Train:12-1; 1-2 Test: 2-3                   
'winter': {'times':
               ([('2015-12-01 00:00:00','2016-01-01 00:00:00'),
                 ('2016-01-01 00:00:00','2016-02-01 00:00:00')],
                [('2016-02-01 00:00:00','2016-03-01 00:00:00')]),
           'normalize': [0],
           'clustering': [0],
           'lag_time': [2,3,8,11,12,14],
           
          },
           
#  Train:15.12-16.8; Test: 16.8-16.11       
'all_year': {'times':
                ([('2015-12-01 00:00:00','2016-01-01 00:00:00'),
                  ('2016-01-01 00:00:00','2016-02-01 00:00:00'),
                  ('2016-02-01 00:00:00','2016-03-01 00:00:00'),
                  ('2016-03-01 00:00:00','2016-04-01 00:00:00'),
                  ('2016-04-01 00:00:00','2016-05-01 00:00:00'),
                  ('2016-05-01 00:00:00','2016-06-01 00:00:00'),
                  ('2016-06-01 00:00:00','2016-07-01 00:00:00'),
                  ('2016-07-01 00:00:00','2016-08-01 00:00:00')
                  ],
                 [('2016-08-01 00:00:00','2016-09-01 00:00:00'),
                  ('2016-09-01 00:00:00','2016-10-01 00:00:00'),
                  ('2016-10-01 00:00:00','2016-11-01 00:00:00'),
                  ('2016-11-01 00:00:00','2016-12-01 00:00:00'),
                  ]),
             'normalize': [0],
             'clustering': [0],
             'lag_time': [10],
            },

#  Train:15.4-6.; Test: 16.4       
'cross_year' : {'times':
                   ([('2015-04-01 00:00:00','2015-07-01 00:00:00')],
                    [('2016-04-01 00:00:00','2016-05-01 00:00:00')]),
                'normalize': [0],
                'clustering': [0],
                'lag_time': [3],
               },
    
    
'new2old' : {'times':
                 ([('2017-01-01 00:00:00','2017-05-01 00:00:00')],
                  [('2015-12-01 00:00:00','2016-01-01 00:00:00'),
                   ('2016-02-01 00:00:00','2016-03-01 00:00:00'),
                   ('2016-03-01 00:00:00','2016-04-01 00:00:00'),
                   ('2016-05-01 00:00:00','2016-06-01 00:00:00'),
                   ('2016-06-01 00:00:00','2016-07-01 00:00:00'),
                   ('2016-08-01 00:00:00','2016-09-01 00:00:00'),
                   ('2016-09-01 00:00:00','2016-10-01 00:00:00'),
                   ('2016-11-01 00:00:00','2016-12-01 00:00:00')]),
             'normalize': [0],
             'clustering': [0],
             'lag_time': [10],
            },

'old2new' : {'times':
                 ([('2015-12-01 00:00:00','2016-01-01 00:00:00'),
                   ('2016-01-01 00:00:00','2016-02-01 00:00:00'),
                   ('2016-02-01 00:00:00','2016-03-01 00:00:00'),
                   ('2016-03-01 00:00:00','2016-04-01 00:00:00'),
                   ('2016-04-01 00:00:00','2016-05-01 00:00:00'),
                   ('2016-05-01 00:00:00','2016-06-01 00:00:00'),
                   ('2016-06-01 00:00:00','2016-07-01 00:00:00'),
                   ('2016-07-01 00:00:00','2016-08-01 00:00:00')],
                  [('2017-05-01 00:00:00','2017-10-01 00:00:00')]),
             'normalize': [0],
             'clustering': [0],
             'lag_time': [10],
            },
}

"""
***previous → future***
"""

repeat_num = 50

path = '/mnt/pami/yqliu/water_13/'

# Features
features = ['RW-Ni','RW-CD','RW-pH','RW-TB','RW-DO', 'SW-TB', 'SW-DO', 'C-TB']

labels = ['Time', 'OD']


 
# 14 models

methods = ['AATC-LSTM', 'TC-LSTM', 'TC-TCN', 'LSTM', 'TENlar', 'ENlar', 'ridge_regression', 'lasso', 'mlr', 'xgboost','lightgbm', 'random_forest', 'mlp', 'nn', 'anfis']   


# 4 metrics
metrics = ['rmse', 'mape', 'correlation', 'wi']
