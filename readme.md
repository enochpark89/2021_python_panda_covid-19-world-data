# Covid-19 World Data

- This application shows the current Covid-19 data with graphics and visuals.

# Set up 

Install below applications:
1. panda
2. flake8
3. black
- These can be installed using pip install
4. plotly

# Data

Get Covid data from below repository
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data

- Check daily reports and time series. 
- Get the most recent daily report data: 09/06/2021 as of now. 
PATH: COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/08-30-2021.csv
- Get the most recent time series data.

# Development process

- **Start notebook and get Sum**

1. Open jupyter notebook
```
jupyter-notebook
```

2. Import panda

```py
import pandas as pd
```

*Data frame: It is like an excel*

3. import data using dataframe.

```
import pandas as pd
daily_df = pd.read_csv("data/daily_report.csv")
daily_df
```
- you can do this on your python console, but it looks so much better on the jupyter notebook. 

4. Get only one column

```py
daily_df["Country_Region"]
# Get only a column with the header "country_region"
```

5. Drop columns. 
```py
daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]]
```

6. Get sums
```py
daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum()
```

Make it into a table
```py
daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index()
```

Final:
```py
import pandas as pd
daily_df = pd.read_csv("data/daily_report.csv")
daily_df = daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
daily_df = daily_df.rename(columns={'index':'condition'})
```
This contains the total of columns that we need.

# Show the map and the table. 

1. Combine by country because some country contains the region also which makes it confusing overall. 

```py
countries_df = countries_df.groupby("Country_Region").sum().reset_index()
```
2. From time_confirmed.csv, get sum of confirmed cases around the world by dates. 

```py

df = pd.read_csv("data/time_confirmed.csv")
df = df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name="total")
df = df.rename(columns={'index': 'date'})
df
```

