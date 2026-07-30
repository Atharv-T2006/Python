import time 
def SumCube(no):
    sum=0

    for i in range(1,no+1):
        sum=sum+(i**3)
    
    return sum

def main():
    Data = [10000000,20000000,30000000,40000000,50000000]
    res=[]
    start_time=time.perf_counter()
    for value in Data:
        ret = SumCube(value)
        res.append(ret)

    
    print("Result is : ")
    print(res)

    end_time = time.perf_counter()
    


    print(f"Time required is {end_time -start_time:.5f} sec")
        
    

if __name__ == "__main__":
    main()