def summation(Data):
      sum=0
      for i in Data:
          sum=sum+i
    
      return sum


def main():
    Marks = [78,90,56,98,77]
    ret = summation(Marks)

    print("Addition is : ",ret)

if __name__ == "__main__":
        main()

    
