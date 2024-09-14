import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])

# print(df.loc[["day2"]]) 

## Reading CSV files
df = pd.read_csv('data.csv')

# df will only return first and last 5 rows, df.st_string() will return the entire dataset
# print(df)

# # check maximum rows returned
# print(pd.options.display.max_rows)

# # change max rows 
# pd.options.display.max_rows = 9999
# print(df)
# print(pd.options.display.max_rows)

## Reading JSON
