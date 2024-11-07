n1 = int(input("Enter first number of the series:"))
n2 = int(input("Enter second number of the series:"))
n = int(input("Enter the number of terms needed:"))
print("Fibonacci Series:")
print(n1, n2, end=" ")
while(n-2):
    num = n1 + n2
    n1 = n2
    n2 = num
    print(num, end=" ")
    n = n-1