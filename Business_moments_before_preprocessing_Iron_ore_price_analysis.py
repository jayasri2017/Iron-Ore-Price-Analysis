# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats

# Load your dataset using read_excel for Excel files
df = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Downloads\iron_ore_dataset.xlsx')

# Step 2: Display the first few rows of the dataset to ensure it has been loaded correctly
print(df.head())


# Step 3: Calculate statistical measures for the entire dataset (numeric columns only)
# Automatically select only the numeric columns
numeric_df = df.select_dtypes(include=[np.number])


# Create an empty DataFrame to store the results
stats_df = pd.DataFrame()

# Calculate Mean
stats_df['Mean'] = numeric_df.mean()

# Calculate Median
stats_df['Median'] = numeric_df.median()

# Calculate Mode (extract the first mode per column)
stats_df['Mode'] = numeric_df.mode().iloc[0]

# Calculate Range (max - min)
stats_df['Range'] = numeric_df.max() - numeric_df.min()

# Calculate Variance
stats_df['Variance'] = numeric_df.var()

# Calculate Standard Deviation
stats_df['Standard Deviation'] = numeric_df.std()

# Calculate Skewness
stats_df['Skewness'] = numeric_df.skew()

# Calculate Kurtosis
stats_df['Kurtosis'] = numeric_df.kurtosis()

# Step 3: Save the statistics to a CSV file
# Replace 'statistical_values.csv' with your desired file path and name
stats_df.to_csv('statistical_values.csv', index=True)

print("Statistical values saved successfully.")
