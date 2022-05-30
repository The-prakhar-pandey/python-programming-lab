x=int(input("enter first side"))
y=int(input("enter second side"))
z=int(input("enter third side"))
s=(x+y+z)/2
h=(s*(s-x)*(s-y)*(s-z))**0.5
print(h)
