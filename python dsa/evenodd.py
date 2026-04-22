# def is_Even(n):
#     return n % 2 == 0


# if __name__ == "__main__":
#     n = int(input("Enter a number: "))
    
#     if is_Even(n):
#         print(f"{n} is an even number.")
#     else:
#         print(f"{n} is an odd number.")

# Efficient Approach
def is_even(n):
    return (n & 1) == 0


n = int(input("Enter a number: "))

if is_even(n):
    print("Even number")
else:
    print("Odd number")
    