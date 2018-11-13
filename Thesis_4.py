import pandas as pd
import numpy as np
from sklearn.metrics import matthews_corrcoef
import openpyxl
data = pd.read_csv('test_1.csv')
def tasktype_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Type_of_task.values == tasktype, 1, 0),
          data.index)
tasktype_convert('intellectual')
tasktype_convert('chores')
tasktype_convert('social')
tasktype_convert('errands')
tasktype_convert('fitness')
tasktype_convert('physical')
tasktype_convert('Spiritual')
task_type = ['intellectual', 'chores', 'social', 'errands', 'fitness', 'physical', 'Spiritual']
def task_duration_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Task_Duration.values == tasktype, 1, 0),
          data.index)
task_duration_convert('very long')
task_duration_convert('short')
task_duration_convert('long')
task_duration_convert('very short')
def task_location_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Location.values == tasktype, 1, 0),
          data.index)
task_location_convert('indoor')
task_location_convert('outdoor')
def task_day_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Weekday.values == tasktype, 1, 0),
          data.index)
task_day_convert('Saturday')
task_day_convert('Sunday')
task_day_convert('Monday')
task_day_convert('Tuesday')
task_day_convert('Wednesday')
task_day_convert('Thursday')
task_day_convert('Friday')


def task_time_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Time_of_the_day.values == tasktype, 1, 0),
          data.index)
task_time_convert('Early Morning')
task_time_convert('Morning')
task_time_convert('Afternoon')
task_time_convert('Evening')
task_time_convert('Night')
task_time_convert('Midnight')
task_time = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Midnight']

for i in task_type:
    for j in task_time:
        data[str(i)+"_"+str(j)] = (np.logical_and(data[str(i)], data[str(j)])).astype(int)

def rating_convert(tasktype, value):
    data[tasktype] = pd.Series(np.where(data.Completion_rating.values == value, 1, 0),
          data.index)
rating_convert('very_low', 1)
rating_convert('low', 2)
rating_convert('medium', 3)
rating_convert('high', 4)
rating_convert('very_high', 5)
rating=[1,2,3,4,5]



#data.Completion_rating = pd.Categorical(data.Completion_rating, categories = [1,2,3,4,5], ordered = True)
#print(data.Completion_rating)
print(matthews_corrcoef(data.intellectual, data.very_high))
import heapq
def Schedule_v2():
    print('Weekly Plan')
    task_type = ['intellectual', 'chores', 'social', 'errands', 'fitness', 'physical', 'Spiritual']
    task_time = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Midnight']
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    v2_result = pd.DataFrame()
    for i in days:
        for j in task_time:
            #print(data[(data['Time_of_the_day'] == j) & (data['Weekday'] == i)])
            data2 = data[(data['Time_of_the_day'] == j) & (data['Weekday'] == i)]
            # print(type(data2))
            rank_score = []
            for k in task_type:
                      rank_score.append(((matthews_corrcoef(data2[k], data2.very_high))*3 + (matthews_corrcoef(data2[k], data2.high))*2 + (matthews_corrcoef(data2[k], data2.medium))) / 6)
            #print(rank_score)
            max_2 = heapq.nlargest(2, enumerate(rank_score), key=lambda x: x[1])
            #print(max_2)
            #print(max_2[0][0], max_2[1][0])
            #print(i,j,task_type[max_2[0][0]], task_type[max_2[1][0]])

            v2_result.loc[i, j] = str("1. "+task_type[max_2[0][0]]+"  2. "+task_type[max_2[1][0]])
            # print(str(corr2_res.idxmax(axis=1)).replace('Completion_rating    ', ''))
    print(v2_result)
    v2_result.to_excel('final_result.xlsx')
Schedule_v2()
