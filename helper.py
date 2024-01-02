import pandas as pd

# def combine_excel_files(file1_path, file2_path, output_path):
#     # Read the data from the first Excel file
#     df1 = pd.read_excel(file1_path)

#     # Read the data from the second Excel file
#     df2 = pd.read_excel(file2_path)

#     # Combine the data from both files
#     combined_df = pd.concat([df1, df2], ignore_index=True)

#     # Write the combined data to a new Excel file
#     combined_df.to_excel(output_path, index=False)

# # Example usage
# file1_path = "./data/Data_Train.xlsx"
# file2_path = "./data/Test_set.xlsx"
# output_path = "./data/dataset.xlsx"

# combine_excel_files(file1_path, file2_path, output_path)
data=pd.read_excel("./data/Data_Train.xlsx")
print(len(data))