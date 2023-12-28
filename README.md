# SMA-and-RSI-calculation
 
This Python script enables the computation of Simple Moving Averages (SMA) and Relative Strength Index (RSI) from a provided CSV dataset containing financial market data.

# Prerequisites
Python 3.x
CSV file containing financial data (e.g., 'orcl.csv')

# Installation
Clone the repository or download the script file.
Ensure Python 3.x is installed on your system.
# Usage

- Calculating SMA:

Use calculate_five_day_sma(file_name) to compute the 5-day Simple Moving Average for 'Close' prices in the financial dataset.
The function returns a dictionary containing 'Date', 'Close', and 'SMA_5' values.
Writing SMA to CSV:

Use write_sma_to_csv(data_list) to write the calculated SMA data to 'orcl-sma.csv'.
Pass the dictionary returned by calculate_five_day_sma() to this function.

- Calculating RSI:

Use calculate_twoweeks_rsi(file_name) to determine the 14-day Relative Strength Index based on price fluctuations.
The function returns a dictionary containing 'Date', 'Close', and 'RSI_14' values.
Writing RSI to CSV:

Use write_rsi_to_csv(data_list) to write the calculated RSI data to 'orcl-rsi.csv'.
Pass the dictionary returned by calculate_twoweeks_rsi() to this function.
