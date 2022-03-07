import pandas as pd
read_df = pd.read_csv('./Instructions/Resources/cities.csv')
read_df.to_html('data.html',classes=['table', 'table-striped', 'table-hover'])