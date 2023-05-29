"""
Cleaning data from a tsv file.
"""
import pandas as pd


def load_data() -> pd.DataFrame:
    """Function to load the tsv file

    Returns:
        pd.DataFrame: _description_
    """
    # Data Collection
    data = 'life_expectancy/data/eu_life_expectancy_raw.tsv'
    return pd.read_csv(data, delimiter='\t')


def clean_data(df_data: pd.DataFrame, region: str) -> pd.DataFrame:
    """Function used to clean data

    Args:
        region (str): _description_
    """
     df_data.columns =  [
        col.replace("\\","") for col
        in df_data.columns
        ]

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
    df_joined['year'] = df_joined['year'].str.extract(r'(\d+)').astype(int)
    df_joined['value'] = pd.to_numeric(df_joined['value'], errors='coerce')
    df_joined = df_joined.dropna(subset=['value'])
    df_joined = df_joined[df_joined['region'] == region]
    return df_joined


def save_data(df_data: pd.DataFrame) -> None:
    """_summary_

    Args:
        df (pd.DataFrame): _description_
        output_path (str): _description_
    """

    # Save the resulting dataframe to pt_life_expectancy.csv
    output_path = 'life_expectancy/data/pt_life_expectancy.csv'
    df_data.to_csv(output_path, index=False)
