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