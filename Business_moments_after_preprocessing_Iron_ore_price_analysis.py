
# Import necessary libraries
import pandas as pd
from scipy import stats

# Load your scaled dataset (if not already in the same variable)

iron_ore_data_scaled = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Business Moments after preprocessing Python\iron_ore_dataset_minmax_scaled.xls')

# Get all numerical columns (float64, int64)
numerical_cols = iron_ore_data_scaled.select_dtypes(include=['float64', 'int64']).columns

# Initialize a DataFrame to hold the statistical measures
stats_df = pd.DataFrame(index=numerical_cols)

# Calculate Mean
stats_df['Mean'] = iron_ore_data_scaled[numerical_cols].mean()

# Calculate Median
stats_df['Median'] = iron_ore_data_scaled[numerical_cols].median()

# Calculate Mode
stats_df['Mode'] = iron_ore_data_scaled[numerical_cols].mode().iloc[0]

# Calculate Standard Deviation
stats_df['Standard Deviation'] = iron_ore_data_scaled[numerical_cols].std()

# Calculate Variance
stats_df['Variance'] = iron_ore_data_scaled[numerical_cols].var()

# Calculate Range
stats_df['Range'] = iron_ore_data_scaled[numerical_cols].max() - iron_ore_data_scaled[numerical_cols].min()

# Calculate Skewness
stats_df['Skewness'] = iron_ore_data_scaled[numerical_cols].skew()

# Calculate Kurtosis
stats_df['Kurtosis'] = iron_ore_data_scaled[numerical_cols].kurtosis()

# Display the statistical measures
print(stats_df)

# Save the statistics DataFrame to a CSV file
stats_df.to_csv('iron_ore_dataset_statistics.csv')

print("Statistics saved to 'iron_ore_dataset_statistics.csv'.")


#############***************Statistics before Scaling the dataset ********############

# Load your preprocessed dataset (replace the path with your actual file path)
iron_ore_data_preprocessed = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Business Moments after preprocessing Python\iron_ore_dataset_encoded.xls')

# Get all numerical columns (float64, int64)
numerical_cols = iron_ore_data_preprocessed.select_dtypes(include=['float64', 'int64']).columns

# Initialize a DataFrame to hold the statistical measures
stats_df_preprocessed = pd.DataFrame(index=numerical_cols)

# Calculate Mean
stats_df_preprocessed['Mean'] = iron_ore_data_preprocessed[numerical_cols].mean()

# Calculate Median
stats_df_preprocessed['Median'] = iron_ore_data_preprocessed[numerical_cols].median()

# Calculate Mode
stats_df_preprocessed['Mode'] = iron_ore_data_preprocessed[numerical_cols].mode().iloc[0]

# Calculate Standard Deviation
stats_df_preprocessed['Standard Deviation'] = iron_ore_data_preprocessed[numerical_cols].std()

# Calculate Variance
stats_df_preprocessed['Variance'] = iron_ore_data_preprocessed[numerical_cols].var()

# Calculate Range
stats_df_preprocessed['Range'] = iron_ore_data_preprocessed[numerical_cols].max() - iron_ore_data_preprocessed[numerical_cols].min()

# Calculate Skewness
stats_df_preprocessed['Skewness'] = iron_ore_data_preprocessed[numerical_cols].skew()

# Calculate Kurtosis
stats_df_preprocessed['Kurtosis'] = iron_ore_data_preprocessed[numerical_cols].kurtosis()

# Display the statistical measures
print(stats_df_preprocessed)

# Save the statistics DataFrame to a CSV file
stats_df_preprocessed.to_csv('iron_ore_dataset_statistics_preprocessed.csv')

print("Statistics for the preprocessed dataset saved to 'iron_ore_dataset_statistics_preprocessed.csv'.")
