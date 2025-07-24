from fetchData.readCsv import readCSV
# filePath = r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\waetherstats_toronto_daily.csv "
filePath = r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_dropna.csv"
df = readCSV(filePath)

# print(df[0:15])
sliced_df = df.iloc[0:15, [2, 3, 4, 5]]
print(sliced_df)

correlation_matrix = sliced_df.corr()
print(correlation_matrix)

