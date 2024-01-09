import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('Unemployment in America Per US State.csv')

# Remove commas and convert the 'Value' column to numeric
df['Total Unemployment in State/Area'] = pd.to_numeric(df['Total Unemployment in State/Area'].str.replace(',', ''), errors='coerce')
df['Total Civilian Labor Force in State/Area'] = pd.to_numeric(df['Total Civilian Labor Force in State/Area'].str.replace(',', ''), errors='coerce')
df['Total Employment in State/Area'] = pd.to_numeric(df['Total Employment in State/Area'].str.replace(',', ''), errors='coerce')

# Group by 'Year' and 'State/Area', select specific columns, and calculate the mean for each group
# df_avg_unemployment_sorted = df.groupby(['Year', 'State/Area'])["Total Employment in State/Area",'Total Unemployment in State/Area','Percent (%) of Labor Force Unemployed in State/Area',"Percent (%) of State/Area's Population",'Total Civilian Labor Force in State/Area',"Percent (%) of Labor Force Employed in State/Area"].mean().reset_index()

columns_to_groupby = ['Year', 'State/Area']
columns_to_average = ["Total Employment in State/Area",'Total Unemployment in State/Area','Percent (%) of Labor Force Unemployed in State/Area',"Percent (%) of State/Area's Population",'Total Civilian Labor Force in State/Area',"Percent (%) of Labor Force Employed in State/Area"]
df_avg_unemployment_sorted = df.groupby(columns_to_groupby)[columns_to_average].mean().reset_index()


# Sort the DataFrame by 'Total Unemployment in State/Area' in descending order
df_avg_unemployment_sorted = df_avg_unemployment_sorted.sort_values(by='Total Unemployment in State/Area', ascending=False)

# Rename columns
column_name_mapping = {
    "State/Area": "State_Area",
    "Total Unemployment in State/Area": "TotalUnemployment",
    "Percent (%) of State/Area's Population": "PopulationPercent",
    "Total Civilian Labor Force in State/Area": "CivilianLabourForce",
    "Percent (%) of Labor Force Unemployed in State/Area": "LabourUnemployed",
    "Percent (%) of Labor Force Employed in State/Area": "LabourEmployed",
    "Total Employment in State/Area": "Totalemployment"
}

df_avg_unemployment_sorted = df_avg_unemployment_sorted.rename(columns=column_name_mapping)

df_2022 = df_avg_unemployment_sorted[df_avg_unemployment_sorted['Year'] == 2022]

# Select the top five states
top5_states_2022 = df_2022.head(5)

# Create a bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(top5_states_2022['State_Area'], top5_states_2022['LabourUnemployed'], color='skyblue')

# Display the exact percentage values on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, yval, f'{yval:.2f}%', ha='center', va='bottom', fontsize=8)

# plt.title('Top 5 States with Highest Average Unemployment Rate in 2022')
plt.xlabel('State/Area',fontweight='bold')
plt.ylabel('Average Percent (%) of Labor Force Unemployed',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks( fontweight='bold')  # Rotate x-axis labels for better visibility
plt.tight_layout()
plt.savefig("21091320_1.png", dpi=300)

# Select the bottom five states
bottom5_states_2022 = df_2022.tail(5)

# Melt the DataFrame to use 'hue' in Seaborn
melted_df = pd.melt(bottom5_states_2022, id_vars=['State_Area'], value_vars=["TotalUnemployment",'Totalemployment'],
                    var_name='Variable', value_name='Value')

# Convert the 'Value' column to numeric
melted_df['Value'] = pd.to_numeric(melted_df['Value'], errors='coerce')

# Create a bar plot using Seaborn with 'hue' for Variable
plt.figure(figsize=(12, 6))
barplot = sns.barplot(x='State_Area', y='Value', hue='Variable', data=melted_df,
                      )

# Display values on top of each bar for 'DLRate'
for i, dlrate in enumerate(melted_df[melted_df['Variable'] == 'Totalemployment']['Value']):
    plt.text(i + 0.2, dlrate, f' {dlrate:.3f} ',  ha='center', va='bottom', color='black', fontweight='bold')

# Display values on top of each bar for 'populationpercentage'
for i, percentage in enumerate(melted_df[melted_df['Variable'] == 'TotalUnemployment']['Value']):
    plt.text(i - 0.2, percentage, f' {percentage:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Country', fontweight='bold')
plt.ylabel('Values', fontweight='bold')
# plt.title('Percentage and DLRate for Each Country')

# Move the legend above the plot
plt.legend(bbox_to_anchor=(0.5, 1.07), loc='upper center', ncol=2, borderaxespad=0.)

plt.xticks( fontweight='bold')
plt.yticks(fontweight='bold')
plt.tight_layout()
plt.savefig("21091320_2.png", dpi=300)


# Melt the DataFrame to use 'hue' in Seaborn
melted_df = pd.melt(top5_states_2022, id_vars=['State_Area'], value_vars=["TotalUnemployment",'Totalemployment'],
                    var_name='Variable', value_name='Value')

# Convert the 'Value' column to numeric
melted_df['Value'] = pd.to_numeric(melted_df['Value'], errors='coerce')

# Create a bar plot using Seaborn with 'hue' for Variable
plt.figure(figsize=(12, 6))
barplot = sns.barplot(x='State_Area', y='Value', hue='Variable', data=melted_df,
                      )

# Display values on top of each bar for 'Totalemployment'
for i, dlrate in enumerate(melted_df[melted_df['Variable'] == 'Totalemployment']['Value']):
    plt.text(i + 0.2, dlrate, f' {dlrate:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

# Display values on top of each bar for 'TotalUnemployment'
for i, percentage in enumerate(melted_df[melted_df['Variable'] == 'TotalUnemployment']['Value']):
    plt.text(i - 0.2, percentage, f' {percentage:.3f} ', ha='center', va='bottom', color='black', fontweight='bold')

plt.xlabel('Country', fontweight='bold')
plt.ylabel('Values', fontweight='bold')
plt.title('Percentage and DLRate for Each Country')

# Move the legend above the plot
plt.legend(bbox_to_anchor=(0.5, 1.07), loc='upper center', ncol=2, borderaxespad=0.)

plt.xticks( fontweight='bold')
plt.yticks(fontweight='bold')
plt.tight_layout()
plt.savefig("21091320_3.png", dpi=300)


# Select the top five states
top5_states = df_avg_unemployment_sorted.groupby('State_Area').mean().nlargest(5, 'LabourUnemployed').index

# Filter the data for the top five states
df_top5_states = df_avg_unemployment_sorted[df_avg_unemployment_sorted['State_Area'].isin(top5_states)]

# Pivot the DataFrame for better plotting
df_pivot = df_top5_states.pivot(index='Year', columns='State_Area', values='LabourUnemployed')

# Plot line charts
plt.figure(figsize=(12, 8))
for state in top5_states:
    plt.plot(df_pivot.index, df_pivot[state], label=state)

# plt.title('Unemployment Change in the Last Ten Years (Top 5 States)')
plt.xlabel('Year',fontweight='bold')
plt.ylabel('Average Percent (%) of Labor Force Unemployed',fontweight='bold')
plt.xticks(fontweight='bold')
plt.yticks( fontweight='bold')
plt.legend()
plt.savefig("21091320_4.png", dpi=300)