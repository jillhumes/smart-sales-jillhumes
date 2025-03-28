"""
Module 3: Data Preparation Script
File: scripts/prepare_customers_data.py

This script is copied from the example given but includes only the customers_data portion. 
Minor modifications were made to the code based on the errors I introduced to the raw data. 

This script loads raw CSV files from the 'data/raw/' directory, cleans and prepares each file, 
and saves the prepared data to 'data/prepared/'.
The data preparation steps include removing duplicates, handling missing values, 
trimming whitespace, and more.
"""

import pathlib
import sys
import pandas as pd

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402
from scripts.data_scrubber import DataScrubber  # noqa: E402

# Constants
DATA_DIR: pathlib.Path = PROJECT_ROOT.joinpath("data")
RAW_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("raw")
PREPARED_DATA_DIR: pathlib.Path = DATA_DIR.joinpath("prepared")

def read_raw_data(file_name: str) -> pd.DataFrame:
    """Read raw data from CSV."""
    file_path: pathlib.Path = RAW_DATA_DIR.joinpath(file_name)
    return pd.read_csv(file_path)

def save_prepared_data(df: pd.DataFrame, file_name: str) -> None:
    """Save cleaned data to CSV."""
    file_path: pathlib.Path = PREPARED_DATA_DIR.joinpath(file_name)
    df.to_csv(file_path, index=False)
    logger.info(f"Data saved to {file_path}")

def main() -> None:
    """Main function for pre-processing customer, product, and sales data."""
    logger.info("======================")
    logger.info("STARTING data_prep.py")
    logger.info("======================")

    logger.info("========================")
    logger.info("Starting CUSTOMERS prep")
    logger.info("========================")

    df_customers = read_raw_data("customers_data.csv")

    df_customers.columns = df_customers.columns.str.strip()  # Clean column names
    df_customers = df_customers.drop_duplicates()            # Remove duplicates

    df_customers['Name'] = df_customers['Name'].str.strip()  # Trim whitespace from column values
    df_customers = df_customers.dropna(subset=['CustomerID', 'Name'])  # Drop rows missing critical info

    scrubber_customers = DataScrubber(df_customers)
    scrubber_customers.check_data_consistency_before_cleaning()
    scrubber_customers.inspect_data()
    
    df_customers = scrubber_customers.handle_missing_data(fill_value="N/A")
    #df_customers = scrubber_customers.parse_dates_to_add_standard_datetime('JoinDate')
    scrubber_customers.check_data_consistency_after_cleaning()

    save_prepared_data(df_customers, "customers_data_prepared.csv")
   
    logger.info("======================")
    logger.info("FINISHED data_prep.py")
    logger.info("======================")

if __name__ == "__main__":
    main()