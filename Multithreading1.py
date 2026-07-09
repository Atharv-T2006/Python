import threading

def display():
    print("Inside display : ",threading.get_ident())

def main():
    print("Inside main : ",threading.get_ident())

    tobj=threading.Thread(target=display)

    tobj.start()

if __name__=="__main__":
    main()