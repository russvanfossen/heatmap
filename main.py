from tracemalloc import start
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import pandas_datareader as web

start = dt.datetime(2018,1,1)
end = dt.datetime.now()

tickers = ['^GSPC', '^TNX', 'XOP', 'GLD']
colnames = []

for ticker in tickers:
    data = web.DataReader(ticker, 'yahoo', start, end)
    if len(colnames) == 0:
        combined = data[['Adj Close']].copy()
    else:
        combined = combined.join(data['Adj Close'])
    colnames.append(ticker)
    combined.columns = colnames

# plt.yscale('log')

# for ticker in tickers:
#     plt.plot(combined[ticker], label=ticker)

# plt.legend(loc='upper right')


# plt.show()

corr_data = combined.pct_change().corr(method='pearson')
sns.heatmap(corr_data, annot=True, cmap='coolwarm')
plt.show()