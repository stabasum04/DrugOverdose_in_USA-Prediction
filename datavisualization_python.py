import pandas as pd
import matplotlib.pyplot as plt

# Loaded the cleaned data into a DataFrame that was cleaned using R
data = pd.read_csv("clean_data.csv")

#Descriptive Statistics of the dataset:
descriptive_stats = data.describe()
print("\nDescriptive Statistics:")
print(descriptive_stats)
# Measures of Central Tendency
mean_value = data['ESTIMATE'].mean()
median_value = data['ESTIMATE'].median()
mode_value = data['ESTIMATE'].mode().iloc[0]

print(f"\nMean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

# Frequency Distribution
plt.hist(data['ESTIMATE'], bins='auto', alpha=0.7, rwidth=0.85)
plt.title('Frequency Distribution of ESTIMATE')
plt.xlabel('ESTIMATE')
plt.ylabel('Frequency')
plt.show()

# Question 1: How have the drug overdose death rates in the United States changed over the past 20 years?
average_rates_by_year = data.groupby('YEAR_NUM')['ESTIMATE'].mean()
#To build the index box on the graph.
year_group_mapping = {
    "X-AXIS": '',
    '1999': 1,
    '2000': 2,
    '2001': 3,
    '2002': 4,
    '2003': 5,
    '2004': 6,
    '2005': 7,
    '2006': 8,
    '2007': 9,
    '2008': 10,
    '2009': 11,
    '2010': 12,
    '2011': 13,
    '2012': 14,
    '2013': 15,
    '2014': 16,
    '2015': 17,
    '2016': 18,
    '2017': 19,
    '2018': 20,
}
plt.plot(average_rates_by_year.index, average_rates_by_year.values, color='red')
plt.xlabel("Year")
plt.ylabel("Overall Estimate")
plt.title("Average Drug Overdose Death Rates in the United States (1999-2018)")
#build the box
legend_text = "\n".join([f"{key}: {value}" for key, value in year_group_mapping.items()])
plt.legend([legend_text], loc='upper left', bbox_to_anchor=(1.0, 0.98), borderaxespad=0.)
plt.show()

# Question 2: Is there any correlation between overdose deaths and drug types or demographics like age and race/ethnicity?

# Correlation between overdose deaths and age
correlation_gender = data['ESTIMATE'].corr(data['AGE_NUM'])
print("Correlation between overdose deaths and gender:", correlation_gender)

# Correlation between overdose deaths and race/ethnicity
correlation_race = data['ESTIMATE'].corr(data['STUB_LABEL_NUM'])
print("Correlation between overdose deaths and race/ethnicity:", correlation_race)


age_group_mapping = {
    "Y-AXIS": '',
    'All Ages': 1.1,
    'Under 15': 1.2,
    '15-24': 1.3,
    '25-34': 1.4,
    '35-44': 1.5,
    '45-54': 1.6,
    '55-64': 1.7,
    '65-74': 1.8,
    '75-84': 1.9,
    '85 and above': 1.91,
}
#corr between Overdose Deaths and Age-plot
plt.scatter(data['ESTIMATE'], data['AGE_NUM'], color='green')
plt.xlabel("Estimated Drug Overdose Death Rate")
plt.ylabel("Age Number")
plt.title("Correlation between Overdose Deaths and Age")
legend_text = "\n".join([f"{key}: {value}" for key, value in age_group_mapping.items()])
plt.legend([legend_text], loc='upper left', bbox_to_anchor=(0.81, 0.98), borderaxespad=0.)
plt.show()

stub_group_mapping = {
    "Y-AXIS": '',
    'Total': 0,
    'Age': 1,
    'Sex': 2,
    'Age and Sex': 3,
    'Sex and Race': 4,
    'Sex Race and Hispanic origin': 5,
    
}
#corr between Deaths and Sex, Age,Race and Ethnicity-plot
plt.scatter(data['ESTIMATE'], data['STUB_NAME_NUM'], color='orange')
plt.xlabel("Estimated Drug Overdose Death Rate")
plt.ylabel("STUB")
plt.title("Correlation between Overdose Deaths and Sex, Age,Race and Ethnicity")
legend_text = "\n".join([f"{key}: {value}" for key, value in stub_group_mapping.items()])
plt.legend([legend_text], loc='upper left', bbox_to_anchor=(0.74, 0.98), borderaxespad=0.)
plt.show()



#3 Are there variations in drug overdose death rates based on demographics such as age, gender, race, and ethnicity, and how do these differences inform different prevention efforts?

sex_array = [0]
age_array = [0]
race_array = [0]
hispanic_array = [0]

for i in data['STUB_NAME']:
    if i =="Total":
        hispanic_array[0]+=1
        sex_array[0]+=1
        race_array[0]+=1
    elif i=="Age":
        age_array[0]+=1
        
    elif i=="Sex":
        sex_array[0]+=1
        
    elif i=='Sex and age':
        age_array[0]+=1
        sex_array[0]+=1
        
    elif i=="Sex and race":
        sex_array[0]+=1
        race_array[0]+=1
        
    elif i=="Sex and race and Hispanic origin":
        hispanic_array[0]+=1
        sex_array[0]+=1
        race_array[0]+=1

categories = ['Sex', 'Age', 'All races', 'Only Hispanic Origin']
values = [sex_array[0], age_array[0], race_array[0], hispanic_array[0]]

# Plotting the bar graph
plt.bar(categories, values, color=['blue', 'orange', 'green', 'red', 'purple'])
plt.xlabel('STUBS/Categories')
plt.ylabel('Count')
plt.title('Distribution of Categories')
plt.show()
#printing the bar columns count
print("The dataset input value from Age :",age_array)
print("The dataset input value from Sex is :",sex_array)
print("The dataset input value from All races is :",race_array)
print("The dataset input value from Hispanic origin is :",hispanic_array)

# Group by 'PANEL' and 'SEX', then calculate the count of 'ESTIMATE' for each group
grouped_data = data.groupby(['PANEL', 'SEX']).count()['ESTIMATE'].unstack()

# Plotting
plt.figure(figsize=(12, 6))
ax = grouped_data.plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('Drug Types')
plt.ylabel('Count')
plt.title('Comparison of Drug Types by Sex')
plt.legend(title='SEX', loc='upper right')
plt.xticks(rotation=45, ha='right') 
plt.tight_layout()
plt.show()

#count of sex:
male_female_data = data[data['SEX'].isin(['Male', 'Female'])]
grouped_data = male_female_data.groupby(['PANEL', 'SEX']).count()['ESTIMATE'].unstack()
print(grouped_data)

#Age
plt.figure(figsize=(12, 6))
grouped_data = data.groupby(['PANEL', 'AGE']).count()['ESTIMATE'].unstack()

# Plotting the grouped data
grouped_data.plot(kind='bar', stacked=True, ax=plt.gca())
plt.xlabel('Drug Types')
plt.ylabel('Count')
plt.title('Comparison of Drug Types by Age')
plt.legend(title='AGE', loc='upper right', bbox_to_anchor=(1.2, 1))
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
grouped_data = data.groupby(['PANEL', 'AGE']).count()['ESTIMATE'].unstack()
print("Comparison of Drug Types by Age:")
print(grouped_data)
