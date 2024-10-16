num = int(input("What is the integer you want: "))
ans = bin(num)[2:]  # Removes the "0b" prefix

print("The binary string is", ans)

