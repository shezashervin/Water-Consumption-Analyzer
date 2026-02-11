import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('\nANNUAL WATER CONSUMPTION ANALYZER')
print('---------------------------------')

water_usage=[]
months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEPT','OCT','NOV','DEC']

for i in range(12):
    water=int(input(f"Enter your water usage for month {i+1} (in Litres): "))
    water_usage.append(water)

# bar graph
df=pd.DataFrame({
        'Months': months,
        'Usage': water_usage
    })

plt.bar(df['Months'],df['Usage'])
plt.xlabel('MONTHS ')
plt.ylabel('USAGE (in Litres)')
plt.title('WATER CONSUMPTION ANALYSIS')
plt.show()

# pie chart
colorss=['navy','cyan','blue']
plt.pie(water_usage,labels=months,colors=colorss,counterclock=False,startangle=90)
plt.title('WATER CONSUMPTION ANALYSIS')
plt.show()

# yearly consumption analysis report
a=np.array(water_usage)
total_water_consumption=np.sum(water_usage)
avg_water_consumption=total_water_consumption/12
max_consumption_month=months[np.argmax(a)]
min_consumption_month=months[np.argmin(a)]

blah=[f'{total_water_consumption}',f'{avg_water_consumption:.2f}',max_consumption_month,min_consumption_month]
print("\nWATER CONSUMPTION ANALYSIS REPORT")
print('-----------------------------------')
display=pd.Series(blah,index=[' Total Water Consumption: ',' Average Water Consumption: ',' Maximum Consumption Month: ',' Minimum Consumption Month: '])
print(display.to_string())
