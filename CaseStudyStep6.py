import pandas
import matplotlib.pyplot as plot 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

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


#####################################################
# Step 3 : Decide Independent and Dependent variables
######################################################

print(Border)
print("Step 3 : Decide Independent and Dependent variables")
print(Border)

# X : Independent variables / features
# Y : Dependent variables / labels

feature_cols=[
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)"
    
]

X = df[feature_cols]
Y = df["species"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)


#####################################
# Step 4 : Data visualization
#####################################

print(Border)
print("Step 4 : Data visualization")
print(Border)

# Scatter plot

plot.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"]==sp]
    plot.scatter(temp['petal length (cm)'],temp['petal width (cm)'],label = sp)
    plot.title("Iris Case Study")
    
    plot.xlabel("petal length (cm)")
    plot.ylabel("petal width (cm)")

    plot.legend()
    plot.grid()
    plot.show()


#####################################################
# Step 5  : Split the dataset for training and testing 
######################################################

print(Border)
print(" Step 5  : Split the dataset for training and testing")
print(Border)


X_train,X_test,Y_train,Y_test= train_test_split(X,Y,test_size=0.5, random_state=42)

print("X shape : ",X.shape)

print("X_train : ",X_train.shape) 
print("X_test : ",X_test.shape)

print("Y shape : ",Y.shape)

print("Y_train : ",Y_train.shape)
print("Y_test : ",Y_test.shape)

#####################################################
# Step 6  : Build the model 
######################################################

print(Border)
print("Step 6  : Build the model")
print(Border)

model= DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")
















