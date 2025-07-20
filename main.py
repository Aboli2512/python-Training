from fetchData.readCsv import readCSV
from fetchData.performEDA import (getNullValueColumns, replaceNullValue)

# get data
filePath = " C:\Users\HP\OneDrive\Documents\pythonTraining01\data\waetherstats_toronto_daily.csv "
df = readCSV(filePath)

# get null value columns
nullValueColumns = getNullValueColumns(df)
print("Columns with Null Values:", nullValueColumns)

# get updated
# remove the empty rows-
for iColumnLabel in nullValueColumns:
    dfDropNa = replaceNullValue(df, iColumnLabel, "DROP_NULL_VALUES")

# fill with zero-
for iColumnLabel in nullValueColumns:
    dfFillNaWithZero = replaceNullValue(df, iColumnLabel, "FILL_WITH_ZERO")

# fill with median -
for icolumnLabel in nullValueColumns:
    dfFillNaWithMedian = replaceNullValue(df, iColumnLabel, "FILL_WITH_MEDIAN")

# fill with mode -
for icolumnLabel in nullValueColumns:
    dfFillNaWithMode = replaceNullValue(df, icolumnLabel, "FILL_WITH_MODE")

# fill with mean -
for icolumnLabel in nullValueColumns:
    dfFillNaWithMean = replaceNullValue(df, icolumnLabel, "FILL_WITH_MEAN")

# fill with forward fill
for icolumnLabel in nullValueColumns:
    dfFillNaWithMedianForwardFill = replaceNullValue(df, icolumnLabel, "FILL_WITH_FORWARD_FILL")

# fill with backward fill-
for icolumnLabel in nullValueColumns:
    dfFillNaWithFillWithBackwardFill = replaceNullValue(df, icolumnLabel, "FILL_WITH_BACKWARD_FILL")

# fill with interpolate-
for icolumnLabel in nullValueColumns:
    dfFillNaWithInterpolate = replaceNullValue(df, icolumnLabel, "FILL_WITH_INTERPOLATE")