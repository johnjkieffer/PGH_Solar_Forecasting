import numpy as np
import pandas as pd
import os
import math

# List of cities from which data was recorded
cities = os.listdir('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data')
# Years during which data was recorded
years = range(1998,2019)

# Create data frames for each city by appending all the years together. 
PITdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Pittsburgh, PA/PIT_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 PITdf = PITdf.append(tempdf)

GREdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Greensburg, PA/GRE_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 GREdf = GREdf.append(tempdf)

JONdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Johnstown, PA/JON_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 JONdf = JONdf.append(tempdf)

MGTdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Morgantown, WV/MGT_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 MGTdf = MGTdf.append(tempdf)

WASdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Washington, PA/WAS_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 WASdf = WASdf.append(tempdf)

WHLdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Wheeling, WV/WHL_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 WHLdf = WHLdf.append(tempdf)

PKSdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Parkersburg, WV/PKS_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 PKSdf = PKSdf.append(tempdf)

CBGdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Cambridge, OH/CBG_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 CBGdf = CBGdf.append(tempdf)

STUdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Steubenville, OH/STU_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 STUdf = STUdf.append(tempdf)

NPHdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/New_Philadelphia, OH/NPH_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 NPHdf = NPHdf.append(tempdf)

ELVdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/East_Liverpool, OH/ELV_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 ELVdf = ELVdf.append(tempdf)

YGTdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Youngstown, OH/YGT_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 YGTdf = YGTdf.append(tempdf)

NCSdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/New_Castle, PA/NCS_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 NCSdf = NCSdf.append(tempdf)

BUTdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Butler, PA/BUT_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 BUTdf = BUTdf.append(tempdf)

KITdf = pd.DataFrame(columns = ['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction'])
for i in years:
	 temp = pd.read_csv('../PGH_Solar_Forecasting/Solar_Wind_and_Cloud_Data/Kittanning, PA/KIT_' + str(i) + '.csv', header = 2)
	 tempdf = temp[['Year', 'Month','Day','Hour','Minute','DNI','Wind Speed','Wind Direction']]
	 KITdf = KITdf.append(tempdf)

# Next, split wind direction and wind speed into wind_x and wind_y and decide how to normalize or scale

PITdf['wind_x'] = np.cos(np.radians(PITdf['Wind Direction']))
# Next, split Month and Day into day_x and day_y and decide how to normalize

# Next, split Hour and Minute into time_x and time_y and decide how to normalize

# Next, find the max DNI for each city at each time of year (over the years given) and name this
# DNI_max. It should have dimension 1 x len(1year)
# Divide all DNI values by the corresponding max DNI value and subtract from 1 to get a cloudiness variable











