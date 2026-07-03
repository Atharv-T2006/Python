
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
    
if __name__ == "__main__":
        main()

    