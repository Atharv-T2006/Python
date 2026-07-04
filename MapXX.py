checkEven= lambda no : (no%2==0)

increment= lambda no:no+1

def main():
    data = [13,12,8,10,11,20]
    print("Input data is : ",data)

    Fdata= list(filter(checkEven,data))

    print("Data after Filter : ",Fdata)

    Mdata = list(map(increment,Fdata))
    print("Data after Map : ",Mdata)


if __name__ == "__main__":
    main()