import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Step 1: Load and Explore the Dataset
df = pd.read_csv('Data/creditcard.csv')

# Step 1b: Data Dictionary (as explained earlier)

# Step 2a: Database Connection
user = 'root'
password = '28311'
host = '127.0.0.1'
port = '3306'
database = 'creditcard_db'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')

# Step 2b: Import Data into MySQL
df.to_sql(name='transactions', con=engine, if_exists='replace', index=False)

# Step 2c: Normalize Data
scaler = StandardScaler()
df[['Normalized_Amount', 'Normalized_Time']] = scaler.fit_transform(df[['Amount', 'Time']])

# Optional: Drop original 'Amount' and 'Time' columns
# df.drop(['Amount', 'Time'], axis=1, inplace=True)

# Import Normalized Data into MySQL
df.to_sql(name='transactions_normalized', con=engine, if_exists='replace', index=False)

# Additional Visualization
plt.figure(figsize=(10, 5))
plt.hist(df['Amount'], bins=50, alpha=0.5, label='Original Amount')
plt.hist(df['Normalized_Amount'], bins=50, alpha=0.5, label='Normalized Amount')
plt.title('Amount Distribution')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(df['Time'], bins=50, alpha=0.5, label='Original Time')
plt.hist(df['Normalized_Time'], bins=50, alpha=0.5, label='Normalized Time')
plt.title('Time Distribution')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.legend()
plt.show()
