def task_time_convert(tasktype):
    data[tasktype] = pd.Series(np.where(data.Time_of_the_day.values == tasktype, 1, 0),
          data.index)
task_time_convert('Early Morning')
task_time_convert('Morning')
task_time_convert('Afternoon')
task_time_convert('Evening')
task_time_convert('Night')
task_time_convert('Midnight')