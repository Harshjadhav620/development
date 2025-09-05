def swap(a,b):
    t=a
    a=b
    b=t
    return (a,b)
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print("Before swap",a,b)
a,b=swap(a,b)
print("After swap",a,b)
