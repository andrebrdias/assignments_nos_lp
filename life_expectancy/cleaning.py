"""
Cleaning data from a tsv file.
"""

import pandas as pd

def clean_data(region: str):
    """Function used to clean data"""

    # Data Collection
    data = 'life_expectancy/data/eu_life_expectancy_raw.tsv'
    df_data = pd.read_csv(data, delimiter='\t')
    # Prepare the data
    df_data = df_data.melt(id_vars='unit,sex,age,region', var_name='year', value_name='value')

    df_values = df_data[['year', 'value']]
    df_key = df_data[['unit,sex,age,region']]

    df_key[['unit','sex','age','region']] = df_key['unit,sex,age,region'] \
    .str.split(",", expand = True)
    df_key.drop(columns=['unit,sex,age,region'], inplace=True)

    df_joined = df_key.join(df_values)

    # Perform Data Cleaning:
    #   - Convert year to integer
    #   - Convert value to float and remove NaNs
    #   - Filter data for region PT (Portugal)
    df_joined['year'] = df_joined['year'].str.extract('(\d+)').astype(int)
    df_joined['value'] = pd.to_numeric(df_joined['value'], errors='coerce')
    df_joined = df_joined.dropna(subset=['value'])
    df_joined = df_joined[df_joined['region'] == 'PT']
    # Save the resulting dataframe to pt_life_expectancy.csv
    output_path = 'life_expectancy/data/pt_life_expectancy.csv'
    df_joined.to_csv(output_path, index=False)
