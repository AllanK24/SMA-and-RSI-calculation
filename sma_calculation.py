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
