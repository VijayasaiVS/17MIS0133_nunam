#Importing Pandas for working with Data
import pandas as pd
import os
#Importing Profiler Module to Profile the Py File
import cProfile
import pstats
profiler=cProfile.Profile()
print('\nProfiling Starts...')
profiler.enable() #Enabling Profiling from here
#Saving Location of CSV files for reading
file1='./processed_data/detail.csv'
file2='./processed_data/detailVol.csv'
file3='./processed_data/detailTemp.csv'
print('\nImporting the merged csv files for processing...')
#Converting CSV to Dataframes
detail_df=pd.DataFrame(pd.read_csv(file1))
detailVol_df=pd.DataFrame(pd.read_csv(file2))
detailTemp_df=pd.DataFrame(pd.read_csv(file3))
print('\nFinished Importing!')
#Converting Object to Datetime datatype
print('\nConverting Object Type of Dates to Datetime datatype...\nSetting up the CSV as DateTime Index from RangeIndex...')
detail_df['Absolute Time']=pd.to_datetime(detail_df['Absolute Time'])
#Detail CSV is converted from RangeIndex to TimedIndex
detail_df.set_index('Absolute Time',drop=False,inplace=True)
#Converting Object to Dattime datatype
detailVol_df['Realtime']=pd.to_datetime(detailVol_df['Realtime'])
#DetailVol CSV is converted from RangeIndex to TimedIndex
detailVol_df.set_index('Realtime',drop=False,inplace=True)
#Converting Object to Dattime datatype
detailTemp_df['Realtime']=pd.to_datetime(detailTemp_df['Realtime'])
#DetailTemp CSV is converted from RangeIndex to TimedIndex
detailTemp_df.set_index('Realtime',drop=False,inplace=True)
print('\nConvertion Done Successfully')
#Detail CSV is being resample to T Frequency which is 1 minute
print('\nData being Down Sampled to 1 Sample/ Minute...\nTaking Last Data of the minute')
detail_df=detail_df.resample('T').last() #Last data of that minute is taken into account
#DetailVol CSV is being resample to T Frequency which is 1 minute
detailVol_df=detailVol_df.resample('T').last()#Last data of that minute is taken into account
#DetailTemp CSV is being resample to T Frequency which is 1 minute
detailTemp_df=detailTemp_df.resample('T').last() #Last data of that minute is taken into account
print('\nExporting the Dataframes to CSV Files')
#Converting the resampled Dataframe to CSV file in a Folder named Processed
if not os.path.exists('./processed_data'):
    os.makedirs('./processed_data') #if the direcotry is not available this will create a directory and place the csv files here
detail_df.to_csv(r'./processed_data/detailDownsampled.csv',index=False)
detailVol_df.to_csv(r'./processed_data/detailVolDownsampled.csv',index=False)
detailTemp_df.to_csv(r'./processed_data/detailTempDownsampled.csv',index=False)
print('\nFinished Exporting CSV Files\nFind your files at: ./processed_data/')
profiler.disable() #Till this line the profiler records the function
print("\nProfiling Ends!")
if not os.path.exists('./cProfileOutput'): #checks for existing folder
    os.makedirs('./cProfileOutput') #if not creating a new folder
with open("./cProfileOutput/task2.txt", "w") as f:
    ps = pstats.Stats(profiler,stream=f) #Transferring the data to stats 
    ps.sort_stats('cumulative')
    ps.print_stats() #dumping the Profiler's output in a txt folder inside the given directory
