import io
import pandas as pd
import numpy as np
import missingno as msno
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
from scipy.stats import norm

df = sns.load_dataset('amazon_prime_titles')
df.head()
df = df.sample(n=1000, random_state= 20)




plt.title('Duration of Movies', fontsize=20)

# plot
sns.regplot(df.release_year, df.duration);

# saves the image
plt.savefig("movie_duration1.png")

# shows the image
plt.show()

print(new_df)

# print(len(duration))