number=int(input("Enter number: "))
if number>1:
    for x in range(2,number):
        if(number%x)==0:
            print("Not a prime number")
            break
        else:
            print("Prime number")
            break
    else:
        print("Not prime")
