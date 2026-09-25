def find_gcd():
    print("Enter two positive integers to find their GCD:")
    
    try:
        n = int(input("Enter first integer (n): "))
        m = int(input("Enter second integer (m): "))
        
        if n <= 0 or m <= 0:
            print("Please enter positive integers greater than 0.")
            return
            
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return
    d = min(n, m)
    while m % d != 0 or n % d != 0:
        d -= 1
    print(f"The GCD is {d}")
if __name__ == "__main__":
    find_gcd()