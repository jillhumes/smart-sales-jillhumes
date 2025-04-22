# P7. Custom BI Project (smart-sales-jillhumes)
## Section 1. The Business Goal
The goal is to identify the most profitable product, in terms of profit per unit and total profits based on sales.

## Section 2. Data Source
### Create raw data files 
Used the raw data from the sample repository as a starting point.  Modifications include:
customers_data_P7: none
products_data_P7: additional columns for UnitCost and UnitProfit
sales_data_P7: additional column for SaleMonth

### Create prepared data files by running data prep scripts
Used "prepare_XXX_data.py" files as starting point. Modifications include:
prepare_customers_data_P7.py
    updated file names for customers_data_P7.csv and customers_data_P7_prepared.csv
    updated file path to P7/data
    removed references to data_scrubber
```shell
py P7/scripts/prepare_customers_data_P7.py
```
prepare_products_data_P7.py
    updated file names for products_data_P7.csv and products_data_P7_prepared.csv
    updated file path to P7/data
    removed references to data_scrubber   
```shell
py P7/scripts/prepare_products_data_P7.py
```
prepare_sales_data_P7.py
    updated file names for sales_data_P7.csv and sales_data_P7_prepared.csv
    updated file path to P7/data
    removed references to data_scrubber    
```shell
py P7/scripts/prepare_sales_data_P7.py
```
### Create data warehouse
Used "etl_to_dw.py" script as starting point. Modifications include:
  - Rename dataframe columns to match the database schema

Schema for dimension tables (customer & product) and fact table (sale)
- customer schema:
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT,
    join_date TEXT,
- product schema:    
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL,
    unit_cost REAL,
    unit_profit REAL
- sale schema:
    sale_id INTEGER PRIMARY KEY,
    sale_date TEXT,
    sale_month TEXT
    customer_id INTEGER,
    product_id INTEGER,
    store_id INTEGER,
    campaign_id INTEGER,
    sale_amount_usd REAL,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
```shell
py scripts/etl_to_dw_P7.py
```

## Section 3. Tools Used
## Section 4. Workflow & Logic
## Section 5. Results (narrative + visualizations)
## Section 6. Suggested Business Action
## Section 7. Challenges
## Section 8. Ethical Considerations