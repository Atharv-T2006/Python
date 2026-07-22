class Demo:
    # class variables
    value1=10
    value2=20

    def __init__(self):
        self.no1=11
        self.no2=21

   # instance method 
    def fun(self):
        print("Inside instance method named as fun")
        print(self.no1)
        print(self.no2)
        print(Demo.value1)
        print(Demo.value2)
    
    @classmethod
    def gun(cls):
        print("Inside class method named as gun")
        # print(Demo.no1)   error
        # print(Demo.no2)   error  
        print(cls.value1)
        print(cls.value2)

    @staticmethod
    def sun():
        print("Inside static method named as sun")
         
        print(Demo.value1)
        print(Demo.value2)


Demo.sun()



