import pandas as pd

# Medal tally
def fetch_medal_tally(df, year, country):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    return medal_tally.groupby(['Country', 'Year']).size().reset_index(name='Medals')

# Year and country list
def country_year_list(df):
    years = df['Year'].dropna().unique().tolist()
    years.sort()
    countries = df['Country'].dropna().unique().tolist()
    countries.sort()
    return years, countries

# Data over time
def data_over_time(df, col):
    return df.drop_duplicates(['Year', col]).groupby('Year').count().reset_index()[['Year', col]].rename(columns={'Year': 'Edition'})

# Country medal tally
def yearwise_medal_tally(df, country):
    country_df = df[(df['Country'] == country) & (df['Medal'].notna())]
    return country_df.groupby('Year').size().reset_index(name='Medal')

# Country heatmap
def country_event_heatmap(df, country):
    country_df = df[(df['Country'] == country) & (df['Medal'].notna())]
    pivot = country_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pivot

# Most successful athletes per country
def most_successful_country(df, country):
    temp = df[(df['Country'] == country) & (df['Medal'].notna())]
    return temp['Name'].value_counts().reset_index().head(10).rename(columns={'index': 'Athlete', 'Name': 'Total Medals'})

# Most successful athletes per sport
def most_successful_by_sport(df, sport='Overall', top_n=10):
    medal_df = df[df['Medal'].notna() & df['Name'].notna()]
    if sport != 'Overall':
        medal_df = medal_df[medal_df['Sport'] == sport]
    return medal_df['Name'].value_counts().reset_index().head(top_n).rename(columns={'index': 'Athlete', 'Name': 'Total Medals'})


# Country-wise athlete distribution
def country_athlete_distribution(df, country):
    athlete_df = df[df['Country'] == country]
    athlete_df = athlete_df.drop_duplicates(subset=['Name', 'Sport', 'Year'])
    return athlete_df['Sport'].value_counts().reset_index().rename(columns={'index': 'Sport', 'Sport': 'No of Athletes'})

# Age distribution
def age_distribution(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'Age', 'Sport'])
    return athlete_df[['Age', 'Sport', 'Medal']].dropna()

# Height vs Weight
def height_weight_distribution(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Height', 'Weight', 'Sport'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df[['Height', 'Weight', 'Medal']]

# Weightlifting distribution
def weightlifting_distribution(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Weight', 'Sport'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df[['Weight', 'Medal']]

# Age vs Medals
def age_vs_medals(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Age', 'Sport', 'Medal'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df[['Age', 'Medal']]

# Height vs Medals
def height_vs_medals(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Height', 'Sport', 'Medal'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df[['Height', 'Medal']]

# Weight vs Medals
def weight_vs_medals(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'Weight', 'Sport', 'Medal'])
    if sport != 'Overall':
        athlete_df = athlete_df[athlete_df['Sport'] == sport]
    return athlete_df[['Weight', 'Medal']]

# Men vs Women participation over the years
def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'Year', 'Sex'])
    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').size().reset_index(name='Male')
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').size().reset_index(name='Female')
    final_df = men.merge(women, on='Year', how='outer').fillna(0)
    return final_df

# Medal tally by sport
def medal_tally_by_sport(df, sport):
    sport_df = df[(df['Sport'] == sport) & (df['Medal'].notna())]
    return sport_df.groupby('Country').size().reset_index(name='Medals').sort_values(by='Medals', ascending=False)

# Overall medal tally
def overall_medal_tally(df):
    medal_tally = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    return medal_tally.groupby('Country').size().reset_index(name='Medals').sort_values(by='Medals', ascending=False)

# Most successful athletes overall
def most_successful_athletes(df):
    athlete_df = df[df['Medal'].notna()]
    return athlete_df['Name'].value_counts().reset_index().rename(columns={'index': 'Athlete', 'Name': 'Total Medals'})

# Fetch successful athletes for a given sport
def fetch_successful_athletes(df, sport):
    temp_df = df[df['Medal'].notna() & df['Name'].notna()]
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]
    return temp_df['Name'].value_counts().reset_index().head(10).rename(columns={'index': 'Athlete', 'Name': 'Total Medals'})

# Helper function to get unique sports
def get_unique_sports(df):
    sports = df['Sport'].dropna().unique().tolist()
    sports.sort()
    sports.insert(0, 'Overall')
    return sports

# Helper function to get unique countries
def get_unique_countries(df):
    countries = df['Country'].dropna().unique().tolist()
    countries.sort()
    countries.insert(0, 'Overall')
    return countries

# Helper function to get unique years
def get_unique_years(df):
    years = df['Year'].dropna().unique().tolist()
    years.sort()
    years.insert(0, 'Overall')
    return years

# Filter dataframe for athletes with valid names
def filter_athletes_with_names(df):
    return df[df['Name'].notna()]
    