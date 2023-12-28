from sma_calculation import calculate_five_day_sma, write_sma_to_csv
from rsi_calculation import calculate_twoweeks_rsi, write_rsi_to_csv

def main():
    # Calculate SMA
    sma_data = calculate_five_day_sma('orcl.csv')

    # Write SMA to CSV
    write_sma_to_csv(sma_data)

    # Calculate RSI
    rsi_data = calculate_twoweeks_rsi('orcl.csv')

    # Write RSI to CSV
    write_rsi_to_csv(rsi_data)

if __name__ == "__main__":
    main()