import pandas as pd
import json

df = pd.read_excel("ecommerce_analytics (1).xlsx")

# Drop any nulls or clean types
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.strftime('%Y-%m-%d')
df['Year_'] = df['Year_'].astype(int)
df['Sales'] = df['Sales'].astype(float).round(2)
df['Profit'] = df['Profit'].astype(float).round(2)
df['Quantity'] = df['Quantity'].astype(int)
df['Customer ID'] = df['Customer ID'].astype(str).str.strip()
df['Segment'] = df['Segment'].astype(str).str.strip()
df['Region'] = df['Region'].astype(str).str.strip()
df['Category'] = df['Category'].astype(str).str.strip()
df['Product Name'] = df['Product Name'].astype(str).str.strip()

# We will extract columns:
# 0: Order ID
# 1: Order Date
# 2: Customer ID
# 3: Segment
# 4: Region
# 5: Category
# 6: Product Name
# 7: Sales
# 8: Profit
# 9: Year_

transactions = []
for idx, row in df.iterrows():
    transactions.append([
        row['Order ID'],
        row['Order Date'],
        row['Customer ID'],
        row['Segment'],
        row['Region'],
        row['Category'],
        row['Product Name'],
        row['Sales'],
        row['Profit'],
        int(row['Year_'])
    ])

# Let's write this to a json file
with open("transactions.json", "w", encoding="utf-8") as f:
    json.dump(transactions, f, ensure_ascii=False)

print(f"Successfully processed {len(transactions)} transactions.")
print("Sample transaction:", transactions[0])
