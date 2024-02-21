import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt

st.write("""# Tipping in restaurants. """)
path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
#path = '../learning/datasets/tips.csv'
tips = pd.read_csv(path)

date1 = pd.to_datetime('2023-01-01')
date2 = pd.to_datetime('2023-01-31')
rand_dates = pd.to_datetime(np.random.randint(date1.value, date2.value, len(tips)))
tips['time_order'] = rand_dates.date

st.dataframe(tips)

#1
st.write("""### Dynamics of tips over time """)
st.line_chart(tips.groupby('time_order')['tip'].sum())

#2
st.write('### Histogram of Total Bill')
plt.hist(tips['total_bill'], bins=13, color='skyblue', edgecolor='white') 
plt.xlabel('Total Bill') 
plt.ylabel('Frequency')  
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()

#3
st.write('### Scatterplot of Total Bill and Tip')
fig, ax = plt.subplots(figsize=(5, 5))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', palette='pastel', s=23)
st.pyplot(fig)

#4
st.write('### Scatterplot of Total Bill and Tip by size')
fig, ax = plt.subplots(figsize=(5, 5))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='time', palette='bright', size='size')
st.pyplot(fig)

#5
st.write('### Bill size by day')
tips.groupby('day')['total_bill'].sum().plot(kind='bar')
plt.ylabel('Bill')
plt.xticks(rotation=0)
st.pyplot()

#6
st.write('### Tipping Habits in Restaurants')
sns.set_style("whitegrid") 
plt.figure(figsize=(10,5)) 
sns.scatterplot(data=tips, x="tip", y="day", hue="sex") 
plt.legend(title='Gender', loc='upper right') 
st.pyplot()

#7
st.write('### Total Bill by Time of Day')
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.boxplot(x="time", y="total_bill", data=tips, palette="Set3")
st.pyplot()

#8
st.write('#### Total Bill by Time of Day var.2')
sns.set_theme(style="whitegrid")
sns.catplot(data=tips, x="total_bill", y="time", hue="sex", kind="boxen", palette="Set3")
st.pyplot()

#9
st.write('### Tips for lunch and dinner')
lunch_tips = tips[tips['time'] == 'Lunch']['tip']
dinner_tips = tips[tips['time'] == 'Dinner']['tip']

raw, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 5))

axes[0].hist(lunch_tips, bins=10, color='skyblue')
axes[0].set_xlabel('Tip')
axes[0].set_ylabel('Frequency')
axes[0].set_title('Tips for Lunch')

axes[1].hist(dinner_tips, bins=10, color='salmon')
axes[1].set_xlabel('Tip')
axes[1].set_ylabel('Frequency')
axes[1].set_title('Tips for Dinner')

st.pyplot()

#10
male = tips[tips['sex'] == 'Male'] 
female = tips[tips['sex'] == 'Female']

plt.subplot(1, 2, 1) 
sns.scatterplot(data=male, x='total_bill', y='tip', hue='smoker') 
plt.title('For males')

plt.subplot(1, 2, 2) 
sns.scatterplot(data=female, x='total_bill', y='tip', hue='smoker') 
plt.title('For females') 

st.pyplot()

st.success('The end :)', icon="✨")
st.balloons()