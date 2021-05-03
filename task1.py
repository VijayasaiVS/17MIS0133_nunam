#importing required modules to work with
import pandas as pd
import os
#Importing Profiler Module to Profile the Py File
import cProfile
import pstats
profiler=cProfile.Profile()
print('\nProfiling Starts...')
profiler.enable() #Enabling Profiling from here
#Storing File Directory Location
file1='./data/data.xlsx'
file2='./data/data_1.xlsx'
print('\nImporting Excel Files to Variable...')
#Getting Excel File 1 and Storing in the variable
excel1=pd.read_excel(file1,sheet_name=None)
#Getting Excel File 2 and Storing in the variable
excel2=pd.read_excel(file2,sheet_name=None)
print('\nImporting Successfully Completed!')
#Getting Name of all Sheets in Excel 1
print('\nExtracting Sheets Names from Excel 1 and Excel 2...')
excel1_keys=excel1.keys()
all_keys_1=[]
for i in excel1_keys:
    all_keys_1.append(i)
#Getting Name of all Sheets in Excel 2
excel2_keys=excel2.keys()
all_keys_2=[]
for i in excel2_keys:
    all_keys_2.append(i)
print('\nFinished Extracting Sheet Names!')
#Choosing only Detail_67 sheets alone and storing them in list
detail=[]
for i in range(0,len(all_keys_1)):
    if(all_keys_1[i].startswith('Detail_67')):
        detail.append(all_keys_1[i])
#Choosing only DetailVol sheets alone and storing them in list
detailVol=[]
for i in range(0,len(all_keys_1)):
    if(all_keys_1[i].startswith('DetailVol_67')):
        detailVol.append(all_keys_1[i])
#Choosing only DetailTemp sheets alone and storing them in list in Excel 1
detailtemp=[]
for i in range(0,len(all_keys_1)):
    if(all_keys_1[i].startswith('DetailTemp_67')):
        detailtemp.append(all_keys_1[i])
#Choosing only DetailTemp sheets alone and storing them in list in Excel 2
detailtemp1=[]
for i in range(0,len(all_keys_2)):
    if(all_keys_2[i].startswith('DetailTemp_67')):
        detailtemp1.append(all_keys_2[i])
print('\nMerging Sheets according to Detail, DetailVol, DetailTemp...')
#Concat the Details, DetailVol, DetailTemp from each List that i previously stored and making a Dataframe of them
detail_df=pd.concat(pd.read_excel(file1,sheet_name=detail),ignore_index=True)
detailVol_df=pd.concat(pd.read_excel(file1,sheet_name=detailVol),ignore_index=True)
detailtemp_df1=pd.concat(pd.read_excel(file1,sheet_name=detailtemp),ignore_index=True)
detail_temp_df2=pd.concat(pd.read_excel(file2,sheet_name=detailtemp1),ignore_index=True)
#DetailTemp1 and DetailTemp2 is concatenated now to form a single Dataframe
detailtemp_df=pd.concat([detailtemp_df1,detail_temp_df2],ignore_index=True)
print('\nFinished Merging')
print('\nRemoving any available Duplicate data...')
#Dropping any duplicate Data present in the Dataframe
detail_df.drop_duplicates('Record Index',keep='first',inplace=True)
detailVol_df.drop_duplicates('Record ID',keep='first',inplace=True)
detailtemp_df.drop_duplicates('Record ID',keep='first',inplace=True)
print('\nExporting the Dataframes to CSV Files')
#Finally converting Dataframes to CSV files
if not os.path.exists('./processed_data'):
    os.makedirs('./processed_data') #if the direcotry is not available this will create a directory and place the csv files here
detail_df.to_csv('./processed_data/detail.csv',index=False)
detailVol_df.to_csv('./processed_data/detailVol.csv',index=False)
detailtemp_df.to_csv('./processed_data/detailTemp.csv',index=False)
print('\nFinished Exporting CSV Files\nFind your files at: ./processed_data/')
profiler.disable() #Till this line the profiler records the function
print("\nProfiling Ends!")
if not os.path.exists('./cProfileOutput'): #checks for existing folder
    os.makedirs('./cProfileOutput') #if not creating a new folder
with open("./cProfileOutput/task1.txt", "w") as f:
    ps = pstats.Stats(profiler,stream=f) #Transferring the data to stats 
    ps.sort_stats('cumulative')
    ps.print_stats() #dumping the Profiler's output in a txt folder inside the given directory