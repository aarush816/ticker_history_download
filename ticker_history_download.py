import requests
import datetime
import argparse
import os
argParser = argparse.ArgumentParser()
argParser.add_argument("-s", "--symbol", help="symbol name")
argParser.add_argument("-st", "--start", help="start date")
argParser.add_argument("-ed", "--end", help="end date")
argParser.add_argument("-it", "--interval", help="interval")
argParser.add_argument("-e", "--events", help="events")
argParser.add_argument("-a", "--adjusted", help="includeAdjustedClose")
argParser.add_argument("-d", "--download", help="download folder location", default=None)

print("hi")

args = argParser.parse_args()
print(args,'args')

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
symbol=args.symbol
start = args.start
period1=int(datetime.datetime.strptime(start, '%Y-%m-%d').timestamp())
end = args.end
period2=int(datetime.datetime.strptime(end, '%Y-%m-%d').timestamp())
interval=args.interval
events=args.events
includeAdjustedClose=args.adjusted
downloadurl = f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={period1}&period2={period2}&interval={interval}&events={events}&includeAdjustedClose={includeAdjustedClose}'
result = requests.get(downloadurl, headers=headers)
if args.download:
    d_path = os.path.join(args.download, datetime.datetime.now().strftime('%Y%m%d%H%M%S')+'_'+symbol+'.csv')
else:
    d_path = os.path.join(os.path.dirname(__file__), datetime.datetime.now().strftime('%Y%m%d%H%M%S') +'' +symbol+'.csv')
if result.status_code==200:
    with open(d_path, "w") as f_w:
        f_w.write(result.content.decode())
else:
    print("Failed to download data for the given symbol and the error is", result.content , symbol)