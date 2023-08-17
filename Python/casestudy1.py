import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv('Downloads/investments.csv')

print(df.columns)

df2 = df.select_dtypes(include='object')

df.describe()

## there is no row-level duplicates
df.duplicated().sum()

# there are three duplicates at ['name','category_list','market'] level
df.duplicated(subset=['name','category_list','market']).sum()

### records having duplicates
df[df.duplicated(subset=['name','category_list','market'])]

## finding duplicate copies
df = (df.name == 'AYOXXA Biosystems') & (df.category_list == '|Biotechnology|') & (df.market == 'Biotechnology')
df[f]

### deleting duplicate records
df.drop_duplicates(subset=['name','category_list','market'],keep = False, inplace=False).shape

cnt_m = df.isnull().sum() # count of missing values
per_m = df.isnull().sum()/df.shape[0]*100 # percentages of missing values
pd.concat([cnt_m, per_m], axis = 1, keys = ['count_M', 'percentage_M']).sort_values('percentage_M', ascending= False)

df.groupby('country_code')['name'].count()

df[df.status.isin(['operating','acquired'])].shape[0]/len(df)*100

df[df.founded_year.isna()].shape[0]

df['category_list_count'] = df.category_list.apply(lambda x: len(str(x).split('|')) - 2)
df.loc[:,['category_list','category_list_count']].head()

df.funding_total_usd = df.funding_total_usd.apply(lambda x: x.replace(',','').replace('-','0')).astype(float)
df.groupby('country_code')['funding_total_usd'].mean()

df.groupby('country_code')['funding_total_usd'].sum()

df.groupby(['country_code', 'region'])['funding_total_usd'].mean()

print(df[df.funding_rounds == 1]['name'].shape[0]) ### including duplicates names
print(len(df[df.funding_rounds == 1]['name'].unique())) ### excluding duplicates names
print(df[df.funding_rounds == 1]['name'].nunique()) ### excluding duplicates names + nan
print(df[df.funding_rounds == 1]['name'].count()) ## excluding nan

df.status.apply(lambda x: 'A' if x== 'acquired' else 'O' if x == 'operating' else 'C' if x== 'closed' else 'missing')

import re
df.homepage_url.apply(lambda x: re.sub('http://www.|.com', '', str(x))).head() 

df.groupby('market')['name'].count()

df['cnt_name'] = df.groupby('market')['name'].transform('count')

df.city.fillna('other_city', inplace = True)

df.country_code.fillna('other_country', inplace = True)

df.groupby('country_code')['funding_total_usd'].transform(lambda x: x/np.max(x))

df.groupby('city')['funding_total_usd'].mean()

fig, ax = plt.subplots(1,2,figsize = (20,5))
ax[0].hist(df.funding_total_usd)
ax[0].set_xlabel('funding_total_usd')
ax[0].set_ylabel('count of funding_total_usd')
ax[0].set_title('histogram of funding_total_usd')

ax[1].hist(np.log1p(df.funding_total_usd))
ax[1].set_xlabel('log of funding_total_usd')
ax[1].set_ylabel('count of funding_total_usd')
ax[1].set_title('histogram of log transformed funding_total_usd')
plt.show()

df.groupby('market')['funding_total_usd'].max()

from datetime import datetime
df['company_age'] =  datetime.today().year-df.founded_year
df.head()

fig, ax = plt.subplots(1,2,figsize = (20,5))
ax[0].hist(df.grant)
ax[0].set_xlabel('grant')
ax[0].set_ylabel('count of grant')
ax[0].set_title('histogram of grant')

ax[1].hist(np.log1p(df.grant), color = 'g')
ax[1].set_xlabel('log of grant')
ax[1].set_ylabel('count of grant')
ax[1].set_title('histogram of log transformed grant')
plt.show()

fig, ax = plt.subplots(1,2,figsize = (20,5))
ax[0].hist(df.grant)
ax[0].set_xlabel('grant')
ax[0].set_ylabel('count of grant')
ax[0].set_title('histogram of grant')

ax[1].hist(np.log1p(df.grant), color = 'g')
ax[1].set_xlabel('log of grant')
ax[1].set_ylabel('count of grant')
ax[1].set_title('histogram of log transformed grant')
plt.show()

df.status.value_counts()/df.shape[0]*100

df[df.country_code == 'USA']['state_code'].nunique()

df['cmt_address'] = df.country_code + '-'+df.state_code+'-'+df.region+'-' + df.city

df.filter(regex = '_').head()
