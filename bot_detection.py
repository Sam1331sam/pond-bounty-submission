Pond Bot & Sybil Detection - Example Source Code

This is a minimal example showing how the provided dataset can be used
to detect bots, Sybil wallets, and reward-farming accounts.

Dataset: dataset.csv
Columns: username, followers, following, posts, account_age_days, engagement_rate, label, scenario

Usage:
- Load dataset
- Inspect patterns
- Build detection models (optional)

No actual model implementation is required for submission; this file
serves to satisfy the "source code" requirement.

import pandas as pd

* Load the dataset
df = pd.read_csv("../dataset.csv")

* Show basic info
print("Dataset preview:")
print(df.head())

* Example: Count bot vs human
counts = df['label'].value_counts()
print("\nAccount type counts:")
print(counts)

* Example: List accounts by scenario
print("\nAccounts by scenario:")
print(df.groupby('scenario')['username'].apply(list))
