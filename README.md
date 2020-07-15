# US-Census-Bureau
For the next set of questions, we will be using census data from the United States Census Bureau. Counties are political and geographic subdivisions of states in the United States. This dataset contains population data for counties and states in the US from 2010 to 2015. 

#1. Which state has the most counties in it?


#2. Only looking at the three most populous counties for each state, that are the three most populous states (in order of highest population to lowest population)?


#3. Which county has had the largest absolute change in population within the period 2010-2015?
population values are stored in columns POPESTIMATE2010 through POPESTIMATE2015, you need to consider all six columns.


#4. In this datafile, the United States is broken up into four regions using the "REGION" column.
#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with 'Washington',
# and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.
#This function should return a 5x2 DataFrame with the columns = ['STNAME', 'CTYNAME'] and the same index ID as the census_df (sorted ascending by index).
