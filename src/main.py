import pandas as pd

path_final = r"C:\Users\shin3\Downloads\修士\final.xlsx"
path_city = r"C:\Users\shin3\Downloads\修士\Citylatlongi.xlsx"
path_geo = r"C:\Users\shin3\Downloads\修士\geocodingViolation.xlsx"

df_final = pd.read_excel(path_final)
df_city = pd.read_excel(path_city)
df_geo = pd.read_excel(path_geo)

print("final:", df_final.shape)
print(df_final.columns.tolist())

print("city:", df_city.shape)
print(df_city.columns.tolist())

print("geo:", df_geo.shape)
print(df_geo.columns.tolist())