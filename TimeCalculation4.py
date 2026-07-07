import time
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact *i

    return fact
        
def main():
   value = int(input("Enter a number : "))
   start_time= time.time()
   ret=factorial(value)
   end_time=time.time()

   print(f"Factorial of {value} is {ret} ")

   print(f"Time required is {end_time - start_time : .5f} sec")
if __name__ == "__main__":
    main()