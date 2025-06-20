# Unemployment Analysis with Python

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace filename with your dataset's path)
df = pd.read_csv("unemployment_data.csv")

# Display first few rows
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Drop missing values (or handle appropriately)
df.dropna(inplace=True)

# Convert 'Date' column to datetime format if not already
df['Date'] = pd.to_datetime(df['Date'])

# Set date as index
df.set_index('Date', inplace=True)

# Plot Unemployment Rate over Time
plt.figure(figsize=(12, 6))
df['Unemployment Rate'].plot(title='Unemployment Rate Over Time', ylabel='Rate (%)')
plt.grid(True)
plt.show()

# Monthly Average Trend
df['Month'] = df.index.month
monthly_avg = df.groupby('Month')['Unemployment Rate'].mean()

plt.figure(figsize=(10, 5))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values)
plt.title('Average Unemployment Rate by Month')
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

# Highlight COVID-19 period
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Unemployment Rate'], label='Unemployment Rate')
plt.axvspan(pd.to_datetime('2020-03'), pd.to_datetime('2021-12'), color='red', alpha=0.3, label='COVID-19 Period')
plt.legend()
plt.title('Unemployment Trends with COVID-19 Highlight')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.show()

# Statistical Summary
print("\nStatistical Summary:")
print(df['Unemployment Rate'].describe())

# Correlation Analysis (if multiple columns exist)
if df.shape[1] > 1:
    print("\nCorrelation Matrix:")
    print(df.corr())
