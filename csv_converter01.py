import pandas as pd
import time
import arcpy

start = time.time()

#### 1.)import the csv into a pandas dataframe ####
print("Reading csv's")
safegraph1_df = pd.read_csv('E:/SafeGraph Project/2019/01/patterns-part1.csv')
print('part 1 read')
safegraph2_df = pd.read_csv('E:/SafeGraph Project/2019/01/patterns-part2.csv')
print('part 2 read')
safegraph3_df = pd.read_csv('E:/SafeGraph Project/2019/01/patterns-part3.csv')
print('part 3 read')
safegraph4_df = pd.read_csv('E:/SafeGraph Project/2019/01/patterns-part4.csv')
print('part 4 read')

#print out all headers
for col in safegraph1_df.columns:
    print(col)

#set csv to a pandas dataframe (this may not be necessary)
print("creating dataframes\n- Time elapsed:", time.time() - start)
df1 = pd.DataFrame(safegraph1_df)
df2 = pd.DataFrame(safegraph2_df)
df3 = pd.DataFrame(safegraph3_df)
df4 = pd.DataFrame(safegraph4_df)

#### 2.)use pandas loc function to create a dataframe for each state
#capture all rows that have TN, GA, AL located in them from the regions column
print("locating TN, GA, and AL regions\n- Time elapsed:", time.time() - start)

df1_TN = df1.loc[(df1['region'] == 'TN')]
df1_GA = df1.loc[(df1['region'] == 'GA')]
df1_AL = df1.loc[(df1['region'] == 'AL')]

df2_TN = df2.loc[(df2['region'] == 'TN')]
df2_GA = df2.loc[(df2['region'] == 'GA')]
df2_AL = df2.loc[(df2['region'] == 'AL')]

df3_TN = df3.loc[(df3['region'] == 'TN')]
df3_GA = df3.loc[(df3['region'] == 'GA')]
df3_AL = df3.loc[(df3['region'] == 'AL')]

df4_TN = df4.loc[(df4['region'] == 'TN')]
df4_GA = df4.loc[(df4['region'] == 'GA')]
df4_AL = df4.loc[(df4['region'] == 'AL')]

#### 3.)export dataframes to an excel file format ####
#create a variable that calls all dataframes
print("combining located data frames\n- Time elapsed:", time.time() - start)
frames = [df1_TN, df1_GA, df1_AL, df2_TN, df2_GA, df2_AL, df3_TN, df3_GA, df3_AL, df4_TN, df4_GA, df4_AL]

#append all dataframes into a master dataframe
print("appending located data frames\n- Time elapsed:", time.time() - start)
final_df = pd.concat(frames)

#export dataframe into a .xlsx file so it can easily imported into a ArcPro
print("exporting to .xlsx file\n- Time elapsed:", time.time() - start)
final_df.to_excel('E:/SafeGraph Project/2019/01/patterns_TN_GA_AL_01.xlsx')

print("Excel to Table\n- Time elapsed:", time.time() - start)
arcpy.conversion.ExcelToTable(r"E:\SafeGraph Project\2019\01\patterns_TN_GA_AL_01.xlsx", r"G:\Shared drives\IGTLab Drive\Data\SafeGraph\2019\Gdb_01-12_TN_GA_AL_Tables\Gdb_01-12_TN_GA_AL_Tables.gdb\Gdb_2019_01_TN_GA_AL", '')

print("Total Process time:", time.time() - start)

