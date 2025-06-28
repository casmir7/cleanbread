🍞 Lagos Bread Price Filter (2020–2025)

This script filters and extracts bread price data for Lagos, Nigeria from a larger national food price dataset between 2020 and 2025.

📌 Features
	•	Loads a raw food price dataset CSV.
	•	Filters for:
	•	Lagos State (adm1_name == "Lagos")
	•	Date range: 2020-01-01 to 2025-12-31
	•	Keeps only relevant bread-related columns.
	•	Optionally saves the filtered data to a new CSV.

🔧 Requirements
	•	Python 3.7+
	•	pandas

Install with:

pip install pandas

📂 Input

Ensure the dataset is named:

NGA_RTFP_mkt_2007_2025-06-16.csv

Required Columns:
	•	adm1_name
	•	price_date
	•	mkt_name
	•	bread
	•	c_bread
	•	inflation_bread
	•	trust_bread

🚀 Usage

python script_name.py

This will create a file named:

lagos_bread_2020_2025.csv

containing the filtered dataset.

🔍 Sample Output

   price_date     mkt_name  bread  c_bread  inflation_bread  trust_bread
0  2020-01-15  Mushin Mkt     320     310              340          0.9
1  2020-02-15  Mushin Mkt     330     320              350          0.8
...
