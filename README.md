# smart-sales-jillhumes

Initialization of the smart sales project in Module 2

-----

## Step 1: Set-up remote repository on GitHub
-	Naming Guidelines: use all lowercase and dashes between words
-	Add brief description
-	Select “Public” option
-	Add default README file
-	Create repository

## Step 2: Clone GitHub repository to local machine
-	Open new terminal in VS Code
-	Copy <URL> from GitHub

```shell
git clone <URL>
```

## Step 3: Create files .gitignore and requirements.txt
-	Copy file contents from starter repo provided

## Step 4: Create and activate virtual environment

```shell
source py -m venv .venv
```
```shell
source .venv\Scripts\activate
```

## Step 5: Install Packages 

```shell
source py -m pip install --upgrade -r requirements.txt
```

## Step 6 (Optional): Verify .venv Setup

```shell
py -m datafun_venv_checker.venv_checker
```

## Step 7: Create data and data\raw folders then get data tables
-	Copy customers_data.csv from smart-store-jillhumes repo
-	Copy products_data.csv from smart-store-jillhumes repo
-	Copy sales_data.csv from smart-store-jillhumes repo

## Step 8: Execute the initial project script

```shell
py scripts/data_prep.py
```

## Final Step: Run add-commit-push to push new files to GitHub

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