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

# Change your Jupyter themes.

- If you don't like your Jupyter theme, you can change it after you install jupyterthemes.


1. Install jupytertheme
```py
pip install jupyterthemes
```
2. Set the theme
```py
jt -t monokai
# Change a theme to monokai.
```

# Setting up Time confirmed. 


1. Take the sum().
```py
import pandas as pd
df = pd.read_csv("data/time_confirmed.csv")
df = df.sum()
df
```
- sum only Latitude and Longitude as well which is what we do not want. 

2. In order to drop some headers you do below, you use .drop().

```py
import pandas as pd
df = pd.read_csv("data/time_confirmed.csv")
df = df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum()
df
```
Output:
1/22/20          557
1/23/20          655
1/24/20          941
1/25/20         1433
1/26/20         2118
             ...    
9/4/21     220348745
9/5/21     220775393
9/6/21     221211222
9/7/21     221932892
9/8/21     222559803
Length: 596, dtype: int64

*We do not want series because the visualization only work with dataframe.*

3. Make it look like an excel by adding .reset_index(name="total")

```py
import pandas as pd
df = pd.read_csv("data/time_confirmed.csv")
# Make like an excel spreadsheet
df = df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name="total")

# Set the column name
df = df.rename(columns={'index': 'date'})
df
```
Output:
	date	total
0	1/22/20	557
1	1/23/20	655
2	1/24/20	941
3	1/25/20	1433
4	1/26/20	2118
...	...	...
591	9/4/21	220348745
592	9/5/21	220775393
593	9/6/21	221211222
594	9/7/21	221932892
595	9/8/21	222559803
596 rows × 2 columns

# Integrate Deaths, Confirmed and Recovered Data

1. Iterate each data and make them into a dataframe. 

```py
import pandas as pd

# Get data from three sources. 
conditions = ["confirmed", "deaths", "recovered"]

def make_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    # Make like an excel spreadsheet
    df = df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1).sum().reset_index(name="total")

    # Set the column name
    df = df.rename(columns={'index': 'date'})
    return df

# Iterate each data and make them into a dataframe.
for condition in conditions:
    condition_df = make_df(condition)
    print(condition_df)
```
Output:

        date      total
0    1/22/20        557
1    1/23/20        655
2    1/24/20        941
3    1/25/20       1433
4    1/26/20       2118
..       ...        ...
591   9/4/21  220348745
592   9/5/21  220775393
593   9/6/21  221211222
594   9/7/21  221932892
595   9/8/21  222559803

[596 rows x 2 columns]
        date    total
0    1/22/20       17
1    1/23/20       18
2    1/24/20       26
3    1/25/20       42
4    1/26/20       56
..       ...      ...
591   9/4/21  4561905
592   9/5/21  4568372
593   9/6/21  4576291
594   9/7/21  4586158
595   9/8/21  4596394

[596 rows x 2 columns]
        date  total
0    1/22/20     30
1    1/23/20     32
2    1/24/20     39
3    1/25/20     42
4    1/26/20     56
..       ...    ...
591   9/4/21      0
592   9/5/21      0
593   9/6/21      0
594   9/7/21      0
595   9/8/21      0

[596 rows x 2 columns]

2. Combine data.
- Look at pandas documentation and see the get started guide.
a. Merge
b. Concat
- *Merge:* merge dataframes. 

- When the dataframe is returned, merge with the previous ones. 

```py

final_df = None

for condition in conditions:
    condition_df = make_df(condition)
    # This will set the first one to be final_df
    if final_df is None:
        final_df = condition_df
    # this will take leftover df and merge with the final_df
    else:
        final_df = final_df.merge(condition_df)
final_df
```

3. Final product
- finally, you will get the data below:

```py
import pandas as pd
# Get data from three sources. 
conditions = ["confirmed", "deaths", "recovered"]
final_df = None

def make_global_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = (
        df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
        .sum()
        .reset_index(name=condition)
    )
    df = df.rename(columns={"index": "date"})
    return df

for condition in conditions:
    condition_df = make_global_df(condition)
    if final_df is None:
        final_df = condition_df
    else:
        final_df = final_df.merge(condition_df)
        
final_df
```

# Get daily cases in the country

1. Get a column by "Country" column

```py
df = pd.read_csv("data/time_confirmed.csv")

# Locate a specific column that matches the condition provided.
df = df.loc[df["Country/Region"] == "Afghanistan"]
df = df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum().reset_index(name="confirmed")
df = df.rename(columns={'index':"date"})
df
```
- Use method called .loc to locate a row that matches a boolean value.

2. Modulize the code by making them into a function

```py
def make_country_df(condition, country):
    df= pd.read.csv("data/time_confirmed.csv")
    df = df.loc[df["Country/Region"]== "Afghanistan"]
    df = df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"]).sum().reset_index(name="confirmed")
    df = df.rename(columns={'index':'date'})
    return df
```

3. Final Recap

- This is created so that the user can select country by a dropdown menu to get the Confirmed, Recovered, Deaths cases by a linear graph. 

# Code refactoring

- Modulization

# Create a Dashboard

1. Build a dashboard using Dash
- Dash runs on top of Flask. 

Default plotly Dashboard code:
```py
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

2. Create a layout - put HTML on the screen.

- you can create an HTML element using the function .layout

```py
app.layout = html.Div(
    html.H1("Hello Dash!")
)
```

- use HTML style

```py
app.layout = html.Div(
    html.H1("Corona Dashboard"), style={"textAlign":"center", "minHeight": "100vh", "backgroundColor":"black", "color":"white"}
)
```

- Create a header with style.
```py
# import external stylesheet that reset the css and Google fonts.
stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily":"Open Sans, sans-serif",
    },
    children =[
        html.Header(
            style={"textAlign":"center", "paddingTop": "50px"},
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})],
        )
    ]
)
```

3. Create divs and tables

In order to create the HTML table as below:
```html
<table>
    <thead>
        <tr>
            <th colspan="2">The table header</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>The table body</td>
            <td>with two columns</td>
        </tr>
    </tbody>
</table>

```
you can use Dash function to create each elements
```py
app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily":"Open Sans, sans-serif",
    },
    children =[
        html.Header(
            style={"textAlign":"center", "paddingTop": "50px"},
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})],
        ),
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Table(
                            children=[
                                html.Thead(
                                    children=[
                                        html.Tr(
                                            children=[
                                                # Create the header of the table on every iteration
                                                html.Th(column_name.replace("_", " "))
                                                for column_name in countries_df.columns
                                            ]
                                        )
                                    ]
                                ),
                                html.Tbody(
                                    children=[
                                        html.Tr(
                                            children=[
                                                html.Td(value_column)
                                                for value_column in value
                                            ]
                                        )
                                        for value in countries_df.values
                                    ]
                                ),
                            ]
                        )
                    ]
                )
            ]
        ),
    ],
)

```

4. Create functions that create table to clean the code

```py
```