# SMA-and-RSI-calculation
 
This Python script enables the computation of Simple Moving Averages (SMA) and Relative Strength Index (RSI) from a provided CSV dataset containing financial market data.

# Prerequisites
Python 3.x
CSV file containing financial data (e.g., 'orcl.csv')

# Installation
Clone the repository or download the script files.
Ensure Python 3.x is installed on your system.

# Usage:
## 1) SMA Calculation (sma_calculation.py)
1) Calculating SMA
- Use calculate_five_day_sma(file_name) from sma_calculation.py to compute the 5-day Simple Moving Average for 'Close' prices in the financial dataset.
- The function returns a dictionary containing 'Date', 'Close', and 'SMA_5' values.
2) Writing SMA to CSV:
- Use write_sma_to_csv(data_list) from sma_calculation.py to write the calculated SMA data to 'orcl-sma.csv'.
- Pass the dictionary returned by calculate_five_day_sma() to this function.


## 2) RSI Calculation (rsi_calculation.py):

1) Calculating RSI
- Use calculate_twoweeks_rsi(file_name) from rsi_calculation.py to determine the 14-day Relative Strength Index based on price fluctuations.
- The function returns a dictionary containing 'Date', 'Close', and 'RSI_14' values.

2) Writing RSI to CSV:
- Use write_rsi_to_csv(data_list) from rsi_calculation.py to write the calculated RSI data to 'orcl-rsi.csv'.
- Pass the dictionary returned by calculate_twoweeks_rsi() to this function.

-----
```
# Import functions from sma_calculation.py and rsi_calculation.py
from sma_calculation import calculate_five_day_sma, write_sma_to_csv
from rsi_calculation import calculate_twoweeks_rsi, write_rsi_to_csv

# Calculate SMA
sma_data = calculate_five_day_sma('orcl.csv')

# Write SMA to CSV
write_sma_to_csv(sma_data)

# Calculate RSI
rsi_data = calculate_twoweeks_rsi('orcl.csv')

# Write RSI to CSV
write_rsi_to_csv(rsi_data)
```