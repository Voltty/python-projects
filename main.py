op = input("Type of operation: ")
n1 = float(input("First number: "))
n2 = float(input("Second number: "))
if op == "+":
    r = n1 + n2
elif op == "-":
    r = n1 - n2
elif op == "/":
    r = n1 / n2
elif op == "*":
    r = n1 * n2
print(r)