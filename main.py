from fetchData.readCsv import readCSV
from fetchData.performEDA import (getNullValueColumns, replaceNullValue)

# get data
filePath = r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\waetherstats_toronto_daily.csv "
df = readCSV(filePath)
# remove duplicates rows here 


numeric_columns = df.select_dtypes(exclude=['object']).columns.tolist()
# get null value columns
nullValueColumns = getNullValueColumns(df)
common = list(set(nullValueColumns) & set(numeric_columns))
# print("Columns with Null Values:", nullValueColumns)

# copies for each operation
# dfDropNa = df.copy()
# dfFillNaWithZero = df.copy()
# dfFillNaWithMedian = df.copy()
# dfFillNaWithMode = df.copy()
# dfFillNaWithMean = df.copy()
# dfFillNaWithForwardFill = df.copy()
# dfFillNaWithBackwardFill = df.copy()
# dfFillNaWithInterpolate = df.copy()

# get updated
# remove the empty rows-
for iColumnLabel in common:
    dfDropNa = replaceNullValue(df, iColumnLabel, "DROP_NULL_VALUES")
    dfFillNaWithZero = replaceNullValue(df, iColumnLabel, "FILL_WITH_ZERO")
# fill with median -
    dfFillNaWithMedian = replaceNullValue(df, iColumnLabel, "FILL_WITH_MEDIAN")
# fill with mode -for icolumnLabel in nullValueColumns:
    dfFillNaWithMode = replaceNullValue(df, iColumnLabel, "FILL_WITH_MODE")

# fill with mean -
    dfFillNaWithMean = replaceNullValue(df, iColumnLabel, "FILL_WITH_MEAN")

# fill with forward fill
    dfFillNaWithForwardFill = replaceNullValue(df, iColumnLabel, "FILL_WITH_FORWARD_FILL")

# fill with backward fill-
    dfFillNaWithBackwardFill = replaceNullValue(df, iColumnLabel, "FILL_WITH_BACKWARD_FILL")

# fill with interpolate-
    dfFillNaWithInterpolate = replaceNullValue(df, iColumnLabel, "FILL_WITH_INTERPOLATE")


# saved the cleaned files--

dfDropNa.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_dropna.csv")
dfFillNaWithMedian.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithMedian.csv")
dfFillNaWithMode.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithMode.csv")
dfFillNaWithMean.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithMean.csv")
dfFillNaWithZero.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithZero.csv")
dfFillNaWithBackwardFill.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithBackward.csv")
dfFillNaWithForwardFill.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_FillWithForward.csv")
dfFillNaWithInterpolate.to_csv(r"C:\Users\HP\OneDrive\Documents\pythonTraining01\data\cleaned_fillWithInterpolate.csv")
