import pandas as pd

url = 'https://www.playstation.com/en-us/'
tables = pd.read_html(url)

print(f"Number of tables found: {len(tables)}")

if tables:
    first_table = tables[0]
    print(first_table)


else:
    print("No tables found on the page")
