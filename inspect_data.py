import pandas as pd
import os

file_path = "ecommerce_analytics (1).xlsx"
if os.path.exists(file_path):
    print("File exists!")
    try:
        df = pd.read_excel(file_path)
        print("Columns in Excel:")
        print(df.columns.tolist())
        print("\nShape of DataFrame:", df.shape)
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 rows:")
        print(df.head())
    except Exception as e:
        print("Error reading excel:", e)
else:
    print("File does not exist!")
