import pandas as pd

df = pd.read_csv("daily_dataset\jaipur.csv", parse_dates=['date_time'], index_col='date_time')
print(df.columns)
print(df.columns[11:])
x = df.columns[:6]

for i in df.columns[11:]:
    x.append(i)
# x.extend(df.columns[11:])
print(x)
