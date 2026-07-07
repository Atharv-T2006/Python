
def factorial(num):
    fact = 1
    for i in range(1,num):
        fact += fact *i

    return fact
        
def main():
   value = int(input("Enter a number : "))
   ret=factorial(value)

   print("Factorial is : ",ret)
if __name__ == "__main__":
    main()