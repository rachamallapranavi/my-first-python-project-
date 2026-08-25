# Student Marks Calculator - By Pranavi
name = input("Enter student name: ")
telugu = int(input("Telugu marks: "))
english = int(input("English marks: "))
maths = int(input("Maths marks: "))

total = telugu + english + maths
average = total / 3

print(f"\nStudent: {name}")
print(f"Total: {total}, Average: {average:.2f}")

if average >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")
