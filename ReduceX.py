from functools import reduce

checkEven= lambda no : (no%2==0)

increment=lambda no:no+1

def Addition(no1,no2):
    return no1+no2

def main():
    data = [13,12,8,10,11,20]
    print("Input data is : ",data)

    Fdata= list(filter(checkEven,data))

    print("Data after Filter : ",Fdata)

    Mdata = list(map(increment,Fdata))
    print("Data after Map : ",Mdata)

    Rdata=reduce(Addition,Mdata)
    print("Data after Reduce : ",Rdata)


if __name__ == "__main__":
    main()