import pandas as pd

# Load the dataset
data = pd.read_csv('dataset.csv')

# Display basic info
print("Dataset Info:")
print(data.info(), "\n")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(data.head(), "\n")

# Count number of bots vs humans
bot_count = data[data['label'] == 'bot'].shape[0]
human_count = data[data['label'] == 'human'].shape[0]

print(f"Number of bot accounts: {bot_count}")
print(f"Number of human accounts: {human_count}")

# Optional: simple detection example
print("\nExample detection based on engagement rate:")
low_engagement_bots = data[data['engagement_rate'] < 0.05].shape[0]
print(f"Accounts with very low engagement (possible bots): {low_engagement_bots}")
