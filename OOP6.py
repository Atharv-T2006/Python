class Demo:
    # class variables
    value1=10
    value2=20

    def __init__(self):
        self.no1=11
        self.no2=21

obj1=Demo()
obj2=Demo()

obj1.no1=0

print(obj1.no1)                                                                                           
print(obj2.no1)

Demo.value1=0

print(Demo.value1)





