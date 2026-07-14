class Arithmetic:
    def Addition(no1,no2):
        ans = no1+no2

        return ans

    def Substraction(no1,no2):
        ans = no1-no2

        return ans 
    
aobj=Arithmetic()

no1=int(input("Enter first number :" ))
no2=int(input("Enter second number : " ))

# ret = Addition(Aobj,no1,no2)   | internally treated

ret=aobj.Addition(no1,no2)
print("Addition is : ",ret)

ret=aobj.Substraction(no1,no2)
print("Addition is : ",ret)