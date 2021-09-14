import pandas as pd

# Create dataframe
def make_global_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = (
        df.drop(["Province/State", "Country/Region", "Lat", "Long"], axis=1)
        .sum()
        .reset_index(name=condition)
    )
    df = df.rename(columns={"index": "date"})
    return df

# Read CSV from the file named "data/daily_report.csv" and get the total of rports by countries.
daily_df = pd.read_csv("data/daily_report.csv")

totals_df = (
    daily_df[["Confirmed", "Deaths", "Recovered"]].sum().reset_index(name="count")
)
totals_df = totals_df.rename(columns={"index": "condition"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


# Take three data and make them into a framework.
conditions = ["confirmed", "deaths", "recovered"]
final_df = None

for condition in conditions:
    condition_df = make_global_df(condition)
    if final_df is None:
        final_df = condition_df
    else:
        final_df = final_df.merge(condition_df)