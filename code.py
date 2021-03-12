# --------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file is stored in the variable path. 

#Code starts here

# Data Loading

#Reading the file
data=pd.read_csv(path)

#Renaming a column
data.rename(columns={'Total':'Total_Medals'},inplace=True)

#Printing the first five columns
print(data.head(5))

# Summer or Winter

#Creating new column 'Better_Event'
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'] , 'Summer', 'Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])

#Finding the value with max count in 'Better_Event' column
better_event=data['Better_Event'].value_counts().index.values[0]

#Printing the better event
print('Better_Event=', better_event)

# Top 10

#Subsetting the dataframe
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]

#Dropping the last row
top_countries=top_countries[:-1]

#Function for top 10
def top_ten(data, col):

    #Creating a new list
    country_list=[]

    #Finding the top 10 values of 'col' column
    country_list= list((data.nlargest(10,col)['Country_Name']))

    #Returning the top 10 list
    return country_list



#Calling the function for Top 10 in Summer
top_10_summer=top_ten(top_countries,'Total_Summer')
print("Top 10 Summer:\n",top_10_summer, "\n")

#Calling the function for Top 10 in Winter
top_10_winter=top_ten(top_countries,'Total_Winter')
print("Top 10 Winter:\n",top_10_winter, "\n")

#Calling the function for Top 10 in both the events
top_10=top_ten(top_countries,'Total_Medals')
print("Top 10:\n",top_10, "\n")

#Extracting common country names from all three lists
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))

print('Common Countries :\n', common, "\n")

# Plotting Top 10
#For Summer

#Creating the dataframe for Summer event
summer_df= data[data['Country_Name'].isin(top_10_summer)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'])

#Changing the graph title
plt.title('Top 10 Summer')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')

#for winter

#creating a new dataframe for winter event
winter_df = data[data["Country_Name"].isin(top_10_winter)]

#plotting the bar graph
plt.figure(figsize=(20,6))
plt.bar(winter_df['Country_Name'], winter_df['Total_Winter'])

#Changing the graph title
plt.title('Top 10 Winter')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')

#for both

#Creating the dataframe for both the events
top_df=data[data['Country_Name'].isin(top_10)]

#Plotting the bar graph
plt.figure(figsize=(20, 6))
plt.bar(top_df['Country_Name'], top_df['Total_Medals'])

#Changing the graph title
plt.title('Top 10 ')

#Changing the x-axis label
plt.xlabel('Country Name')

#Changing the y-axis label
plt.ylabel('Total Medals')

#STEP 5

# Best In Summer 

summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']

summer_max_ratio = max(summer_df['Golden_Ratio'])

summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name'] 

print("Top Summer Country:", summer_country_gold, " with a ratio of %.2f" %summer_max_ratio )

# Best In Winter 

winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']

winter_max_ratio  = max(winter_df['Golden_Ratio'])

winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']

print("Top Winter Country: ", winter_country_gold, "with a ratio of %.2f" %winter_max_ratio)

#best in top

top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']

top_max_ratio = max(top_df['Golden_Ratio'])

top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']

print("Top country:", top_country_gold, "with a ratio of %.2f" %top_max_ratio)

#Step 6

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1

most_points = max(data_1['Total_Points'])

best_country = data_1.loc[data_1['Total_Points'].idxmax(),"Country_Name"]

print("best country", best_country , "with most points" ,most_points )

#Step 7
best = data[data['Country_Name']== best_country]

best.reset_index(drop = True, inplace = True)

best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked = True)

plt.xlabel('United States')

plt.ylabel('Medals Tally')

plt.xticks(rotation = 45)











