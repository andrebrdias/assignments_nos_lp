"""Run Main Fuction
"""

import argparse
from life_expectancy.cleaning import load_data, clean_data, save_data

def main(region: "PT"):
    """Main Function to Run the Pipeline
        Args:
        region (_type_): _description_
    """
    prepared_df = load_data()
    cleaned_df = clean_data(prepared_df, region)
    save_data(cleaned_df)

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default = 'PT', help = "Provide a Region code (default = PT)")
    args = parser.parse_args()

    main(args.region)
