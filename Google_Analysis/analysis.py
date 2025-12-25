import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# LOAD DATA
df = pd.read_csv("data/raw/raw.csv")
print("Data loaded & merged:", df.shape)

# CLEANING
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df = df.replace(
    [" ", "NaN"],np.nan
)
df.drop_duplicates(inplace=True)

# DATE CLEANING & SORTING
def fix_date(date_str):
    try:
        parts = str(date_str).replace('/', '-').split('-')
        if len(parts) == 3:
            year = parts[0].zfill(4)
            month = parts[1].zfill(2)
            day = parts[2].zfill(2)
            return f"{year}-{month}-{day}"
        else:
            return date_str
    except:
        return pd.NaT
df['date'] = df['date'].apply(fix_date)
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%d-%m-%Y')
df = df.sort_values(by='date')

# Numeric columns
num_cols = [
    "search_volume","trend_score","click_through_rate","bounce_rate","avg_session_time"
]
for col in num_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].fillna(df[col].median())

# Fix ranges
df["search_volume"] = df["search_volume"].abs()
df["bounce_rate"] = df["bounce_rate"].clip(0, 100)
df["click_through_rate"] = df["click_through_rate"].clip(0, 100)

# Text columns
df['keyword'] = df['keyword'].astype(str).str.strip().str.title()
df['is_seasonal'] = df['is_seasonal'].astype(str).str.strip().str.capitalize()
df['region'] = df['region'].astype(str).str.strip().str.capitalize()
df["category"] = df["category"].astype(str).str.strip().str.title()
df["device"] = df["device"].astype(str).str.strip().str.title()
print("Data cleaned")

# SAVE CLEAN DATA
df.to_csv("data/clean/google_cleaned.csv", index=False)
# DESCRIPTIVE STATISTICS
print(df.describe())
df.describe().to_csv("data/processed/descriptive_statistics.csv")
print("Data Saved in CSV")
# BAR CHART 
cat_avg = df.groupby("category")["search_volume"].mean()
plt.figure()
cat_avg.plot(kind="bar")
plt.title("Average Search Volume by Category")
plt.ylabel("Search Volume")
plt.tight_layout()
plt.savefig("visuals/bar_category_search_volume.png", dpi=300)
plt.close()
# PIE CHART
device_sum = df["device"].value_counts()
plt.figure()
device_sum.plot(kind="pie", autopct="%1.1f%%")
plt.title("Device Usage Share")
plt.ylabel("")
plt.savefig("visuals/pie_device_share.png", dpi=300)
plt.close()
# SCATTER PLOT
plt.figure()
plt.scatter(df["search_volume"], df["click_through_rate"])
plt.title("Search Volume vs CTR")
plt.xlabel("Search Volume")
plt.ylabel("CTR")
plt.savefig("visuals/scatter_volume_vs_ctr.png", dpi=300)
plt.close()
# BOX PLOT
plt.figure()
plt.boxplot(df["bounce_rate"], vert=False)
plt.title("Bounce Rate Distribution")
plt.xlabel("Bounce Rate")
plt.savefig("visuals/boxplot_bounce_rate.png", dpi=300)
plt.close()

# CONTOUR PLOT
x = df["search_volume"]
y = df["click_through_rate"]
xi = np.linspace(x.min(), x.max(), 50)
yi = np.linspace(y.min(), y.max(), 50)
xi, yi = np.meshgrid(xi, yi)
zi = np.sin(xi / 1000) + np.cos(yi)
plt.figure()
plt.contourf(xi, yi, zi, cmap="viridis")
plt.colorbar()
plt.title("Contour Plot (Synthetic Relationship)")
plt.xlabel("Search Volume")
plt.ylabel("CTR")
plt.savefig("visuals/contour_plot.png", dpi=300)
plt.close()

df.groupby("category").mean(numeric_only=True) \
  .reset_index().to_csv("data/processed/category_summary.csv", index=False)
df.groupby("device").mean(numeric_only=True) \
  .reset_index().to_csv("data/processed/device_summary.csv", index=False)
df.groupby("region").mean(numeric_only=True) \
  .reset_index().to_csv("data/processed/region_summary.csv", index=False)
print("PROJECT COMPLETED SUCCESSFULLY✅")
print("\nKEY INSIGHTS:\n• Education, Career,& Finance keywords show consistently high search volumes.")
print("• Search interest peaks during exams, jobs & financial periods.")