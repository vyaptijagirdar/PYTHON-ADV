import pandas as pd
import numpy as np

data = {
    'Name': ['Aarav', 'Diya', 'Rahul', None, 'Priya'],
    'Age': [20, np.nan, 25, 22, np.nan],
    'Weight': [60, np.nan, 70, 65, 55],
    'Blood Pressure': [120, 130, np.nan, 125, 115]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Weight'] = df['Weight'].fillna(df['Weight'].mean())
df['Blood Pressure'] = df['Blood Pressure'].fillna(df['Blood Pressure'].mean())

df = df[df['Name'].notnull()]

print("\nUpdated DataFrame:")
print(df)
