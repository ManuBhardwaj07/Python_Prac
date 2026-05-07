# Write a program to input eight numbers from the user and display all the unique numbers (once).

unique_numbers = set()

for i in range(8):
    num = int(input("Enter number: "))
    unique_numbers.add(num)

print(unique_numbers)
