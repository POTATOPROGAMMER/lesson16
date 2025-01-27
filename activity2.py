def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide (a,b):
    return a/b
print("a.add")
print("b.subtract")
print("c.multiply")
print("d.divide")
choice =  input("please enter choice a/b/c/d")
num_1 = int(input ("enter the first number: "))
num_2 = int(input ("enter the second number: "))
if choice =='a':
    print(add(num_1,num_2))
elif choice=='b':
    print(subtract(num_1,num_2))
elif choice=='c':
    print(multiply(num_1,num_2))
elif choice=='d':
    print(divide(num_1,num_2))
else :
    print("invalid input")echo "# lesson16" >> README.md

