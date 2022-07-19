import statistics
from numpy import std
import pandas as pd

df=pd.read_csv('StudentsPerformance.csv')
data=df['reading score'].to_list()

mean=statistics.mean(data)
median=statistics.median(data)
mode=statistics.mode(data)
stdev=statistics.stdev(data)

first_std_dev_start,first_std_dev_end=mean-stdev,mean+stdev
second_std_dev_start,second_std_dev_end=mean-(2*stdev),mean+(2*stdev)
third_std_dev_start,third_std_dev_end=mean-(3*stdev),mean+(3*stdev)

std_dev_1=[result for result in data if result>first_std_dev_start and result<first_std_dev_end]
std_dev_2=[result for result in data if result>second_std_dev_start and result<second_std_dev_end]
std_dev_3=[result for result in data if result>third_std_dev_start and result<third_std_dev_end]


print('The mean is ',mean)
print('The median is ',median)
print('The mode is ',mode)
print('The standard deviation is ',stdev)
print('{}% of data lies between first standard deviation'.format(len(std_dev_1)*100/len(data)))
print('{}% of data lies between second standard deviation'.format(len(std_dev_2)*100/len(data)))
print('{}% of data lies between third standard deviation'.format(len(std_dev_3)*100/len(data))) 
