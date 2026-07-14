class Arithmetic:
    def Addition(self,no1,no2):   # [thats why here we give three parameters (add self)]
        ans = no1+no2

        return ans

    def Substraction(self,no1,no2):
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