import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("demand_forecasting_dataset.csv")
dataset50 = dataset.head(50)

# ===================================
# What is the general behavior of demand over time? (first 50 days)
# ===================================

"""
time = dataset["date"]
demand = dataset["target_demand"]

plt.xlabel("Time")
plt.ylabel("Demand")
plt.title("Demand - Time Graph")

graph = plt.plot(time.head(50), demand.head(50))

plt.show()
"""

# ===================================
# Analysis of sales differences by product and store
# ===================================

"""
for product in dataset["product_id"].unique():  # unique() ensures each product is taken once
    max_sales = np.max(
        dataset[dataset["product_id"] == product]["historical_sales"]
    )

    store = dataset[
        (dataset["product_id"] == product) &
        (dataset["historical_sales"] == max_sales)
    ]["store_id"].values[0]

    print(f"{product} - max sales: {max_sales} - store: {store}")
"""

# ===================================
# Do promotions really work?
# ===================================

"""
daily_demand = (
    dataset50
    .groupby(["date", "promotion_flag"])["target_demand"]
    .mean()
    .reset_index()
)

promotion_yes = daily_demand[daily_demand["promotion_flag"] == 1]
promotion_no = daily_demand[daily_demand["promotion_flag"] == 0]

promotion_yes = promotion_yes.sort_values("date")
promotion_no = promotion_no.sort_values("date")

plt.plot(
    promotion_yes["date"],
    promotion_yes["target_demand"],
    label="Promotion Yes"
)

plt.plot(
    promotion_no["date"],
    promotion_no["target_demand"],
    label="Promotion No"
)

plt.xlabel("Date")
plt.ylabel("Average Demand")
plt.title("Daily Average Demand (Promotion Effect)")
plt.legend()
plt.show()
"""

# ===================================
# Which products have the highest demand?
# ===================================

results = []

for product in dataset["product_id"].unique():
    total_demand = dataset[dataset["product_id"] == product]["target_demand"].sum()
    results.append((product, total_demand))

# x[0] represents product_id and x[1] represents total demand
# sorting from highest demand to lowest demand
results.sort(key=lambda x: x[1], reverse=True)

# for product, total in results:
#     print(f"{product} - total demand: {total}")

results_df = pd.DataFrame(results, columns=["product_id", "total_demand"])
print(results_df.head())