# Pandas: Select Rows between two values in DataFrame

import pandas as pd


df = pd.DataFrame({
    'name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'experience': [1, 3, 5, 7],
    'salary': [175.1, 180.2, 190.3, 205.4],
})

print(df)

print('-' * 50)

output = df[df['salary'].between(180, 200)]

print(output)