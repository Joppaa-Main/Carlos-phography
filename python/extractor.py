import pandas as pd


# Webpage url                                                                                                               
url = 'https://www.tesco.com/groceries/en-GB/shop/fresh-food/all'

# Extract tables
dfs = pd.read_html(url)

# Get first table                                                                                                           


# df = dfs[0]

# # Extract columns                                                                                                           
# df2 = df[['Version','Release date']]
print("carlos")