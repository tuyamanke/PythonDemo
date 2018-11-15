import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style

start = datetime.datetime(2018, 1, 1)
end = datetime.datetime(2018, 11, 22)

df = web.DataReader("AAPL", "yahoo", start, end)

style.use('fivethirtyeight')

print(df.head(5))
df['High'].plot()
plt.legend()
plt.show()
