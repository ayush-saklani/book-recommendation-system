import pandas as pd

# Load the database
df = pd.read_csv('filtered_book.csv')

# Specify the fraction of data to keep (e.g., 0.5 for 50%)
fraction_to_keep = 0.4

# Randomly sample the data
new_df = df.sample(frac=fraction_to_keep, random_state=42)  # Use a fixed seed for reproducibility

# Save the reduced database
new_df.to_csv('GoodReads_35k_books.csv', index=False)
