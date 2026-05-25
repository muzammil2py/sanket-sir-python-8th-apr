# Practical Example 6: Check if a number is prime

def check_prime():
    # Get user input
    num = int(input("Enter a number: "))

    # A prime number is always greater than 1
    if num > 1:
        # Check for factors from 2 up to the square root of the number
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                print(f"{num} is not a prime number.")
                print(f"Reason: {i} times {num//i} equals {num}.")
                break  # Exit the loop since we found a factor
        else:
            # This 'else' is tied to the 'for' loop. 
            # It executes ONLY if the loop completes without hitting a 'break'.
            print(f"{num} is a prime number!")
            
    else:
        # If the number is 1 or less, it's not prime
        print(f"{num} is not a prime number.")

# Run the program
check_prime()
 