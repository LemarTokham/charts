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
# df = pd.read_json('data.json')
# print(df)

# loading python dictionary into DataFrame
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.read_json("data.json")
print(df.head(2))
print(df.tail())

## Info about the data
print(df.info()) # tells us that calories has 5 rows with null values

## Cleaning Data
# dropna() creates a new dataframe
# new_df = df.dropna()
# print(new_df.info())

# modifying existing dataframe
# df.dropna(inplace=True)
# print(df.info())

# filling null values with 120
# df.fillna(130, inplace=True)
# print(df.info())

# fill specified coloumns
#df["Calories"].fillna(130, inplace=True)

# replace empty cells with mean, media or mode
# replaced_df =pd.read_json('data.json')
# x = replaced_df["Calories"].mean()
# replaced_df["Calories"] = replaced_df["Calories"].fillna(x)
# print(replaced_df.to_string())

