name = input("Enter your name: ")

print("\n1. Right Angle")
print("2. Left Angle")
print("3. Pyramid")

choice = int(input("Enter your choice: "))

if choice == 1:
    for i in range(1, len(name) + 1):
        print(name[:i])

elif choice == 2:
    for i in range(1, len(name) + 1):
        print(" " * (len(name) - i) + name[:i])

elif choice == 3:
    for i in range(1, len(name) + 1):
        left = name[:i]
        right = name[:i - 1][::-1]
        print(" " * (len(name) - i) + left + right)

else:
    print("Invalid choice")