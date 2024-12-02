# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 11:39:34 2024

@author: kolli
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load your preprocessed dataset (replace the path with your actual file path)
iron_ore_data_preprocessed = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Business Moments after preprocessing Python\iron_ore_dataset_encoded.xls')

# Get all numerical columns (float64, int64)
numerical_cols = iron_ore_data_preprocessed.select_dtypes(include=['float64', 'int64']).columns


# Set up the matplotlib and seaborn styles
sns.set(style='whitegrid')

# 1. Histogram and Density Plot for each numerical column
for col in numerical_cols:
    plt.figure(figsize=(12, 6))
    sns.histplot(iron_ore_data_preprocessed[col], kde=True)
    plt.title(f'Histogram and Density Plot of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

# 2. Box Plot for each numerical column
for col in numerical_cols:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=iron_ore_data_preprocessed[col])
    plt.title(f'Box Plot of {col}')
    plt.xlabel(col)
    plt.show()



# Set the Date column as the index
iron_ore_data_preprocessed.set_index('Date', inplace=True)

# 3. Line Chart for each numerical column (using the Date index)
for col in numerical_cols:
    plt.figure(figsize=(12, 6))
    plt.plot(iron_ore_data_preprocessed[col], marker='o')
    plt.title(f'Line Chart of {col} over Time')
    plt.xlabel('Date')
    plt.ylabel(col)
    plt.xticks(rotation=45)  # Rotate date labels for better visibility
    plt.tight_layout()  # Adjust layout to make room for the rotated labels
    plt.show()



import seaborn as sns
from itertools import combinations



# Selected pairs of variables
selected_pairs = [
    ('Iron_Ore_Price', 'Global_Demand'),
    ('Iron_Ore_Price', 'Copper_Price'),
    ('Iron_Ore_Price', 'Nickel_Price'),
    ('Tariffs', 'Carbon_Emissions'),
    ('Copper_Price', 'Nickel_Price'),
    ('Iron_Ore_Price', 'Interest_Rate')
]

# Create scatter plots for each selected pair with correlation coefficient
for col1, col2 in selected_pairs:
    plt.figure(figsize=(10, 6))
    
    # Calculate the correlation coefficient
    correlation_coefficient = iron_ore_data_preprocessed[col1].corr(iron_ore_data_preprocessed[col2])
    
    # Create scatter plot
    sns.scatterplot(data=iron_ore_data_preprocessed, x=col1, y=col2, color='blue', s=100, alpha=0.6)

    # Optional: Add a regression line to see the trend
    sns.regplot(data=iron_ore_data_preprocessed, x=col1, y=col2, scatter=False, color='red', line_kws={"linestyle": "--"})

    # Title and labels
    plt.title(f'Scatter Plot of {col1} vs {col2}', fontsize=16)
    plt.xlabel(col1)
    plt.ylabel(col2)
    
    # Add correlation coefficient to the plot
    plt.text(0.05, 0.95, f'Correlation: {correlation_coefficient:.2f}', fontsize=14,
             transform=plt.gca().transAxes, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.5))
    
    plt.grid(True)
    plt.show()

# 5. Heatmap for correlation matrix
correlation_matrix = iron_ore_data_preprocessed[numerical_cols].corr()
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Correlation Heatmap')
plt.show()

# 6. Correlation Coefficient for the chosen pair of variables
correlation_coefficient = iron_ore_data_preprocessed[numerical_cols[0]].corr(iron_ore_data_preprocessed[numerical_cols[1]])
print(f'Correlation Coefficient between {numerical_cols[0]} and {numerical_cols[1]}: {correlation_coefficient}')
