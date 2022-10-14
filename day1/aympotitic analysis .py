# HEre the problem is to find maximum value of the empty list by comparing the previous on 

a=[2,3,4,5]
b=[]
for x in a:
    for y in b: 
        if a[x]>b[y]:
            print(a[x])

# Index error ,it means index is out of the reange which we defining the index with a certain range but it does'nt return those o
# Because we defined the value of index which does'nt exit in those variable 


# The main reason of this type of error is to improve the volatal