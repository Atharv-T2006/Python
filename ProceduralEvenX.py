def checkEven(no):
    if(no%2==0):
        return True

    else:
        return False

def main():
    value=int(input("Enter number that you want to check even or odd : "))
    ret = checkEven(value)
    print(ret)

    if(ret == True):
        print("Its Even number")

    else:
        print("Its Odd number")


if __name__ == "__main__":
    main()