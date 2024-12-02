# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:00:40 2024

@author: kolli
"""

import pandas as pd
from sqlalchemy import create_engine

# Database connection parameters
DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'  # MySQL server
USER = 'root'
PASSWORD = 'Vedanshi%402017'  # URL-encoded password (%40 for @)
PORT = 3306
DATABASE = 'project_2db'

# Create SQLAlchemy engine to connect to MySQL Database
engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}")

# Load your dataset using read_excel for Excel files
df = pd.read_excel(r'C:\Users\kolli\OneDrive\Documents\360DigiTMG\IRON ORE PRICE ANALYSIS - PROJECT\Downloads\iron_ore_dataset.xlsx')

# Import the DataFrame into the MySQL database
table_name = 'iron_ore_data'  # Replace with your desired table name
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"Data imported successfully into {table_name}!")


DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'
USER = 'root'
PASSWORD = 'Vedanshi@2017'
PORT = 3306
DATABASE = 'project_2db'


null_counts = df.isnull().sum()

# Display the count of null values
print(null_counts)

total_null_count = df.isnull().sum().sum()

# Display the total count of null values
print(f'Total count of null values in the dataset: {total_null_count}')


