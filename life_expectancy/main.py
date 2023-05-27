from life_expectancy.cleaning import clean_data
import argparse

def main(region: str = 'PT'):
    clean_data(region)

if __name__ == "__main__": # pragma: no cover
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", default = 'PT', help = "Provide a Region code (default = PT)")
    args = parser.parse_args()

    main(args.region)
