import pandas as pd

# Load your CSV
df = pd.read_csv("NGA_RTFP_mkt_2007_2025-06-16.csv")

# Convert price_date to datetime
df['price_date'] = pd.to_datetime(df['price_date'])

# Filter for Lagos and date range
lagos_bread = df[
    (df['adm1_name'] == 'Lagos') &
    (df['price_date'] >= '2020-01-01') &
    (df['price_date'] <= '2025-12-31')
]

# Keep only relevant columns
bread_filtered = lagos_bread[[
    'price_date', 'mkt_name', 'bread', 'c_bread', 'inflation_bread', 'trust_bread'
]]

# Save result (optional)
bread_filtered.to_csv("lagos_bread_2020_2025.csv", index=False)

# Preview
print(bread_filtered.head())
