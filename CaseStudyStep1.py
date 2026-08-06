import pandas 

Border="-"*50
#####################################
# Step 1 : Load the dataset
#####################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

data_path="iris.csv"

df=pandas.read_csv(data_path)

print("Dataset loaded successfully")
print("Initial entries from dataset are : ")
print(df.head())










