def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

print("Please select operation:-\n"
      "1. Add\n"
      "2. Subtract\n"
      "3. Multiply\n"
      "4. Divide\n")

ch = int(input("Select operation (1-4): "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if ch == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif ch == 2:
    print(n1, "-", n2, "=", sub(n1, n2))
elif ch == 3:
    print(n1, "*", n2, "=", mul(n1, n2))
elif ch == 4:
    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print(n1, "/", n2, "=", div(n1, n2))
else:
    print("Invalid input")
