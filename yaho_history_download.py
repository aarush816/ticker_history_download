import requests
import datetime
import argparse
import os


class YahooFinanceDownloader:
    def __init__(self, symbol, start, end, interval, events, adjusted, download_folder=None):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.interval = interval
        self.events = events
        self.adjusted = adjusted
        self.download_folder = download_folder

    def download_data(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

        period1 = int(datetime.datetime.strptime(self.start, '%Y-%m-%d').timestamp())
        period2 = int(datetime.datetime.strptime(self.end, '%Y-%m-%d').timestamp())

        download_url = f'https://query1.finance.yahoo.com/v7/finance/download/{self.symbol}?period1={period1}&period2={period2}&interval={self.interval}&events={self.events}&includeAdjustedClose={self.adjusted}'

        result = requests.get(download_url, headers=headers)

        if self.download_folder:
            file_path = os.path.join(self.download_folder, datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + self.symbol + '.csv')
        else:
            file_path = os.path.join(os.path.dirname(__file__), datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '_' + self.symbol + '.csv')

        if result.status_code == 200:
            with open(file_path, "w") as f_w:
                f_w.write(result.content.decode())
        else:
            print("Failed to download data for the given symbol and the error is", result.content, self.symbol)


if __name__ == "__main__":
    argParser = argparse.ArgumentParser()
    argParser.add_argument("-s", "--symbol", help="symbol name")
    argParser.add_argument("-st", "--start", help="start date")
    argParser.add_argument("-ed", "--end", help="end date")
    argParser.add_argument("-it", "--interval", help="interval")
    argParser.add_argument("-e", "--events", help="events")
    argParser.add_argument("-a", "--adjusted", help="includeAdjustedClose")
    argParser.add_argument("-d", "--download", help="download folder location", default=None)

    args = argParser.parse_args()

    if args.start is None:
        print("Please provide a start date.")
        exit(1)

    downloader = YahooFinanceDownloader(
        symbol=args.symbol,
        start=args.start,
        end=args.end,
        interval=args.interval,
        events=args.events,
        adjusted=args.adjusted,
        download_folder=args.download
    )
    downloader.download_data()
