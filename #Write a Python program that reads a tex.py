#Write a Python program that reads a text file named numbers.txt that contains 20 integers. The program will create two other text file; the first text file will be named even.txt that will contain all even numbers extracted from numbers.txt. The second text file will be named odd.txt that will contain all odd numbers extracted from the numbers.txt.
print ("This program is created to separate even and odd numbers from 20 integers.")
#read input file
with open ("integers.txt", "r") as numbers_file:
    integers = list(map(int, numbers_file.read().split()))
#create two lists
even_numbers = []
odd_numbers = []
#determine if odd or even
for num in integers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
#define even numbers
with open("even.txt", "w") as numbers_file:
    for num in even_numbers:
        numbers_file.write(str(num) + "\n")
#define odd numbers
with open("odd.txt", "w") as numbers_file:
    for num in odd_numbers:
        numbers_file.write(str(num) + "\n")