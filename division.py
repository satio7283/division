def div (dividers=[15,34,9],Number=3):



    print("the numbers in",dividers,"that are divisible by",Number,"are: ")
    satio=0
    for i in dividers:
        if i%Number==0:
            satio+=1
            print(i)
    if satio==0:
        print("not found")

div([7,12,35,24,36],4)