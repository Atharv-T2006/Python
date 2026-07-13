def checkEven(no):
    if(no%2==0):
        print("No. is even")

    else:
        print("No. is odd")

def main():
    value=int(input("Enter number that you want to check even or odd : "))
    checkEven(value)

if __name__ == "__main__":
    main()