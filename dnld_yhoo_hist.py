import requests
import datetime
import argparse
import os

class Download():
    ''' Download Yahoo History '''
    def _init_(self) :
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    
    def getArguments(self, ):
        ''' Get the arguments from command line and parse them '''
        argParser = argparse.ArgumentParser()
        argParser.add_argument("-s", "--symbol", help="symbol name", required=True)
        argParser.add_argument("-st", "--start", help="start date format would be yyyy-mm-dd", type=self.valid_date, required=True)
        argParser.add_argument("-ed", "--end", help="end date format would be yyyy-mm-dd", type=self.valid_date, required=True)
        argParser.add_argument("-it", "--interval", help="interval", choices=['1d', '1wk', '1mo'], required=True)
        argParser.add_argument("-e", "--events", help="events", choices=['history', 'div', 'split', 'capitalGain'], required=True)
        argParser.add_argument("-a", "--adjusted", help="includeAdjustedClose", choices=['true','false'], required=True)
        argParser.add_argument("-d", "--download", help="download folder location", default=None)
        self.args = argParser.parse_args()
        # print(self.args,'args')
        self.symbol = self.args.symbol
        self.interval=self.args.interval
        self.events=self.args.events
        self.includeAdjustedClose=self.args.adjusted
        self.period1=self.args.start
        self.period2=self.args.end

    def valid_date(self, s):
        ''' Date format (%Y-%m-%d) validation and convert to timestamp'''
        try:
            return int(datetime.datetime.strptime(s, "%Y-%m-%d").timestamp())
        except ValueError:
            msg = "not a valid date/format: {0!r} and accepted format is %Y-%m-%d".format(s)
            raise argparse.ArgumentTypeError(msg)

    def validateArguments(self, ):
        ''' validate the arguments '''
        start = self.args.start
        try:
            self.period1=int(datetime.datetime.strptime(start, '%Y-%m-%d').timestamp())
        except Exception as e:
            print("Invalid start date format and accepted format would be %Y-%m-%d")
            raise Exception("Invalid start date format and accepted format would be %Y-%m-%d")
        end = self.args.end
        try:
            self.period2=int(datetime.datetime.strptime(end, '%Y-%m-%d').timestamp())
        except Exception as e:
            print("Invalid end date format and accepted format would be %Y-%m-%d")
            raise Exception("Invalid end date format and accepted format would be %Y-%m-%d")

    def download(self):
        ''' download data '''
        downloadurl = f'https://query1.finance.yahoo.com/v7/finance/download/{self.symbol}?period1={self.period1}&period2={self.period2}&interval={self.interval}&events={self.events}&includeAdjustedClose={self.includeAdjustedClose}'
        result = requests.get(downloadurl, headers=self.headers)
        if self.args.download:
            d_path = os.path.join(self.args.download, datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'_'+self.symbol+'.csv')
        else:
            d_path = os.path.join(os.path.dirname(_file), datetime.datetime.now().strftime('%Y%m%d%H%M%S') +'' +self.symbol+'.csv')
        if result.status_code==200:
            with open(d_path, "w") as f_w:
                f_w.write(result.content.decode())
        else:
            print("Failed to download data for the given symbol and the error is", result.content , self.symbol, " may not be found!")

    def run(self):
        self.getArguments()
        # self.validateArguments()
        self.download()

if __name__ == '_main_':
    ref = Download()
    ref.run()