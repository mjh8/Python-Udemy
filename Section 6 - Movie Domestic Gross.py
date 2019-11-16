# Movie Ratings

# Import Libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline


# Import the data
mov = pd.read_csv('Movie_Budget_Revenue_Dataset.csv', encoding = 'latin1')


# Explore the dataset
mov.head()

# Check the summary of the dataframe
mov.describe()

# Check the structure of the dataframe
mov.info()



#Factor Plot - Day of Week
vis1 = sns.factorplot(data=mov, x='Day of Week', kind = 'count', size=5)



# Explore the categorical variable Studio, used in the assignment
mov.Studio.unique()
len(mov.Studio.unique())

# Explore the categorical variable Studio, used in the assignment
mov.Genre.unique()
len(mov.Genre.unique())



# Filter the dataframe by genre
mov2 = mov[(mov.Genre == 'action') | (mov.Genre == 'adventure') | (mov.Genre == 'animation') | (mov.Genre == 'comedy') | (mov.Genre == 'drama')]

# Filter the dataframe by studio
mov3 = mov2[(mov2.Studio == 'Buena Vista Studios') | (mov2.Studio == 'Fox') | (mov2.Studio == 'Paramount Pictures') | (mov2.Studio == 'Sony') | (mov2.Studio == 'Universal') | (mov2.Studio == 'WB')]

# Check how the filters worked
print (mov3.Genre.unique())
print (mov3.Studio.unique())
print (len(mov3))



# Build Plot ->

# Define the style
sns.set(style="darkgrid", palette="muted", color_codes=True)

# Plot the boxsplots
ax = sns.boxplot(data=mov3, x='Genre', y='Gross % US', orient='v', color='lightgray', showfliers=False)
plt.setp(ax.artists, alpha=0.5)

# Add in points to show each observation
sns.stripplot(x='Genre', y='Gross % US', data=mov3, jitter=True, size=6, linewidth=0, hue = 'Studio', alpha=0.7)

ax.axes.set_title('Domestic Gross % by Genre',fontsize=20)
ax.set_xlabel('Genre',fontsize=10)
ax.set_ylabel('Gross % US',fontsize=10)

# Define where to place the legend
ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)