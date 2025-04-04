# smart-sales-jillhumes

Initialization of the smart sales project in Module 2

-----

## Set-up remote repository on GitHub
-	Naming Guidelines: use all lowercase and dashes between words
-	Add brief description
-	Select “Public” option
-	Add default README file
-	Create repository

## Clone GitHub repository to local machine
-	Open new terminal in VS Code
-	Copy <URL> from GitHub

```shell
git clone <URL>
```

## Create files .gitignore and requirements.txt
-	Copy file contents from starter repo provided

## Create and activate virtual environment

```shell
source py -m venv .venv
```
```shell
source .venv\Scripts\activate
```

## Install Packages 

```shell
source py -m pip install --upgrade -r requirements.txt
```

## Optional: Verify .venv Setup

```shell
py -m datafun_venv_checker.venv_checker
```

## Create data and data\raw folders then get data tables
-	Copy raw data files from starter repo

## Create data\prepared folder

## Create scripts data_scrubber.py and data_prep.py
-	Copy file contents from starter repo provided

## Create tests folder and script test_data_scrubber.py 
-	Copy file contents from starter repo provided

## Execute test script to confirm data_scrubber.py runs without error

```shell
py tests/test_data_scrubber.py
```

## Create unique data prep script for each raw data set
-	Use data_prep.py as starting point and modify as needed

## Execute data prep scripts

```shell
py scripts/prepare_customers_data.py
py scripts/prepare_products_data.py
py scripts/prepare_sales_data.py
```

## Create & Execute script to 
### (1) Create data warehouse with dimension tables (customer & product) and fact tables (sale)
- customer schema:
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    region TEXT,
    join_date TEXT,
    loyalty_points INTEGER,
    preferred_contact_method TEXT

- product schema:    
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL,
    stock_quantity INTEGER,
    bin_number TEXT

- sale schema:
    sale_id INTEGER PRIMARY KEY,
    sale_date TEXT,
    customer_id INTEGER,
    product_id INTEGER,
    store_id INTEGER,
    campaign_id INTEGER,
    sale_amount_usd REAL,
    discount_percent REAL,
    payment_type TEXT,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id)

### (2) Load data into data warehouse
- Use sample code from "P4. Create and Populate DW" as starting point and modify as needed
- Modifications include:
  - Rename dataframe columns to match the database schema
  - add error processing using try...except keywords

```shell
py scripts/etl_to_dw.py
```

## Run add-commit-push to push new files to GitHub

```shell
git add .
git commit -main “add starter files”
git push -u origin main
```

-----

## Initial Package List

- pip
- loguru
- ipykernel
- jupyterlab
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- pyspark==4.0.0.dev1
- pyspark[sql]
- git+https://github.com/denisecase/datafun-venv-checker.git#egg=datafun_venv_checker