import pandas as pd

def clean_data():
    # Load the data
    !pip install pandas
    data_path = 'data/eu_life_expectancy_raw.tsv'
    df = pd.read_csv(data_path, sep='\t')
    
    # Unpivot the date to long format
    df = df.melt(id_vars=['unit', 'sex', 'age', 'region'], var_name='year', value_name='value')
    
    # Convert year to integer
    df['year'] = df['year'].str.extract('(\d+)').astype(int)
    
    # Convert value to float and remove NaNs
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna(subset=['value'])
    
    # Filter data for region PT (Portugal)
    df = df[df['region'] == 'PT']
    
    # Save the resulting dataframe to pt_life_expectancy.csv
    output_path = 'data/pt_life_expectancy.csv'
    df.to_csv(output_path, index=False)