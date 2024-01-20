import pandas as pd

df = pd.read_csv('filtered_book.csv')

new_df = df.sample(0.4, random_state=42)  

new_df.to_csv('GoodReads_35k_books.csv', index=False)