def sum(lengtharray):
    result=[]
    total = 0
    for i in range(lengtharray):
        n = int(input("Get result"))
        result.append(n)
    print(result)
    for i in result:
        total += i
    print("total sum=", total)

sum(2)