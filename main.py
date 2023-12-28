import csv

def calculate_five_day_sma(file_name: str) -> dict:
    data_list = []
    with open(file_name, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            data_list.append(row)

    closes = [float(row['Close']) for row in data_list]
    sma_5 = []
    window_5 = 5
    for i in range(len(closes)):
        if i < window_5 - 1:
            sma_5.append(None)
        else:
            sma = sum(closes[i - window_5 + 1: i + 1]) / window_5
            sma_5.append(sma)

    # Adding the SMA_5 values to the dictionaries in the 'data_list'
    for i, row in enumerate(data_list):
        if i < window_5 - 1:
            row['SMA_5'] = None
        else:
            row['SMA_5'] = sma_5[i - window_5 + 1]

    return data_list


def write_sma_to_csv(data_list: dict):
    # Writing Moving Averages (SMA) to orcl-sma.csv
    with open('orcl-sma.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Close', 'SMA_5']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data_list:
            writer.writerow({'Date': row['Date'], 'Close': row['Close'], 'SMA_5': row['SMA_5']})


def calculate_twoweeks_rsi(file_name: str) -> dict:
    data_list = []
    with open(file_name, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            data_list.append(row)

    closes = [float(row['Close']) for row in data_list]

    # Calculate price differences
    price_changes = [closes[i] - closes[i - 1] for i in range(1, len(closes))]
    upward_movements = [change if change > 0 else 0 for change in price_changes]
    downward_movements = [abs(change) if change < 0 else 0 for change in price_changes]

    # Calculate average gains and average losses over the 14-day window
    rsi_14 = []
    window = 14

    # Calculate initial average gain and average loss
    avg_gain = sum(upward_movements[:window]) / window
    avg_loss = sum(downward_movements[:window]) / window

    # Calculate RSI for subsequent days
    for i in range(window, len(closes)):
        current_upward = upward_movements[i - 1]
        current_downward = downward_movements[i - 1]

        avg_gain = ((avg_gain * 13) + current_upward) / 14
        avg_loss = ((avg_loss * 13) + current_downward) / 14

        if avg_loss == 0:  # To avoid division by zero
            rsi_14.append(100)
        else:
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            rsi_14.append(rsi)

    # Add RSI values to the dictionaries in the 'data_list'
    for i, row in enumerate(data_list):
        if i < window:
            row['RSI_14'] = None
        else:
            row['RSI_14'] = rsi_14[i - window]
    return data_list


def write_rsi_to_csv(data_list: dict):
    # Writing RSI to orcl-rsi.csv
    with open('orcl-rsi.csv', 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Close', 'RSI_14']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in data_list:
            writer.writerow({'Date': row['Date'], 'Close': row['Close'], 'RSI_14': row['RSI_14']})