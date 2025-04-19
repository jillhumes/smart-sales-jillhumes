"""
Module 6: OLAP Goal Script (uses cubed results)
File: scripts/olap_goals_sales_by_month.py

This script uses our precomputed cubed data set to get the information 
we need to answer a specific business goal. 

GOAL: Identify variation in month-to-month sales to identify trends, if any, in total monthly sales.  

ACTION: Understanding the volatility in monthly sales allows for better forecasting of cash flows.

PROCESS: 
Group transactions by month.
Sum SaleAmount for each month.
Identify the lowest month, highest month, and monthly average.

This script assumes a cube data set with the following column names.
Month, MonthName, sale_amount_usd_sum,sale_amount_usd_mean,sale_amount_usd_min, sale_amount_usd_max,sale_id_count, sale_ids
"""

import pandas as pd
import matplotlib.pyplot as plt
import pathlib
import sys

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from utils.logger import logger  # noqa: E402

# Constants
OLAP_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("olap_cubing_outputs")
CUBED_FILE: pathlib.Path = OLAP_OUTPUT_DIR.joinpath("monthlysales_olap_cube.csv")
RESULTS_OUTPUT_DIR: pathlib.Path = pathlib.Path("data").joinpath("results")

# Create output directory for results if it doesn't exist
RESULTS_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_olap_cube(file_path: pathlib.Path) -> pd.DataFrame:
    """Load the precomputed OLAP cube data."""
    try:
        cube_df = pd.read_csv(file_path)
        logger.info(f"OLAP cube data successfully loaded from {file_path}.")
        return cube_df
    except Exception as e:
        logger.error(f"Error loading OLAP cube data: {e}")
        raise

def analyze_sales_by_month(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by Month."""
    try:
        # Group by Month (numeric) and sum the sales
        sales_by_month = (
            cube_df.groupby("Month")["sale_amount_usd_sum"].sum().reset_index()
        )
        sales_by_month.rename(columns={"sale_amount_usd_sum": "TotalSales"}, inplace=True)
        sales_by_month.sort_values(by="TotalSales", inplace=True)
        logger.info("Sales aggregated by Month successfully.")
        return sales_by_month
    except Exception as e:
        logger.error(f"Error analyzing sales by Month: {e}")
        raise

def analyze_sales_by_month_name(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate total sales by Month."""
    try:
        # Group by Month (name) and sum the sales
        sales_by_month_name = (
            cube_df.groupby("MonthName")["sale_amount_usd_sum"].sum().reset_index()
        )
        sales_by_month_name.rename(columns={"sale_amount_usd_sum": "TotalSales"}, inplace=True)
        sales_by_month_name.sort_values(by="TotalSales", inplace=True)
        logger.info("Sales aggregated by Month successfully.")
        return sales_by_month_name
    except Exception as e:
        logger.error(f"Error analyzing sales by Month: {e}")
        raise

def analyze_sales_by_product_month(cube_df: pd.DataFrame) -> pd.DataFrame:
    """Identify the product with the highest revenue for each month."""
    try:
        # Group by Month and product_id, sum the sales
        top_products = (cube_df.groupby(["Month", "product_id"])["sale_amount_usd_sum"].sum().reset_index()
        )
        top_products.rename(columns={"sale_amount_usd_sum": "TotalSales"}, inplace=True)
        top_products.sort_values(["Month", "TotalSales"], ascending=[True, False]).groupby("Month").head(1)
        logger.info("Top products identified for each month.")
        return top_products
    except Exception as e:
        logger.error(f"Error analyzing top product by Month: {e}")
        raise

def identify_least_profitable_month(sales_by_month: pd.DataFrame) -> str:
    """Identify the month with the lowest total sales."""
    try:
        least_profitable_month = sales_by_month.iloc[0]
        logger.info(
            f"Least profitable month: {least_profitable_month['MonthName']} with total sales of ${least_profitable_month['TotalSales']:.2f}."
        )
    except Exception as e:
        logger.error(f"Error identifying least profitable month: {e}")
        raise

def identify_most_profitable_month(sales_by_month: pd.DataFrame) -> str:
    """Identify the month with the highest total sales."""
    try:
        most_profitable_month = sales_by_month.iloc[9]
        logger.info(
            f"Most profitable month: {most_profitable_month['MonthName']} with total sales of ${most_profitable_month['TotalSales']:.2f}."
        )
    except Exception as e:
        logger.error(f"Error identifying most profitable month: {e}")
        raise

def visualize_sales_by_month(sales_by_month: pd.DataFrame) -> None:
    """Visualize total sales by month."""
    try:
        plt.figure(figsize=(10, 6))
        plt.bar(
            sales_by_month["Month"],
            sales_by_month["TotalSales"],
            color="skyblue",
        )
        plt.title("Total Sales by Month", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_month.png")
        plt.savefig(output_path)
        logger.info(f"Visualization saved to {output_path}.")

    except Exception as e:
        logger.error(f"Error visualizing sales by month: {e}")
        raise

def visualize_sales_by_product_month(cube_df: pd.DataFrame) -> None:
    """Visualize total sales by month, broken down by product."""
    try:
        # Pivot the data to organize sales by Month and ProductID
        sales_pivot = cube_df.pivot_table(
            index="Month",
            columns="product_id",
            values="sale_amount_usd_sum",
            aggfunc="sum",
            fill_value=0
        )

        # Plot the stacked bar chart
        sales_pivot.plot(
            kind="bar",
            stacked=True,
            figsize=(12, 8),
            colormap="tab10"
        )

        plt.title("Total Sales by Month and Product", fontsize=16)
        plt.xlabel("Month", fontsize=12)
        plt.ylabel("Total Sales (USD)", fontsize=12)
        plt.xticks(rotation=45)
        plt.legend(title="Product ID", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()

        # Save the visualization
        output_path = RESULTS_OUTPUT_DIR.joinpath("sales_by_month_and_product.png")
        plt.savefig(output_path)
        logger.info(f"Stacked bar chart saved to {output_path}.")
  
    except Exception as e:
        logger.error(f"Error visualizing sales by day and product: {e}")
        raise



def main():
    """Main function for analyzing and visualizing sales data."""
    logger.info("Starting SALES_LOW_REVENUE_MONTH analysis...")

    # Step 1: Load the precomputed OLAP cube
    cube_df = load_olap_cube(CUBED_FILE)

    # Step 2: Analyze total sales by MonthName
    sales_by_month = analyze_sales_by_month_name(cube_df)

    # Step 3: Identify the least & most profitable month by name
    least_profitable_month = identify_least_profitable_month(sales_by_month)
    most_profitable_month = identify_most_profitable_month(sales_by_month)
    logger.info("Close the Figure to complete this script.")

    # Step 4: Analyze total sales by Month
    sales_by_month = analyze_sales_by_month(cube_df)

    # Step 5: Visualize total sales by Month
    visualize_sales_by_month(sales_by_month)
    logger.info("Analysis and visualization completed successfully.")
   
    # Step 6: Analyze total sales by Product & Month
    top_products = analyze_sales_by_product_month(cube_df)
    logger.info("Analysis completed successfully.")
    print(top_products)

    # Step 7: Visualize total sales by Product & Month
    visualize_sales_by_product_month(cube_df)
    logger.info("Analysis and visualization completed successfully.")

   # Step 8: Show Visualizes on screen
    plt.show()

if __name__ == "__main__":
    main()