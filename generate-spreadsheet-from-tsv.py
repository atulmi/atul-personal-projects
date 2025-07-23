# Goal of this program: generate a spreadsheet from a set of TSV (tab separated values) files
# The spreadsheet will have separate tabs containing each file's content (with the tab name being same as filename)
# Example usage: python3 generate-spreadsheet-from-tsv.py Book-List.tsv Articles-List.tsv Games-List.tsv

import pandas as pd
import sys
import os

from pandas.io.formats import excel
excel.ExcelFormatter.header_style = None

pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 2000)
pd.set_option('display.width', 2000)

file_array = [] # array of filenames
df_array = []   # array containing content of each file

# Loop through all TSV files passed in
for file in sys.argv:

    # ensure TSV file exists before reading
    if file == sys.argv[0] or os.path.exists(file) == False:
       continue

    print("file being read: ", file) # print file being read for debugging purposes

    df = pd.read_csv(file, delimiter="\t")
    df.drop(df.filter(regex="Unnamed"),axis=1, inplace=True)

    df_array.append(df) # append full contents of file to array of file contents
    file_array.append(file)


with pd.ExcelWriter('multiple.xlsx', engine='xlsxwriter') as writer:
    
    # Loop through array containing each file's contents
    for index, df in enumerate(df_array):

        # get filename (filter out initial part of path)
        sheetName = file_array[index].rsplit('/', 1)[-1].split('.')[0][:20]

        df.to_excel(writer, sheet_name=sheetName, index=False, startrow=0, startcol=0)

        currentSheet = writer.sheets[sheetName]
        numberColumns = currentSheet.dim_colmax

        currentSheet.set_column(0, 0, 10)
        currentSheet.set_column(0, numberColumns - 1, 30)
