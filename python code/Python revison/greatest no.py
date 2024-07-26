n1 = float(input("Enter your first number"))
n2 = float(input("Enter your Second number"))
n3 = float(input("Enter your Third number"))

if n1==n2>n3:
    print("Number 1 and 2 are same and greatest")
elif n2==n3>n1:
    print("Number 2 and 3 are same and greatest")
elif n3==n1>n2:
    print("Number 1 and 3 are same and greatest")
elif n1==n2==n3:
    print("All numbers are same")

elif n1>=n2>=n3 or n1>=n3>=n2:
    print("Number 1 is greatest")

elif n2>=n1>=n3 or n2>=n3>=n1:
    print("Number 2 is greatest")

else:
    print("Number 3 is greatest")