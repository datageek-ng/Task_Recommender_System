import pandas as pd
import numpy as np
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


#print(data)
data.to_excel('new2.xlsx')

corr = data.corr(method='pearson')

#print(corr)

corr.to_excel('new.xlsx')


def Schedule_v1():
    task_type = ['intellectual', 'chores', 'social', 'errands', 'fitness', 'physical', 'Spiritual']
    task_time = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Midnight']
    type_time = []
    type_time_type = []
    for i in task_type:
        for j in task_time:
            type_time.append(str(i) + "_" + str(j))
            type_time_type.append(i)
    print('Day Plan V1')
    for j in task_time:
        a = {}
        for i in task_type:
            a[str(i) + "_" + str(j)] = corr.loc[str(i) + "_" + str(j), 'Completion_rating']

        # print(a)
        def keywithmaxval(d):
            """ a) create a list of the dict's keys and values;
                b) return the key with the max value"""
            v = list(d.values())
            k = list(d.keys())
            return k[v.index(max(v))]

        print(str(j) + ' : ' + str(type_time_type[type_time.index(keywithmaxval(a))]))

Schedule_v1()


def Schedule_v2():
    print('Weekly Plan')
    task_type = ['intellectual', 'chores', 'social', 'errands', 'fitness', 'physical', 'Spiritual']
    task_time = ['Early Morning', 'Morning', 'Afternoon', 'Evening', 'Night', 'Midnight']
    days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    v2_result = pd.DataFrame()
    for i in days:
        for j in task_time:
            # print(data[(data['Time_of_the_day'] == 'Early Morning') & (data['Weekday'] == 'Monday')])
            data2 = data[(data['Time_of_the_day'] == j) & (data['Weekday'] == i)]
            # print(type(data2))
            corr2 = data2.corr(method='pearson')
            # print(type(corr2))
            corr2.to_excel('newcorr.xlsx')
            corr2_res = corr2.iloc[[0], [1, 2, 3, 4, 5, 6, 7]]
            # print(corr2_res)
            # print(type(corr2_res))
            v2_result.loc[i, j] = str(corr2_res.idxmax(axis=1)).replace('Completion_rating    ', '').replace('\ndtype: object', '')
            # print(str(corr2_res.idxmax(axis=1)).replace('Completion_rating    ', ''))
    print(v2_result)
    v2_result.to_excel('final_result.xlsx')

Schedule_v2()















