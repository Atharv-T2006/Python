
def SumCube(no):
    sum=0

    for i in range(1,no+1):
        sum=sum+(i*i*i)
    
    return sum

def main():
    ret = SumCube(5)
    print("Result is :",ret)

if __name__ == "__main__":
    main()