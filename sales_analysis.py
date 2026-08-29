import pandas as pd

# 1. Load the CSV file using pandas.#36AEE8
df = pd.read_csv("sales_data.csv")

# Clean column names by removing accidental leading/trailing spaces.
df.columns = [column.strip() for column in df.columns]

print("=" * 70)
print("SALES DATA ANALYSIS REPORT")
print("=" * 70)

# 2. Explore the dataset.
print("\n1. DATASET OVERVIEW")
print("-" * 70)
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")
print("\nColumns:")
print(list(df.columns))

print("\nData types:")
print(df.dtypes)

print("\nFirst 5 rows:")
print(df.head())

# 3. Check for missing values.
print("\n2. MISSING VALUES")
print("-" * 70)
print(df.isnull().sum())

# Fill missing values appropriately.
for column in df.columns:
    missing = df[column].isnull().sum()

    if missing > 0:
        if pd.api.types.is_numeric_dtype(df[column]):
            # Median is less affected by extreme values than the mean.
            df[column] = df[column].fillna(df[column].median())
        else:
            # For text columns, use the most frequent value.
            mode = df[column].mode()
            replacement = mode.iloc[0] if not mode.empty else "Unknown"
            df[column] = df[column].fillna(replacement)

# 4. Remove duplicate rows.
duplicate_count = df.duplicated().sum()
df = df.drop_duplicates()

print(f"\nDuplicate rows removed: {duplicate_count}")
print(f"Missing values remaining: {df.isnull().sum().sum()}")

# 5. Identify common sales columns.
def find_column(candidates):
    lower = {column.lower(): column for column in df.columns}

    for candidate in candidates:
        if candidate.lower() in lower:
            return lower[candidate.lower()]

    for column in df.columns:
        normalized = column.lower().replace(" ", "_")
        if any(candidate in normalized for candidate in candidates):
            return column

    return None

sales_col = find_column(
    ["Total_Sales", "total sales", "sales", "revenue", "amount", "total"]
)
quantity_col = find_column(
    ["Quantity", "qty", "units", "units_sold"]
)
product_col = find_column(
    ["Product", "product_name", "item"]
)

# If revenue is not directly stored, calculate it from quantity * unit price.
price_col = find_column(["Price", "Unit_Price", "unit price"])

if sales_col is None and quantity_col and price_col:
    df["Total_Sales"] = df[quantity_col] * df[price_col]
    sales_col = "Total_Sales"

# 6. Calculate sales metrics.
print("\n3. SALES METRICS")
print("-" * 70)

if sales_col:
    total_revenue = df[sales_col].sum()
    average_sale = df[sales_col].mean()
    highest_sale = df[sales_col].max()
    lowest_sale = df[sales_col].min()

    print(f"Total Revenue       : ₹{total_revenue:,.2f}")
    print(f"Average Sale        : ₹{average_sale:,.2f}")
    print(f"Highest Sale        : ₹{highest_sale:,.2f}")
    print(f"Lowest Sale         : ₹{lowest_sale:,.2f}")
else:
    print("A sales/revenue column could not be identified.")

if quantity_col:
    total_quantity = df[quantity_col].sum()
    print(f"Total Quantity Sold : {total_quantity:,.0f}")

# 7. Find the best-selling product by revenue.
print("\n4. PRODUCT ANALYSIS")
print("-" * 70)

if product_col and sales_col:
    product_sales = (
        df.groupby(product_col)[sales_col]
        .sum()
        .sort_values(ascending=False)
    )

    print("Sales by product:")
    print(product_sales.to_string())

    best_product = product_sales.idxmax()
    print(f"\nBest-selling product by revenue: {best_product}")
    print(f"Revenue from best product      : ₹{product_sales.max():,.2f}")
else:
    print("Product/revenue columns could not be identified.")

# 8. Show simple statistics for numerical columns.
print("\n5. NUMERICAL SUMMARY")
print("-" * 70)
print(df.select_dtypes(include="number").describe().round(2))

print("\n" + "=" * 70)
print("Analysis completed successfully.")
print("=" * 70)
