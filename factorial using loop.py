#factorial using iterative statement
n=int(input("enter value"))
result=1
for i in range(n,0,-1):
    result=result*i
print("the factorial of",n, "is",result)
