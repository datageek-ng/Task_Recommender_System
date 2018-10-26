import pandas as pd
import numpy as np
data = pd.read_csv('dataset_v1.csv')
data_copy= data.copy()


data_copy['Refined Percentage'] = data_copy['Completion_rating']/2


#print(data_copy.info())
#print(data_copy.head(5))

#intel


def f(row):
    if row['Type_of_task'] == 'Intellectual':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['Intellectual'] = data_copy.apply(f, axis=1)



def i(row):
    if row['Type_of_task'] == 'Fitness':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['Fitness'] = data_copy.apply(i, axis=1)






#data_copy = data_copy.drop('Percentage of Successful Completion', axis=1)






#morning_data = data_copy.set_index('Start Time').between_time('08:00:00', '11:59:59')

#print(list(morning_data.index))
#for entry in (morning_data.index.tolist()):
#    for i in range(data_copy.size):
#         if (data_copy.iloc[i,4] == entry):
#            data_copy.iloc[i]['Time of the Day'] = "Morning"
# print(morning_data.head())

#coverting according to date time


def a2(row):
    if row['Time_of _the_day'] == 'Early Morning':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['Early Morning'] = data_copy.apply(a2, axis=1)


def a5(row):
    if row['Time_of _the_day'] == 'Evening':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['Evening'] = data_copy.apply(a5, axis=1)

def b1(row):
    if row['Location'] == 'Indoor':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['indoor'] = data_copy.apply(b1, axis=1)

def b2(row):
    if row['Location'] == 'Outdoor':
        val = 1
        return val
    else:
        val=0
        return val
#Then apply it to your dataframe passing in the axis=1 option:
data_copy['outdoor'] = data_copy.apply(b2, axis=1)








def create_multi_period(column):
    data_copy[column+' early-morning'] = (data_copy[column]) & (data_copy['Early Morning'])
    data_copy[column+' morning'] = (data_copy[column]) & (data_copy['Evening'])
    data_copy[column + ' indoor'] = (data_copy[column]) & (data_copy['indoor'])
    data_copy[column + ' outdoor'] = (data_copy[column]) & (data_copy['outdoor'])
create_multi_period('Intellectual')
create_multi_period('Fitness')

corr = data_copy.corr(method='pearson')

print(corr)

corr.to_excel('new.xlsx')

