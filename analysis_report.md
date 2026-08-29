# Sales Data Analysis Report

## 1. Introduction

This report documents the analysis performed on `sales_data.csv` using Python and the Pandas library.

The purpose of the project is to demonstrate a practical data-analysis workflow: loading a CSV dataset, inspecting its structure, validating data quality, cleaning records, calculating sales metrics, identifying the strongest product by revenue, and producing descriptive statistics.

## 2. Dataset Overview

The dataset contains:

- **Rows:** 100
- **Columns:** 7
- **Products:** 5 distinct products
- **Regions:** 4 distinct regions
- **Customer IDs:** 100 unique customer IDs

### Columns

| Column | Data Type | Description |
|---|---|---|
| Date | object | Transaction date |
| Product | object | Product sold |
| Quantity | int64 | Number of units sold |
| Price | int64 | Price associated with the transaction |
| Customer_ID | object | Customer identifier |
| Region | object | Sales region |
| Total_Sales | int64 | Total sales/revenue for the transaction |

## 3. Data Quality Checks

### Missing Values

All seven columns contain **0 missing values** in the supplied dataset.

```text
Date           0
Product        0
Quantity       0
Price          0
Customer_ID    0
Region         0
Total_Sales    0
```

The script nevertheless contains general-purpose missing-value handling:

- Numeric columns → median replacement.
- Text columns → mode replacement.
- No replacement was necessary for this dataset because no values were missing.

### Duplicate Rows

The dataset contains:

```text
Duplicate rows removed: 0
```

Therefore, all 100 records were retained after duplicate validation.

## 4. Sales Metrics

| Metric | Value |
|---|---:|
| Total Revenue | ₹12,365,048.00 |
| Average Sale | ₹123,650.48 |
| Highest Sale | ₹373,932.00 |
| Lowest Sale | ₹6,540.00 |
| Total Quantity Sold | 478 |

### Interpretation

The dataset records total revenue of approximately **₹12.37 million** across 100 transactions.

The average transaction value is **₹123,650.48**. The highest individual sale is **₹373,932.00**, while the lowest is **₹6,540.00**.

The total quantity sold is **478 units**, giving an average quantity of **4.78 units per transaction**.

## 5. Product Analysis

Revenue by product:

| Product | Total Revenue |
|---|---:|
| Laptop | ₹3,889,210 |
| Tablet | ₹2,884,340 |
| Phone | ₹2,859,394 |
| Headphones | ₹1,384,033 |
| Monitor | ₹1,348,071 |

### Key Finding

**Laptop** is the best-selling product by revenue with:

**₹3,889,210**

Its revenue is higher than every other product in the dataset.

## 6. Numerical Summary

The program generates descriptive statistics for:

- Quantity
- Price
- Total_Sales

### Quantity

| Statistic | Value |
|---|---:|
| Count | 100.00 |
| Mean | 4.78 |
| Standard deviation | 2.59 |
| Minimum | 1.00 |
| 25% | 2.75 |
| Median | 5.00 |
| 75% | 7.00 |
| Maximum | 9.00 |

### Price

| Statistic | Value |
|---|---:|
| Count | 100.00 |
| Mean | ₹25,808.51 |
| Standard deviation | ₹13,917.63 |
| Minimum | ₹1,308.00 |
| 25% | ₹14,965.25 |
| Median | ₹24,192.00 |
| 75% | ₹38,682.25 |
| Maximum | ₹49,930.00 |

### Total Sales

| Statistic | Value |
|---|---:|
| Count | 100.00 |
| Mean | ₹123,650.48 |
| Standard deviation | ₹100,161.09 |
| Minimum | ₹6,540.00 |
| 25% | ₹39,517.50 |
| Median | ₹97,955.50 |
| 75% | ₹175,792.50 |
| Maximum | ₹373,932.00 |

## 7. Methodology

The analysis follows these stages:

1. Import Pandas.
2. Load `sales_data.csv`.
3. Strip whitespace from column names.
4. Inspect dataset dimensions and columns.
5. Display data types and the first five rows.
6. Count missing values.
7. Fill missing values when required.
8. Count and remove duplicate rows.
9. Identify sales, quantity, product, and price columns.
10. Calculate total, average, highest, and lowest sales.
11. Calculate total quantity sold.
12. Group revenue by product.
13. Identify the highest-revenue product.
14. Generate descriptive statistics for numerical columns.
15. Print a completion message.

## 8. Validation and Testing

The final execution was validated in the Nyarch Linux environment.

### End-to-end result

```text
Analysis completed successfully.
```

### Validation summary

| Test | Expected | Result |
|---|---|---|
| Python starts | No interpreter error | Passed |
| Pandas import | Successful | Passed |
| CSV loading | 100 × 7 dataset | Passed |
| Missing-value check | No missing values | Passed |
| Duplicate check | 0 duplicates | Passed |
| Sales metrics | Calculated | Passed |
| Product grouping | 5 products analyzed | Passed |
| Numerical summary | Generated | Passed |
| End-to-end execution | Successful completion | Passed |

## 9. Conclusion

The analysis successfully demonstrates a complete introductory data-analysis workflow using Pandas.

The dataset is clean, with no missing values and no duplicate records. Total revenue is **₹12,365,048.00**, and **Laptop** is the highest-revenue product at **₹3,889,210.00**.

The project satisfies the core requirements of dataset exploration, data cleaning, metric calculation, product analysis, statistical summarization, testing, and visual documentation.
