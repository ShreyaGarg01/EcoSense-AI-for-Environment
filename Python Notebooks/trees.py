# %%
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas as gpd

# %%
shp_gdf = gpd.read_file('.\\India_States\\Indian_states.shp')

# %%
df = pd.read_csv('.\\Datasets\\StatewiseTreeCover.csv')
df.columns

# %%
df['State/ Uts'] = df['State/ Uts'].replace(['Delhi'], 'NCT of Delhi')
df['State/ Uts'] = df['State/ Uts'].replace(['Dadra and Nagar Haveli'], 'Dadara & Nagar Havelli')
df['State/ Uts'] = df['State/ Uts'].replace(['Daman and Diu'], 'Daman & Diu')
df['State/ Uts'] = df['State/ Uts'].replace(['Jammu and Kashmir'], 'Jammu & Kashmir')
df['State/ Uts'] = df['State/ Uts'].replace(['Andaman and Nicobar Islands'], 'Andaman & Nicobar Island')




df['State/ Uts'].unique()

# %%
shp_gdf['st_nm'].unique()
shp_gdf['st_nm'] = shp_gdf['st_nm'].replace(['Arunanchal Pradesh'], 'Arunachal Pradesh')
shp_gdf['st_nm'] = shp_gdf['st_nm'].replace(['Telangana'], 'Andhra Pradesh')


# %%
merged = shp_gdf.set_index('st_nm').join(df.set_index('State/ Uts'))
merged

# %%
fig, ax = plt.subplots(1, figsize=(12, 12))
ax.axis('off')
ax.set_title('Tree Cover ',
             fontdict={'fontsize': '15', 'fontweight' : '3'})
fig = merged.plot(column='Tree Cover - Area', cmap='Greens', linewidth=0.5, ax=ax, edgecolor='0.2', legend = True)
plt.savefig("trees.png")

