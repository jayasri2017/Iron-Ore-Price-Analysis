# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:14:13 2024

@author: kolli
"""
# Import necessary libraries
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.impute import KNNImputer
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mstats

# Load your dataset using read_excel for Excel files
iron_ore_data = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Downloads\iron_ore_dataset.xlsx')

## ********************* HANDLING MISSING VALUES *******************####
# Check for missing values 
missing_values = iron_ore_data.isnull().sum()
print("Missing values before imputation:\n", missing_values)

total_missing_values = iron_ore_data.isnull().sum().sum()
print("Total missing values before imputation:", total_missing_values)

# Get all numerical columns (float64, int64) for imputation
numerical_cols = iron_ore_data.select_dtypes(include=['float64', 'int64']).columns

# Initialize KNNImputer
imputer = KNNImputer(n_neighbors=5)

# Apply KNN imputation only on numerical columns
iron_ore_data[numerical_cols] = imputer.fit_transform(iron_ore_data[numerical_cols])

# Get categorical columns
categorical_cols = iron_ore_data.select_dtypes(include=['object']).columns

# Replace null values in categorical columns with 'unknown'
iron_ore_data[categorical_cols] = iron_ore_data[categorical_cols].fillna('unknown')

#############*********Histogram and Density Plots ************############
# Loop through each numerical column and plot histogram + density plot after imputation
for col in numerical_cols:
    plt.figure(figsize=(10, 6))
    # Plot histogram with density plot (KDE)
    sns.histplot(iron_ore_data[col], kde=True, bins=30, color='blue')
    # Adding title and labels
    plt.title(f'Histogram and Density Plot of {col} (After KNN Imputation)', fontsize=16)
    plt.xlabel(f'{col}', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)

# Step 2: Categorical Columns - Fill missing values with 'Unknown'
iron_ore_data['Ore_Grade'].fillna('Unknown', inplace=True)
iron_ore_data['Mining_Location'].fillna('Unknown', inplace=True)

# Step 4: Save the dataset with missing values handled
iron_ore_data.to_csv('iron_ore_dataset_with_imputed_values.csv', index=False)
print("Missing values handled successfully for all numeric and categorical columns.")

## ********************* HANDLING DUPLICATES  *******************####
# Step 1: Detect duplicate rows in the dataset
duplicate_rows = iron_ore_data.duplicated()

# Step 2: Count the number of duplicate rows in the entire dataset
num_duplicates = duplicate_rows.sum()
print(f"\nTotal number of duplicate rows in the dataset: {num_duplicates}")

# Step 3: Display the actual duplicate rows (if you want to see them)
if num_duplicates > 0:
    print("\nDuplicate rows in the dataset:")
    print(iron_ore_data[duplicate_rows])

# Step 4: Save the duplicate rows to a CSV file (optional)
iron_ore_data[duplicate_rows].to_csv('duplicate_rows.csv', index=False)
print("Duplicate rows saved to 'duplicate_rows.csv'.")

#########************** TYPE CASTING *******************************##########
# Convert categorical columns to 'category' data type
iron_ore_data['Ore_Grade'] = iron_ore_data['Ore_Grade'].astype('category')
iron_ore_data['Mining_Location'] = iron_ore_data['Mining_Location'].astype('category')

# Verify the data types after conversion
print(iron_ore_data.dtypes)

############******************* BOX PLOT ****************##############
sns.set(style="whitegrid")
# Create box plots for each numerical column
for col in numerical_cols:
    plt.figure(figsize=(12, 6))
    sns.boxplot(y=iron_ore_data[col])
    # Add title and labels
    plt.title(f'Box Plot of {col}')
    plt.ylabel(col)
    # Show the plot
    plt.tight_layout()  # Adjust layout for better appearance
    plt.show()

##########*************** Capping method to handle ouliers ****************####

# Function to cap outliers
def cap_outliers(data, col):
    Q1 = data[col].quantile(0.25)
    Q3 = data[col].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Cap outliers
    data[col] = data[col].clip(lower=lower_bound, upper=upper_bound)

# Apply capping to each numerical column
for col in numerical_cols:
    cap_outliers(iron_ore_data, col)

# Step 5: Save the dataset after handling outliers
iron_ore_data.to_csv('iron_ore_dataset_with_capped_outliers.csv', index=False)
print("Outliers handled successfully and dataset saved as 'iron_ore_dataset_with_capped_outliers.csv'.")

##########*************** ZERO VARIANCE AND NEAR ZERO VARIANCE ****************####

from sklearn.feature_selection import VarianceThreshold

# Step 1: Calculate the variance of each numerical column
variances = iron_ore_data[numerical_cols].var()
print("Variances of numerical columns:\n", variances)

# Step 2: Identify columns with zero variance
zero_variance_cols = variances[variances == 0].index.tolist()
print("\nColumns with zero variance:", zero_variance_cols)

# Step 3: Identify columns with near-zero variance (you can adjust the threshold)
near_zero_variance_cols = variances[abs(variances) < 1e-5].index.tolist()
print("Columns with near-zero variance:", near_zero_variance_cols)

## that there are no columns with zero variance or near-zero variance in your dataset,
## there is no need to drop any columns based on those criteria. 
#Threshold:Commonly set at 1e-5 (0.00001) 


##########*************** ONE-HOT ENCODING ****************####

# Step 1: Identify categorical columns that need to be one-hot encoded
# You might want to encode categorical columns that were originally of object type
categorical_cols = iron_ore_data.select_dtypes(include=['category']).columns.tolist()

# Step 2: Apply one-hot encoding
iron_ore_data_encoded = pd.get_dummies(iron_ore_data, columns=categorical_cols, drop_first=True)

# Display the first few rows of the new dataset to verify one-hot encoding
print(iron_ore_data_encoded.head())

# Step 3: Save the encoded dataset
iron_ore_data_encoded.to_csv('iron_ore_dataset_encoded.csv', index=False)
print("One-hot encoding completed and dataset saved as 'iron_ore_dataset_encoded.csv'.")


#########**********************Transformation **************************#########
## Highly skewed columns (Iron_Ore_Price, Production_Volume) may benefit from Logarithmic 
## or Exponential Transformations to reduce skewness.
## Most other columns are approximately symmetric with low skewness, 
## so no transformation is needed for them.

# Apply Log Transformation for Iron_Ore_Price and Production_Volume
iron_ore_data['Iron_Ore_Price_log'] = np.log(iron_ore_data['Iron_Ore_Price'].replace(0, np.nan))  # Replace zeros with NaN to avoid log(0)
iron_ore_data['Production_Volume_log'] = np.log(iron_ore_data['Production_Volume'].replace(0, np.nan))


# Check the transformed columns
print(iron_ore_data[['Iron_Ore_Price', 'Iron_Ore_Price_log', 'Production_Volume', 'Production_Volume_log']].head())


##########*************Feature Scaling or Feature shrinking *******************###########


from sklearn.preprocessing import MinMaxScaler

# Step 1: Get all numerical columns (float64, int64)
numerical_cols = iron_ore_data.select_dtypes(include=['float64', 'int64']).columns

# Step 2: Initialize the MinMaxScaler to scale between 0 and 1 (default)
min_max_scaler = MinMaxScaler()

# Step 3: Apply Min-Max scaling to the numerical columns
iron_ore_data_scaled = iron_ore_data.copy()
iron_ore_data_scaled[numerical_cols] = min_max_scaler.fit_transform(iron_ore_data[numerical_cols])

# Step 4: Verify the scaled data (optional)
print(iron_ore_data_scaled.head())

# Step 5: Save the scaled dataset if necessary
iron_ore_data_scaled.to_csv('iron_ore_dataset_minmax_scaled.csv', index=False)
print("Min-Max scaling completed and dataset saved as 'iron_ore_dataset_minmax_scaled.csv'.")




