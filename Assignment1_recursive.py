def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1)+ recur_fibo(n-2))
    
nterms = int(input("Enter the number of terms needed in fibonacci series :"))

if nterms <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci Series:")
    for i in range(nterms):
        print(recur_fibo(i))