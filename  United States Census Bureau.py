import pandas as pd
census_df = pd.read_csv('census.csv')
census_df.head()


#1. Which state has the most counties in it?
#(hint: consider the sumlevel key carefully! You'll need this for future questions too...)
# This function should return a single string value.
def answer_five():
    c_copy = census_df.copy().groupby(['STNAME']).sum()  #groupby state name and sum up
    c_copy = c_copy.sort_values(by= ['COUNTY'],ascending=False)
    return c_copy.index[0]
answer_five()

#2. Only looking at the three most populous counties for each state,
# hat are the three most populous states (in order of highest population to lowest population)?
# Use CENSUS2010POP.
# This function should return a list of string values.

def answer_six():
    c_copy = census_df.copy() # make a copy first
    c_copy = c_copy[c_copy['SUMLEV'] >= 45]  #filter the data where SUMLEV=50
    c_copy.sort_values(by=['CENSUS2010POP'], inplace=True,ascending=False)   #sort the data by population

    newcopy = c_copy.groupby(['STNAME']).head(3)  #use head directly on after groupby method to have a top 3 counties from each state
    result = newcopy.groupby(['STNAME']).sum() #group the data for the second time, by STNAME, and apply sum method


    result.sort_values(by=['CENSUS2010POP'], inplace=True,ascending=False) #sort the data again by population

    str = result.index[0:3] #take the top 3 States

    list = str.values.tolist()   #convert to a list of string
    return list

answer_six()


#3. Which county has had the largest absolute change in population within the period 2010-2015?
# (Hint: population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.)
# e.g. If County Population in the 5 year period is 100, 120, 80, 105, 100, 130, then its largest change
# in the period would be |130-80| = 50.
#This function should return a single string value.
def answer_seven():
    copy = census_df.copy()
    copy = copy[copy['SUMLEV'] >= 45]
    copy = copy.set_index(['CTYNAME'])
    # create two columns of max and min by comparing 6 columns
    copy['max'] = copy[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015',]].max(axis=1)
    copy['min'] = copy[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015',]].min(axis=1)
    #create anonther column for the absolute change
    copy['absolute change']=copy['max']-copy['min']
    copy = copy.sort_values(by='absolute change',ascending = False)
    return copy.index[0]
answer_seven()

#4. In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington',
# and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
def answer_eight():
    copy = census_df.copy()
    copy = copy[(copy['SUMLEV'] >= 45) & (copy['REGION'] <=2) & (copy['POPESTIMATE2015']-copy['POPESTIMATE2014']>0)]

    copy = copy[copy['CTYNAME'].str.match('Washington')]  #find the counties starting with 'Washington'
    copy = copy[['STNAME','CTYNAME']]   #only the take 'STNAME'and 'CTYNAME' two columns
    return copy
answer_eight()
