# Intern Details

Name: Riya Chauhan

Intern ID: CTIS2027

Domain: Data Analytics

Duration : 12 weeks

Mentor: Neela Santhosh Kumar

# Project Overview

This project analyzes the BigMart sales dataset (Train.csv) using Python and Dask to perform large-scale data processing efficiently. The main goal of this task is to demonstrate how Big Data tools like Dask can handle large datasets faster than traditional tools like Pandas. Dask enables parallel computing and distributed data processing, which allows operations to run on partitions of data simultaneously, making the analysis scalable and efficient.

The dataset contains information about sales across multiple outlets and different product categories. By processing this dataset, the project aims to extract meaningful insights about sales performance, outlet efficiency, and product category trends. Understanding these insights can help business managers make data-driven decisions regarding inventory, marketing strategies, and resource allocation.

Using Dask, we load the data, inspect its structure, and perform aggregation and visualization to identify patterns in sales. This project is designed for beginners to learn Big Data concepts in a practical context, including data partitioning, parallel computation, and visualization of results.

# Dataset

File: Train.csv

Total records: 8523

Key columns: Item_Identifier, Item_Weight, Item_MRP, Outlet_Type, Item_Type, Item_Outlet_Sales


# Analysis Performed

Loaded dataset using Dask DataFrame, which allows efficient handling of large datasets by partitioning them into smaller chunks

Displayed first 5 rows to inspect structure and confirm correct loading

Calculated the total number of rows to verify dataset size

Computed average Item MRP (Maximum Retail Price) to understand product pricing trends

Calculated total sales by outlet type to determine top-performing outlets

Calculated average sales by item type to understand category performance

Created a bar chart for sales by outlet type for visual analysis of trends

Saved the chart as Sales_by_outlet.png for easy reference


# Key Insights

Supermarket Type1 has the highest total sales, showing that it is the most successful outlet in terms of revenue generation

Starchy Foods category has the highest average sales, indicating strong customer demand and potential focus for marketing or stock planning

These insights can guide business decisions such as promotional strategies, inventory management, and understanding customer preferences. By analyzing sales data, businesses can optimize operations and focus on high-performing categories and outlets to increase profitability.

# Tools & Technologies Used

Python

Dask (for large-scale data processing)

Pandas (for smaller data manipulations if needed)

Matplotlib (for visualization of sales data)

# Project Files

analysis.py → Main file to run project

train.csv → Dataset

Sales_by_outlet.png → Graph output

README.md → Project description

Output Screenshot

# How to Run

Open terminal

Install required libraries:

pip install dask pandas matplotlib

# Run the main file:

python analysis.py

The program will display key calculations in terminal and save a bar chart image (Sales_by_outlet.png)
