📊 Google Search Analysis – Final Report

1. Introduction
This project analyzes Google Search data to demonstrate a complete data analytics workflow, from raw data cleaning to visual insights, using Python.

2. Dataset Overview
The dataset contains information related to Google search activity, including:
    ─ Keywords
    ─ Search volume
    ─ Click-through rate (CTR)
    ─ Bounce rate
    ─ Region and device type
    ─ Category and seasonal indicator
    ─ Date
The raw dataset included missing values, inconsistent date formats, extra spaces, and mixed text cases, making it suitable for a data cleaning and analysis task.

3. Data Cleaning & Preprocessing

The following preprocessing steps were performed:
─ Converted empty cells and common placeholders into NaN
─ Standardized mixed date formats into a single format (DD-MM-YYYY)
─ Removed extra spaces from text fields
─ Standardized capitalization for categorical columns (keyword, region, device, seasonal flag)
─ Converted numeric columns to proper data types
─ Filled missing numeric values using the median method to avoid skewed results
─ After cleaning, the dataset became consistent, structured, and ready for analysis.

4. Exploratory Data Analysis (EDA)

Exploratory analysis was conducted to understand patterns and relationships in the data.
       ─ Histogram to analyze search volume distribution
       ─ Boxplot to identify bounce rate variability and outliers
       ─ Scatter plot to study the relationship between search volume and CTR
These visualizations helped in identifying trends, anomalies, and overall data behavior.

5. Key Insights

─ Most keywords fall under low to medium search volume, showing a long-tail distribution
─ Bounce rate varies significantly, with noticeable outliers indicating inconsistent user engagement
─ Higher search volume does not always result in higher CTR
─ Engagement metrics show mixed correlations, suggesting multiple influencing factors

7. Conclusion

This project successfully demonstrates an end-to-end data analytics pipeline, from raw data cleaning to insight generation through visual analysis.It highlights essential data handling, analytical thinking, and visualization skills required for real-world data analytics roles.













📊Key Insights

─ Bounce rate has noticeable outliers
─ High search volume does not always mean high CTR
─ Certain categories dominate search interest

