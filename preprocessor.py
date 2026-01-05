import pandas as pd
# Preprocess dataset
def preprocess():
    athletes = pd.read_csv("athlete_events.csv.zip")
    regions = pd.read_csv("noc_regions.csv")

    df = athletes.merge(regions, on="NOC", how="left")
    df.drop_duplicates(inplace=True)

    # Standardize column names
    df.rename(columns={"region": "Country"}, inplace=True)
    return df