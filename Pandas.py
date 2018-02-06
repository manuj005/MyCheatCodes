# Video 2
# Column Access, Index, TO List, Array

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
'''
web_stats = {'Day' : [1,2,3,4,5,6],
             'Visitors' : [43,53,34,45,64,34],
             'Bounce_Rate' : [65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
# df = df.set_index('Day')
df.set_index('Day',inplace=True)

# print(df)
print(df['Visitors'])
print(df.Visitors)
print(df[['Visitors','Bounce_Rate']])

# Convert to list
print(df.Visitors.tolist())

# Convert to list for multiple columns doesn't work
# Will have to use NP.array
print(np.array(df[['Visitors', 'Bounce_Rate']]))

# Converting back to DF from list
df2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_Rate']]))
print(df2)
'''

# Video 3
# I/O in Pandas, Column Rename, Index
'''
import pandas as pd

# Read and set index
df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')
df.set_index('Date', inplace = True)

# write as csv
#df.to_csv('with_index.csv')

# read with index
df_index =  pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv', index_col=0)

# Index is NOT A COLUMN anymore
# Rename
df.columns = ['House_Price_Index']

# Writing eithout colnames
df.to_csv('newcsv2.csv', header=False)

# Read csv w/o colnames and give it colnames:
df2 = pd.read_csv( 'newcsv2.csv', names = ['Date', 'HPI'], index_col=0)
print(df2.head())

# Saving it as an HTML file
df.to_html('myhtml.html')

# Renaming a single column
df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')
print(df.head())
df.rename(columns = {'Date' : 'NewDate'}, inplace = True)
print(df.head())
'''

# Video 5
# Combining Datasets : Concatenate and Append
'''
import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

# When Columns are same, just add rows :
concat = pd.concat([df1,df3])
print(concat)

df4 = df1.append(df3)
print(df4)

s = pd.Series([80, 2, 50], index = ['HPI','Int_rate','US_GDP_Thousands'])
# will not add with index, it will have to be removed
df5 = df1.append(s, ignore_index=True)
print(df5)
'''

# Video 6
# Merging and joining
'''
import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#print(pd.merge(df1,df2, on = 'HPI')) # Here, Duplicate coluns formed
#print(pd.merge(df1,df2, on = ['HPI', 'Int_rate'])) # Index are gone



df4 = pd.DataFrame({'Year':[2001, 2002, 2003, 2004],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df5 = pd.DataFrame({'Year':[2001, 2003, 2004, 2005],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})

### Merge doesn't care about the index ############
merged = pd.merge(df4, df5, on = 'Year') # (Inner) Here 2002, 2005 omitted
merged = pd.merge(df4,df5, on = 'Year', how = 'left') # Left Join
merged = pd.merge(df4,df5, on = 'Year', how = 'right') # Right Join
merged = pd.merge(df4,df5, on = 'Year', how = 'outer') # Union kind
merged.set_index('Year', inplace = True)
print(merged)


######################## Join takes care of Index ##########
df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]})

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]})

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)
print(joined)
'''

# Video 4, 7
# Building dataset, pickling
'''
import quandl
import pandas as pd
import pickle

api_key = 'eB5myx3QjQXUbcXWsGWL'
df_test = quandl.get('Fmac/HPI_AK', authtoken = api_key)

def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    #print(fiddy_states) # This is a list
    #print(fiddy_states[0]) # This is a DF
    #print(fiddy_states[0][0]) # This is a column
    return fiddy_states[0][0][1:]

def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()

    # Now make get url for each state after 1st element
    for abbv in states:
        query = 'Fmac/HPI_' + str(abbv)
        df = quandl.get(query, authtoken = api_key)
        df.columns = [str(abbv)]

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df)

    #print(main_df.head())

    pickle_out = open('fiddy_states.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

# grab_initial_state_data()

pickle_in = open('fiddy_states.pickle','rb')
HPI_data = pickle.load(pickle_in)
#print(HPI_data)

# Pandas Version of Pickle

HPI_data.to_pickle('PandaPickle.pickle')
HPI_data_2 = pd.read_pickle('PandaPickle.pickle')
print(HPI_data_2)
'''

# Video 8
# Mathematical functions in Pandas
'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
HPI_data_2 = pd.read_pickle('PandaPickle.pickle')

HPI_data_2['TX2'] = HPI_data_2['TX'] * 2
# print(HPI_data_2[['TX','TX2']])

#HPI_data_2.plot()
#plt.legend().remove()
#plt.show()


# Video 9
# Resampling- If we have readings for every minute of 5 yrs data, want for each day

TX1yr = HPI_data_2['TX'].resample('A').mean()
# A- Year end frequency , MEAN is default

HPI_data_2['TX'].plot()
TX1yr.plot()

plt.legend().remove()
plt.show()
'''

# Video 10
# Missing value handling
'''
HPI_data_2 = pd.read_pickle('PandaPickle.pickle')
HPI_data_2['TX1yr'] = HPI_data_2['TX'].resample('A', how = 'mean')
print(HPI_data_2[['TX','TX1yr']])

HPI_data_2.dropna(inplace = True # Completely drops rows with NA
# HPI_data_2.dropna(inplace = True, how = 'all') # Will drop if all rows NAN
# HPI_data_2.dropna(thresh = 5,inplace = True) # Number of NAN atleast to drop

HPI_data_2.fillna(method = 'ffill', inplace = true) # Older data shifted to next NAN
HPI_data_2.fillna(method = 'bfill', inplace = true) # Future data shifted to prev NAN
HPI_data_2.fillna(value = -99999, limit = 100, inplace = true) # Put limit for number of replaced
print(HPI_data_2.isnull().values.sum()) # Gives number of NANin DF
print(HPI_data_2[['TX','TX1yr']])

HPI_data_2.replace([np.inf, -np.inf], np.nan, inplace = True)
# Replaces infinities by NAN
'''

# Video 11
# Rolling Functions
'''
HPI_data = pd.read_pickle('PandaPickle.pickle')
HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12) # Mean over 12 data points
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12) # STD over 12 data points
HPI_data['TX12CORR'] = pd.rolling_corr(HPI_data['TX'], 12) # Corr over 12 data points

print(HPI_data['TX'].head(20))
print(HPI_data['TX12MA'].head(20))

HPI_data[['TX','TX12MA']].plot()
plt.legend(loc = 2)
plt.show()
'''

# Video 12
# Comparison
'''
bridge_height = {'meters':[10.26, 10.31, 10.27, 10.22, 10.23, 6212.42, 10.28, 10.25, 10.31]}
df = pd.DataFrame(bridge_height)

# How to find the error values
df['std'] = pd.rolling_std(df['meters'], 2)

df_std = df.describe()['meters']['std']
print(df_std)

df = df[ (df['std'] < df_std) ]
print(df)
df.plot()
plt.show()
'''

# Video 15
# Mapping and crerating label for machine Learning
'''
def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

housing_data = pd.read_pickle('abs')
housing_data.replace([np.inf, -np.inf], np.nan, inplace= True)

housing_data['future'] = housing_data['colname'].shift(-1)

###################### MAP Function #############
housing_data['labels'] = list(map(create_labels, housing_data['colname'], housing_data['future']))
# Function, followed by parameters
'''
