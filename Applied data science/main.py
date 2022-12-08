import io
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
from scipy.stats import norm

df = pd.read_csv('amazon_prime_titles.csv')
df.head()

correct = 0


new_df= df.drop(['show_id', 'type', 'title', 'director', 'cast', 'country', 'date_added', 'rating','listed_in', 'description'], axis=1)
duration = new_df['duration']

for i in range(len(duration)):
    fix = duration[i].split(' ')
    if (fix[1] == 'Season') or (fix[1] == 'Seasons'):
        duration[i] = np.nan
    
    else:
        duration[i] = int(fix[0])
mean_value = new_df['duration'].mean()

new_df['duration'].fillna(value=mean_value, inplace=True)

dfSample = new_df.sample(9600)
# title

plt.title('Duration of Movies', fontsize=20)

# plot

plt.gca().set(xlim=(1920,2020))
sns.regplot(x="release_year", y= "duration", data=dfSample, scatter_kws={'s':40, 'alpha':0.7,'color':'lightgray'})

# saves the image
plt.savefig("movie_duration1.png")

# shows the image
plt.show()

print(new_df)

# print(len(duration))

