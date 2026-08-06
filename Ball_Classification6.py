from sklearn import tree
# Rough = 1
# smooth = 0

#tennis =1
#cricket=2


def main():
    print('Ball Classification Case Study')

    Independent=[[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]]
    # testing features = [35,1],[95,0]

    Dependent=[1,1,2,1,2,1,2,1,1,1,2,1,2]
    # testing labels =[1,2]

    model = tree.DecisionTreeClassifier()

    model=model.fit(Independent,Dependent)

    Result=model.predict([[35,1],[95,0]])

    print("predicted result of model is : ",Result)




if __name__=="__main__":
    main()