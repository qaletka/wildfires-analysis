import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/areaburntbywildfiresbyweeknew.csv')

years = ['area burnt by wildfires in 2024', ' burnt by wildfires in 2023', ' burnt by wildfires in 2022',
         ' burnt by wildfires in 2021', ' burnt by wildfires in 2020', 'area burnt by wildfires in 2019',
         'a burnt by wildfires in 2018', 'area burnt by wildfires in 2017', ' area burnt by wildfires in 2016',
         ' area burnt by wildfires in 2015', 'area burnt by wildfires in 2014', ' area burnt by wildfires in 2013',
         ' area burnt by wildfires in 2012']

total_area_burnt = df[years].sum()

plt.figure(figsize=(10, 6))
plt.bar(total_area_burnt.index, total_area_burnt.values, color='orangered')

plt.xlabel('Year')
plt.ylabel('Area burnt by wildfires (in million hectares)')
plt.title('Total area burnt by wildfires over the years')

plt.xticks(total_area_burnt.index, [year.split()[-1] for year in total_area_burnt.index], rotation=45)

plt.tight_layout()
plt.show()
