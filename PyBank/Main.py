import csv
import os

filepath = os.path.join("budget_data_2.csv")

revenue= []
date = []

with open(filepath) as data_file:

    
    csv_data = csv.reader(data_file)
    
    next(csv_data)
    
    for row in csv_data:
        revenue.append(float(row[1]))
        date.append(row[0])
        
        
        
#Revenue Change

revenue_change = []

for i in range(1,len(revenue)):
    
        revenue_change.append(revenue[i] - revenue[i-1])
        
avg_revenue_change = sum(revenue_change)/len(revenue_change)

#Max Revenue   

index_max_revenue_change = revenue_change.index(max(revenue_change))
max_revenue_change_date = date[index_max_revenue_change]
 
#Min Revenue 

index_min_revenue_change = revenue_change.index(min(revenue_change))
min_revenue_change_date = date[index_min_revenue_change]

#

#print Financial Analysis to terminal

print('Financial Analysis')
print('----------------------------')
print('Total Months: {}'.format(len(date)))
print('Total Revenue: {}'.format(sum(revenue)))
print('Average Revenue Change: {}'.format(round(avg_revenue_change,2)))
print('Greatest Increase in Revenue: {} (${})'.format(max_revenue_change_date,max(revenue_change)))
print('Greatest Decrease in Revenue: {} (${})'.format(min_revenue_change_date,min(revenue_change)))