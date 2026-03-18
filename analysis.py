import dask.dataframe as dd

# Load dataset
df = dd.read_csv("Train.csv", encoding="latin-1")

print("First 5 rows of dataset:")
print(df.head())

# Total rows in dataset
total_rows = df.shape[0].compute()
print("\nTotal rows:", total_rows)

# Average Item MRP
avg_mrp = df["Item_MRP"].mean().compute()
print("\nAverage Item MRP:", avg_mrp)

# Total sales by outlet type
sales_outlet = df.groupby("Outlet_Type")["Item_Outlet_Sales"].sum().compute()
print("\nSales by Outlet Type:")
print(sales_outlet)

# Average sales by item type
sales_item = df.groupby("Item_Type")["Item_Outlet_Sales"].mean().compute()
print("\nAverage Sales by Item Type:")
print(sales_item)
# Find outlet type with highest sales
top_outlet = sales_outlet.idxmax()
print("\nOutlet type with highest sales:", top_outlet)

# Item type with highest average sales
top_item = sales_item.idxmax()
print("Item type with highest average sales:", top_item)
import matplotlib.pyplot as plt

sales_plot = sales_outlet

plt.figure(figsize=(8,5))   # bigger graph

sales_plot.plot(
    kind="bar",
    color=["#4CAF50","#2196F3","#FF9800","#E91E63"]  # colors
)

plt.title("Total Sales by Outlet Type", fontsize=14, fontweight="bold")
plt.xlabel("Outlet Type", fontsize=12)
plt.ylabel("Total Sales", fontsize=12)

plt.xticks(rotation=30)   # rotate labels so they fit
plt.tight_layout()        # prevents text cutting

plt.savefig("sales_by_outlet.png")
plt.show()