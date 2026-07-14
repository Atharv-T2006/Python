class Arithmetic:
    def __init__(self,a,b):
        self.no1=a
        self.no2=b

    def Addition(self):   # [thats why here we give three parameters (add self)]
        ans = self.no1+self.no2

        return ans

    def Substraction(self):
        ans = self.no1-self.no2

        return ans 
        

no1=int(input("Enter first number :" ))
no2=int(input("Enter second number : " ))

aobj=Arithmetic(no1,no2)


# ret = Addition(Aobj,no1,no2)   | internally treated

ret=aobj.Addition()
print("Addition is : ",ret)

ret=aobj.Substraction()
print("Addition is : ",ret)