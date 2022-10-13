def fact(n):
    print("Factorial callled with",str(n))
    if n<2:
        return 1
    result=n*fact(n-1)
    print("Resultng"+str(result)+"for factorial"+str(n))
    return result
fact(4)