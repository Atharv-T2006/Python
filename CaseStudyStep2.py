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

#####################################
# Step 2 : Data Analysis (EDA)
#####################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of datasset : ",df.shape)

print("Column names : ",df.columns)

print("Missing values per column : ",df.isnull().sum())

print("Class distribution [species count]")
print(df['species'].value_counts())

print("Statistical report of dataset : ")
print(df.describe())












