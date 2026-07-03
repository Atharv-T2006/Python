def summation(Data):
    sum=0
    for i in Data:
        sum = sum + i
       
    return sum

         

def main():
    size = 0
    Arr = list()

    print("Enter the no. of elements : ")
    size=int(input())
    
    print("Enter the elements : ")
    for i in range(size):
        no = int (input())
        Arr.append(no)
    
    print("Your list is : ",Arr)

    ret = summation(Arr)
    print("Summation is : ",ret)
    
if __name__ == "__main__":
        main()

    