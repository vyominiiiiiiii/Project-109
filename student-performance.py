import csv
import pandas as pd
import statistics

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].to_list()

mean=statistics.mean(data)
mode=statistics.mode(data)
stdv=statistics.stdev(data)
median=statistics.median(data)

stdv_1st_start,stdv_1st_end=mean-stdv,mean+stdv
stdv_2nd_start,stdv_2nd_end=mean-(2*stdv),mean+(2*stdv)

first=[result for result in data if result>stdv_1st_start and result<stdv_1st_end]
second=[result for result in data if result>stdv_2nd_start and result<stdv_2nd_end]

print("mean is {}".format(mean))
print("median is {}".format(median))
print("mode is {}".format(mode))
print("standard deviation is {}".format(stdv))

print("{}% of data lies within 1st standard deviation".format(len(first)*100.0/len(data)))
print("{}% of data lies within 2nd standard deviation".format(len(second)*100.0/len(data)))

